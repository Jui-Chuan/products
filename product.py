#讀取檔案
product = []
with open ('product.csv' ,'r', encoding= 'utf-8') as f:
	for line in f :
		if'商品,價格' in line
			continue     #跳出這一回直接進入下一回
		name,price = line.strip().split (',')  #把換行符號用掉
		product.append ([name,price])

#讓使用者輸入
while True :
		name = input ('請輸入商品名稱:')
		if name == 'q':
			break
		price = input ('請輸入商品價格:') 
		p = []             #可以直接寫 p[name, price]
		p.append (name)
		p.append (price) 
		product.append (p)  #或直接寫product.append([name,price])
print (product)

#印出所有購買紀錄
for pr in product:
	print (pr[0],'的價格是',pr[1])


#寫入檔案
with open ('product.csv' , 'w', encoding= 'utf-8') as f:    #把寫的內容存入電腦裡
	f.write ('商品,價格')
	for p in product:
		f.write (p[0] + ',' + p[1] + '\n')