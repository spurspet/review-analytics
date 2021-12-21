# 留言小于100的清单

data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '笔留言长度包含good.')
print(good[0])
