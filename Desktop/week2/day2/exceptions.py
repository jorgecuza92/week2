# TRY AND EXCEPT
# try:
#     number = int(input('enter a number: ')) # enter a letter here
# except ValueError:
#     print('Enter a number, not any other characters')

try:
    zero = int(input('try to divide by 0: '))
except ValueError:
    print('except divide by zero')
