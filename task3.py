# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
def serch_text(line):
	if 'абв' in line:
		return False
	else:
		return True
	
lin = 'лыолы абв оуллв абвооко'.split()
a = list(filter(serch_text, lin))
print(serch_text(lin), a)