import string
import random

list_of_char_lower_case = list(string.ascii_letters)
list_of_char_upper_case = list(string.ascii_uppercase)
list_of_digits = list(string.digits)
list_of_punctuation = list(string.punctuation)

char_num = input('How many character do you need : ')

while True:
    try:
        char_num = int(char_num)
        if char_num < 6:
            print('enter at least 6 number')
            char_num = input('How many character do you need : ')
        else:
            break
    except:
        print('please enter numbers only')
        char_num = input('How many character do you need : ')

random.shuffle(list_of_char_lower_case)
random.shuffle(list_of_char_upper_case)
random.shuffle(list_of_digits)
random.shuffle(list_of_punctuation)

part1 = round(char_num * (30 /100))
part2 = round(char_num * (20 /100))

password = []

for i in range(part1):
    password.append(list_of_char_lower_case[i])
    password.append(list_of_char_upper_case[i])

for i in range(part2):
    password.append(list_of_digits[i])
    password.append(list_of_punctuation[i])


random.shuffle(password)
password= "".join(password[0:])
print(password)