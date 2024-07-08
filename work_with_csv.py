import csv


# 1
with open('data.csv', mode='r', encoding='utf-8') as file:
    data = file.read()
    data = data.split('\n')
    for row in data:
        maybe_age = row.split(',')[2]
        is_age = maybe_age.isdigit()
        if is_age:
            age_numeric = int(maybe_age)
            print(age_numeric * 88)

# 2
with open('data.csv', mode='r', encoding='utf-8') as file:
    # reader = csv.DictReader(file, delimiter=',')
    reader = csv.reader(file, delimiter=',')

    # print(reader)
    for row in reader:
        print(row)
