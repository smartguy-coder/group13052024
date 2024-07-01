list_of_recipients = [
    'test_hillel_api_mailing@ukr.net',
    'aaaa@ukr.net',
]

# result = ''
# for email in list_of_recipients:
#     result += f' {email},'
#
#
# result= result.strip(', ')
#
# print(result)


result = ', '.join(list_of_recipients)


print(result)