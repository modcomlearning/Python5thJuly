# functions can return values

def bmi(weight, height):
    #weight = 56.5
    #height = 1.5
    answer = weight / (height * height)
    return answer


# how to return values
# the answer is returned below
answer = bmi(weight=45, height=1.2)
print('Answer is ', answer)

if answer<10:
    print('okay')

