import requests
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server

url = 'https://script.google.com/macros/s/AKfycbyOkfwcFBXQ7m5JeupNVhLs8doQLwaegYKnpiWkTctrSjsloVUOjPQHx4SJB6U3HyYI/exec'


def get_trip_data() -> dict:
    response = requests.get(url, timeout=5)
    data = response.json()
    return data


def get_trip_grouped_details(trip_data: dict) -> dict:
    result = {}
    result['money'] = 0
    result['dishes'] = []
    result['men_count'] = 0
    for person in trip_data['trip']:
        result['money'] += person['money']
        if person['gender'] == 'Ч':
            result['men_count'] += 1

        dishes = person['dishes'].split(', ')
        result['dishes'].extend(dishes)

    result['dishes'] = set(result['dishes'])
    # our_dishes = {'Макарони', 'Ковбаса', 'Мандарини', 'Борщ'}
    # print(our_dishes)
    # print(set('jshgfjdsgfgjsdfgsdjfgjdsgfdsjgfdsgfd9sfgjdsjfgh'))
    # print(tuple('jshgfjdsgfgjsdfgsdjfgjdsgfdsjgfdsgfd9sfgjdsjfgh'))
    return result


def main():
    trip_data = get_trip_data()
    grouped_data = get_trip_grouped_details(trip_data)
    put_html('<h1>Подорож в Карпати</h1>')
    put_success(f'Грошей буде додатково {grouped_data["money"]}')
    put_error(f'Чоловіків буде {grouped_data["men_count"]}')

    dishes = grouped_data['dishes']
    put_html('<h3>Cтрави</h3>')
    for dish in dishes:
        put_warning(dish)

    run_js('setTimeout(function(){location.reload();}, 5000)')


if __name__ == '__main__':
    start_server(main, port=16000)
