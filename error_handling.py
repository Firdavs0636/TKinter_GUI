# File not found
try:
    file = open('fila.txt')
    text = 'abc'
    print(text)
except FileNotFoundError:
    file = open('fila.txt', 'w')
    file.write('lorem ipsum dolor amos compas')
except TypeError as error_message:
    print(error_message)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file is closed')

# Key ERROR
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# Index ERROR
# fruit = ['banana', 'grape', 'apple', 'orange', 'mandarin', 'lemon']
# print(fruit[6])

# Type ERROR
# text = 'abc'
# print(text + 5)


