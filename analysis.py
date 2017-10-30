a = [[],[],[]] # если длина ключа равно 4 то  a = [[],[],[],[]] 

f = open('vigenere.txt', 'r') 
s = f.read()
s = s.replace(chr(10), '')
#print(s)
f.close()
for i in range(0,len(s)):
    a[i % 3].append(s[i]) #если длина ключа 4 то  a[i % 4].append(s[i])
dic1 ={'А':0,'Б':0,'В':0,'Г':0,'Д':0,'Е':0,'Ж':0,'З':0,'И':0,'Й':0,'К':0,'Л':0,'М':0,'Н':0,'О':0,'П':0,'Р':0,'С':0,'Т':0,'У':0,'Ф':0,'Х':0,'Ц':0,'Ч':0,'Ш':0,'Щ':0,'Ъ':0,'Ы':0,'Ь':0,'Э':0,'Ю':0,'Я':0,'_':0}
for i in a[0]:
		if i in dic1.keys():
			dic1[i] += 1
#-------получение частот 2 столбца и расчет коэффициентов
dic2 = {'А':0,'Б':0,'В':0,'Г':0,'Д':0,'Е':0,'Ж':0,'З':0,'И':0,'Й':0,'К':0,'Л':0,'М':0,'Н':0,'О':0,'П':0,'Р':0,'С':0,'Т':0,'У':0,'Ф':0,'Х':0,'Ц':0,'Ч':0,'Ш':0,'Щ':0,'Ъ':0,'Ы':0,'Ь':0,'Э':0,'Ю':0,'Я':0,'_':0}
for i in a[1]:
		if i in dic2.keys():
			dic2[i] += 1

print('Рассчет для 2 столбца')
keys = sorted(dic2.keys())
vals = []
vals2 = vals[:]
offset_2 = 0
for i in keys:
    vals.append(dic2[i])

for i in range(1, 34):
    buf = vals[-i:] + vals[:-1]
    for f in range(len(keys)):
        dic2[keys[f]] = buf[f]
    ssum = 0
    mc = 0
    for j in sorted(dic2.keys()):
        ssum += dic1[j] * dic2[j]
    mc = ssum / (len(a[0]) * len(a[1]))
    if mc > 0.053 and mc < 0.07:
        print('Сдвиг = ', i, ' коэффициент = ', mc)
        offset_2 = i
        sdic2 = dic2.copy()
        #print(sdic2)
		
#-------получение частот 3 столбца и расчет коэффициентов
dic3 = {'А':0,'Б':0,'В':0,'Г':0,'Д':0,'Е':0,'Ж':0,'З':0,'И':0,'Й':0,'К':0,'Л':0,'М':0,'Н':0,'О':0,'П':0,'Р':0,'С':0,'Т':0,'У':0,'Ф':0,'Х':0,'Ц':0,'Ч':0,'Ш':0,'Щ':0,'Ъ':0,'Ы':0,'Ь':0,'Э':0,'Ю':0,'Я':0,'_':0}
for i in a[2]:
		if i in dic3.keys():
			dic3[i] += 1

print('Рассчет для 3 столбца')
keys = sorted(dic3.keys())

vals = []
vals2 = vals[:]
offset_3 = 0
for i in keys:
    vals.append(dic3[i])

for i in range(1, 34):
    buf = vals[-i:] + vals[:-1]
    for f in range(len(keys)):
        dic3[keys[f]] = buf[f]

    ssum = 0
    mc = 0
    for j in sorted(dic3.keys()):
        ssum += dic1[j] * dic3[j]
    mc = ssum / (len(a[0]) * len(a[2]))
    if mc > 0.053 and mc < 0.07:
        offset_3 = i
        print('Сдвиг = ', i, ' коэффициент = ', mc)
        sdic3  = dic3.copy()
        #print(sdic3)

		
'''
Если столбцов 4 то просто копирнуть блок коэффициентов и рассчета и поставить туда имя нового словаря, к примеру dic4 вместо dic2
Индекс в а соответственно будет a[4]
'''
#--------вывод столбцов со сдвигами
tt = sorted(dic1.keys())
ff = list(tt)
for i in range(len(sorted(dic1.keys()))):
    print(ff[i], ff[(i-offset_2) % 33], ff[(i - offset_3) %33])
