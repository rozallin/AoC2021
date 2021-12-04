#Advent of Code 2021 Day 1 Part 2

inputFile = open('1.1_input.txt', 'r')
l = list(map(int, inputFile.read().splitlines()))
result = 0
s = sum(l[:3])
for i in range(3, len(l)):
	n = s + l[i] - l[i - 3]
	if n > s:
		result += 1
print(result)
inputFile.close()
