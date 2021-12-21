# 留言小于100的清单

data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])
