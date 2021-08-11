try:
    f = open('modhhcom.txt','r+')
    print(f.readlines())
except:
    print('File Not found')


