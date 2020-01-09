with open('zbsconfig.txt', 'r') as file: #нужен файл zbsconfig.txt заполнить 16 строк по одному смайлу, иначе жопа отвалиться
	emoji = file.readlines()
	file.close()
for line in range(0,16):
    emoji[line] = emoji[line].rstrip("\n")

answer=input("Чо будем? Читать(0) или писать(1), всё остальное будет воспринято предательством: ")

hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
tmp = ["#0","#1","#2","#3","#4","#5","#6","#7","#8","#9","#a","#b","#c","#d","#e","#f"]
if (int(answer) == 0):

	answer=input("Чо будем читать? Картины(0) или письменные произведения(1): ")
	
	if (int(answer) == 0):
		answer=input("Место действа: ")
		with open(answer, 'r') as file:
			filedata = file.read()
	

		for eh in range(0,16):
			filedata = filedata.replace(emoji[eh], hex[eh])

		answer=input("Название картины: ")
		
		with open(answer, 'wb') as file:
			file.write(bytes.fromhex(filedata))

	elif (int(answer) == 1):
		answer=input("Вставляй: ")
		
		for eh in range(0,16):
			answer = answer.replace(emoji[eh], hex[eh])
		answer = bytes.fromhex(answer).decode('cp1251')
		print(answer)



elif (int(answer) == 1):

	answer=input("Чо будем писать? Картины(0) или письменные произведения(1): ")
	
	if (int(answer) == 0):
		answer=input("Название картины?: ")
		
		with open(answer, 'rb') as file:
		  filedata = file.read().hex()
		
		for eh in range(0,16):
			filedata = filedata.replace(hex[eh],tmp[eh])
		countMsg = len(filedata) / 2000
		for eh in range(0,16):
			filedata = filedata.replace(tmp[eh],emoji[eh])
		
		answer=input("Куда ставить картину: ")
		
		print("Чтобы отправить это, потребуеться ~"+str(countMsg)+" сообщений..")
		
		with open(answer, 'w') as file:
		  file.write(filedata)
	elif (int(answer) == 1):
		answer=input("Пиши: ").encode('cp1251').hex()

		for eh in range(0,16):
			answer = answer.replace(hex[eh],tmp[eh])
		for eh in range(0,16):
			answer = answer.replace(tmp[eh],emoji[eh])
	
		print(answer)