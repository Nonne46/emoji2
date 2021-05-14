import strutils, tables, re, encodings
from sequtils import zip, toSeq, mapIt

proc getEmojis(): seq[string] = split(readFile("zbsconfig.txt"), "\c\n")

proc getKeys(emojis: seq[string]): (Table[string, char], Table[char, string]) =
    var emoji2hex = initTable[string, char]()

    for enh in zip(emojis, ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']):
        let (emoji, hex) = enh
        emoji2hex[emoji] = hex

    var hex2emoji = toSeq(emoji2hex.pairs).mapIt((it[1], it[0])).toTable
    return (emoji2hex, hex2emoji)

proc regular(text: string): seq[string] = findAll(text, re":\w+:")

proc encryptDecrypt(mode, message: string): string =
    var final: string = ""
    let (emoji2hex, hex2emoji) = getKeys(getEmojis())

    if mode == "Ч":
        for symbol in regular(message):
            if emoji2hex.hasKey(symbol):
                final.add(emoji2hex[symbol])
        final = final.parseHexStr().convert("utf-8", "cp1251")
    else:
        var hMessage = message.convert("cp1251", "utf-8").toHex().toLower()
        for symbol in hMessage:
            if hex2emoji.hasKey(symbol):
                final.add(hex2emoji[symbol])
    return final

proc encryptDecryptFile(mode, filename, outfile: string) =
    var final: string = ""
    let (emoji2hex, hex2emoji) = getKeys(getEmojis())

    if mode == "Ч":
        let filebytesemoji = readFile(filename)
        for symbol in regular(filebytesemoji):
            if emoji2hex.hasKey(symbol):
                final.add(emoji2hex[symbol])
        final = final.parseHexStr()
    else:
        let filebyteshex = readFile(filename).toHex().toLower()
        for symbol in filebyteshex:
            if hex2emoji.hasKey(symbol):
                final.add(hex2emoji[symbol])
    writeFile(outfile, final)

proc checkArguments(thin, a, b: string) =
    if not (thin in [a, b]):
        echo "Ошибка: аргументы где??"
        system.quit(1)

var cryptMode, cryptType, startMessage, filename, outfile: string

stdout.write "С чем собираемся иметь дело? С [К]артинами или [П]исьменными произведениями: "
cryptType = stdin.readLine
checkArguments(cryptType, "К", "П")

if cryptType == "П":
    stdout.write "Что будем? [Ч]итать или [П]исать? Всё остальное будет воспринято предательством: "
    cryptMode = stdin.readLine
    checkArguments(cryptMode, "Ч", "П")

    stdout.write "Пиши: "
    startMessage = stdin.readLine

    echo encryptDecrypt(cryptMode, startMessage)
else:
    stdout.write "Что будем? [Ч]итать или [П]исать? Всё остальное будет воспринято предательством: "
    cryptMode = stdin.readLine
    checkArguments(cryptMode, "Ч", "П")

    stdout.write "Название картины: "
    filename = stdin.readLine

    stdout.write "Где её разместим: "
    outfile = stdin.readLine
    encryptDecryptFile(cryptMode, filename, outfile)

