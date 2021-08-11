import Lesson5a

try:
    with open('modcom.txt','r+', encoding='utf-8') as f:
        print(f.read())

except:
    print('File not Found')

finally:
    answer = Lesson5a.add(4,5)
    print(answer)



