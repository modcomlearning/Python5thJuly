
marks = int(input('Enter some marks: '))
print('You scored ', marks)

if marks < 30:
    print('You Failed')

elif marks >= 30 and marks < 50:
    print('You got below average')

elif marks >= 50 and marks < 75:
    print('You have above average')

elif marks >=75 and marks < 99:
    print('Passed')

else:
    print('Invalid')