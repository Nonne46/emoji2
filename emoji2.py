from re import findall
emoji = open('zbsconfig.txt', 'r').read().split("\n", 15)  #нужен файл zbsconfig.txt заполнить 16 строк по одному смайлу, иначе жопа отвалиться
emoji2hex = dict(zip(emoji, ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]))

def checkArguments(thin, A, B):
	if thin not in [A, B]:
		print("Ошибка: аргументы где??")
		raise SystemExit

def regular(text):
	return findall(":\w+:", text)

cryptMode=input("Что будем? [Ч]итать или [П]исать? Всё остальное будет воспринято предательством: ")
checkArguments(cryptMode, 'Ч', 'П')

final = ""
if (cryptMode == 'Ч'):
	answer=input("Что будем читать? [К]артины или [П]исьменные произведения: ")
	checkArguments(answer, 'К', 'П')

	if (answer == 'К'):
		answer = input("Место действа: ")

		filedata = open(answer, 'r').read()
	
		for symbol in regular(filedata):
			if symbol in emoji2hex:
				final += emoji2hex[symbol]

		answer=input("Название картины: ")
		
		open(answer, 'wb').write(bytes.fromhex(final))
	else:
		answer = input("Вставляй: ")

		for symbol in regular(answer):
			if symbol in emoji2hex:
				final += emoji2hex[symbol]

		final = bytes.fromhex(final).decode('cp1251')
		print(final)
else:
	answer=input("Что будем писать? [К]артины или [П]исьменные произведения: ")
	checkArguments(answer, 'К', 'П')
	
	if (answer == 'К'):
		answer = input("Название картины: ")
		
		filedata = open(answer, 'rb').read().hex()
		
		for symbol in filedata:
			for key in emoji2hex:
				if symbol == emoji2hex[key]:
					final += key

		answer=input("Куда ставить картину: ")
		
		print("Чтобы отправить это, потребуеться ~"+str(len(final) / 2000)+" сообщений..")
		
		open(answer, 'w').write(final)
	else:
		answer = input("Пиши: ").encode('cp1251').hex()

		for symbol in answer:
			for key in emoji2hex:
				if symbol == emoji2hex[key]:
					final += key
		print(final)