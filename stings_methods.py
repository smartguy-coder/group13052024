from constants import MSG_INPUT_LAST_NAME, MSG_INPUT_FIRST_NAME
from text_templates import WELCOME_TEMPLATE

user_first_name = input(MSG_INPUT_FIRST_NAME).title().strip()
# user_first_name = user_first_name.title()
# user_first_name = user_first_name.strip()
user_last_name = input(MSG_INPUT_LAST_NAME).title().strip()

# welcome_text = 'Вітаю тебе, '
# mark = '!'
# max two pluses
# result = welcome_text + user_first_name + ' ' + user_last_name + mark

# result = WELCOME_TEMPLATE.format(first_name=user_first_name, last_name=user_last_name)

result = f'Вітаю тебе, {user_first_name} {user_last_name}!'
print(result)


print('  Hhhh lkjkuhh'.lower())
print('ßßßßßßßßßß'.lower())
print('ßßßßßßßßßß'.upper())
print('  Hhhh lkjkuhh'.upper())
print('  Hhhh lkjkuhh'.lower().count('hh'))

head = '*8' * 40
print(head)
