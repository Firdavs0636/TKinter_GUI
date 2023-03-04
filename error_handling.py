# File not found
# try:
#     file = open('fila.txt')
#     text = 'abc'
#     print(text)
# except FileNotFoundError:
#     file = open('fila.txt', 'w')
#     file.write('lorem ipsum dolor amos compas')
# except TypeError as error_message:
#     print(error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     s = ('smth')
#     raise PermissionError(s)

# Key ERROR
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# Index ERROR
# fruit = ['banana', 'grape', 'apple', 'orange', 'mandarin', 'lemon']
# print(fruit[6])

# Type ERROR
# text = 'abc'
# print(text + 5)


height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise TypeError('Human HEIGHT is not more than 3 meters!')

bmi = weight / (height ** 2)
print(bmi)


