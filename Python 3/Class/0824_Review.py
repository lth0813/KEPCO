a=0x8ff
print(a)

b="Life is too short\nYou need Python"
print(b)

multiline='''Life is too short
You need Python'''
print(multiline)

c='My Program'
print('='*50)
print(f'{c:=^50}')
print('='*50)

d='20230824Rainy'
date=d[4:8]
year=d[:4]
weather=d[8:]
print(date, year, weather)

e="Hi!! Pithon!!"
e=e[:6]+'y'+e[7:]
print(e)

f=3.1425796321
print('%0.4f' %f)

g='Hello'
print(f'{g:^15}')

h='python'
print(f'{h:!^12}')

i='banana'
print(i.count('a'))
print(i.find('a'))
print(i.rfind('a'))
print(i.find('c'))
print(i.index('a'))
print(i.rindex('a'))

print(i.index('a'))
print(i[2:].index('a'))
print(i[4:].index('a'))

j='hobby'
print(j.index('b'))
print(j[3:].index('b'))

print(e[:4]+e[4:].replace('i','y'))

print(j.upper())

k='Life is too short'
print(k.split('i'))








