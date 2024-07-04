# my_file = open('main.py')
# print(my_file)
#
# # print(my_file.read())
# print(my_file.closed)
# 1/0
# my_file.close()
# # my_file.read()
# print(my_file.closed)

# with open('main.py') as my_file, open('numbers_theory.py') as numbers_file:
#     print(my_file.read())
#     print(numbers_file.read())

import requests


def create_log(log: str, filename: str = 'new_file.txt'):
    with open(filename, mode='a') as my_file:
        my_file.write(f'\n{log}')


create_log(log='kjhkjhk')
create_log(log='kjhkjhk')
create_log(log='kjhkjhk')
create_log(log='kjhkjhk')
create_log(log='kjhkjhk')


def read_log(filename: str = 'new_file.txt'):
    with open(filename, mode='r') as my_file:
        logs = my_file.read()
        print(logs.split())
        my_file.seek(6)
        data = my_file.readlines()
        print(data)

# read_log()


# with open('progit.pdf', mode='br') as my_file, open('new_git.pdf', mode='bw') as new_git_file:
#     content = my_file.read()
#     new_git_file.write(content)


# with open('spring.jpg', mode='bw') as my_file:
#     response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Colorful_spring_garden.jpg/2560px-Colorful_spring_garden.jpg')
#     print(response.content)
#     my_file.write(response.content)

# with open('spring.jpg', mode='ba') as my_file:
#     my_file.write(b'Vasja - the best')
#
# with open('spring.jpg', mode='br') as my_file:
#     print(my_file.read())




