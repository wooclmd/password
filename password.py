password = '123456'
t = 5 
while t > 0:
	reply = input('請輸入密碼: ')
	if reply == password : 
		print('登入成功')
		break
	else:
		t = t - 1
		print('登入失敗, 還有' , t , '次機會')