#Задача «Делаем срезы»
s = input()
print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])
print(s[1::2])
print(s[0:-1:2])
print(s[::-1])
print(s[-1:0:-2])
print(len(s))


#Задача «Количество слов»
a = input(':')
print(a.count(' ') + 1)


#Задача «Две половинки»
s = input(':')
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])


#Задача «Первое и последнее вхождения»
s = input(':')
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))


#Задача «Удаление фрагмента»
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


#Задача «Замена подстроки»
a = input(':')
print(a.replace('1', 'one'))


#Задача «Удаление символа»
a = input(':')
print(a.replace('@', ''))


#Задача «Замена внутри фрагмента»
s = input(':')
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)


#Задача «Минимум из двух чисел»
a = int(input(':'))
b = int(input(':'))
if a < b:
    print(a)
else:
    print(b)


#Задача «Знак числа»
x = int(input(':'))
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)


#Задача «Шахматная доска»
x1 = int(input('число от 1 до 8 каждое: '))
y1 = int(input('число от 1 до 8 каждое: '))
x2 = int(input('число от 1 до 8 каждое: '))
y2 = int(input('число от 1 до 8 каждое: '))
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')


#Задача «Сколько совпадает чисел»
a = int(input(':'))
b = int(input(':'))
c = int(input(':'))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)


#Задача «Ход ладьи»
x1 = int(input(':'))
y1 = int(input(':'))
x2 = int(input(':'))
y2 = int(input(':'))
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


#Задача «Шоколадка»
n = int(input(':'))
m = int(input(':'))
k = int(input(':'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')


#Задача «Яша плавает в бассейне»
n = int(input(':'))
m = int(input(':'))
x = int(input(':'))
y = int(input(':'))
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
if x < y:
    print(x)
else:
    print(y)