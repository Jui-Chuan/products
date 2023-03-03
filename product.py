product = []
while True :
		name = input ('請輸入商品名稱:')
		if name == 'q':
			break
		price = input ('請輸入商品價格:') 
		p = []
		p.append (name)
		p.append (price)
		product.append (p)
print (product)
for pr in product:
	print (pr[0],'的價格是',pr[1])