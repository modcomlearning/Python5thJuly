


with open('modcom.txt','w+', encoding='utf-8') as f:
    f.write('Its Fun here\n')
    f.write('Its Awesome\n')


f = open('modcom.txt','r+')
# print(f.read())

for line in f:
    print(line, end='')


