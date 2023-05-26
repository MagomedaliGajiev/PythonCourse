with open("ppp\\test.txt", 'w') as data:
    data.write("asdsfff\n")
    data.write("fuck you bitch")
data.close

data2 = open("ppp\\test.txt", 'r')
for i in data2:
    print(i)

spisok = ['232', '222', 'sdasd']

data3 = open("ppp\\test1.txt", 'w')
data3.writelines(spisok)
data.close()