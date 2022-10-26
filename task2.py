#  задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
def packing(line):
	arr = []
	count = 1
	result = []
	for i in range(len(line)):
		if len(arr) == 0:
			arr.append(line[i])
		elif arr[-1] == line[i]:
			count += 1
		elif arr[-1] != line[i]:
			arr.append(count)
			result.append(arr)
			arr = []
			count = 1
			arr.append(line[i])
		if i == len(line) - 1:
			arr.append(count)
			result.append(arr)
	return result
	
def unpacking(arr):
	text = ""
	for i in arr:
		text += i[0] * i[1]
	return text

def open_file():
	with open("BD.json", "r", encoding="utf-8") as file:
		data = json.load(file)
		return data

def save(BD):
	with open('BD.json', 'w', encoding = 'utf-8') as saves:
		saves.write(json.dumps(BD, ensure_ascii=False))
		print("База данных сохранена!")

save(packing(open_file()))

print(unpacking(open_file()))