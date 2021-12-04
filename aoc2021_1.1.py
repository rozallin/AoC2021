inputFile = open('1.1_input.txt', 'r')

l = list(map(int, inputFile.read().splitlines()))
result = 0
for i in range(1, len(l)):
	if l[i] > l[i-1]:
		result += 1
print(result)

inputFile.close()
