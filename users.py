import requests

url = 'https://dummyjson.com/users'


def get_users() -> list[dict]:
    params = {'limit': 208}
    response = requests.get(url=url, params=params)
    response_json = response.json()
    users = response_json['users']
    return users


def get_users_data_from_city(
        users: list[dict],
        city: str,
) -> list:
    result = []
    for user in users:
        if user["address"].get("city") == city:
            first_name = user['firstName']
            last_name = user['lastName']
            result.append(f'{first_name} {last_name}')
    return result


def main():
    users = get_users()
    users_in_city = get_users_data_from_city(users=users, city='Phoenix')
    print(users_in_city)


if __name__ == "__main__":
    main()
