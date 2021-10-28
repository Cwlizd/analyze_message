data =[] 
count = 0

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 ==0:
		    print(len(data))
print('complete reading data')

sum_len = 0
for d in data:
	sum_len += len(d)
print('總共留言長度為:',sum_len)

message = []
for d in data:
	if len(d) <= 100:
		message.append(d)
print('小於100總比數為:',len(message))

