# 读取评价内容的程序

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))

print(data[0])
print('-------------')
print(data[1])