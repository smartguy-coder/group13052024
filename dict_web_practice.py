from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server

creds = {
    'password': '123',
    'login': 'admin',
}

observing_data = []

def main():
    put_html('<h1>Програма моніторингу погоди</h1>')
    login_form = input_group(
        'Enter your creds',
        [
            input_pw('Login', placeholder='Login here', name='login'),
            input_pw('Password', type=PASSWORD, placeholder='Input password here', name='password'),
        ]
    )
    # if login_form['login'] == creds['login'] and login_form['password'] == creds['password']:
    if login_form == creds:
        put_success('Welcome')
    else:
        put_warning('Go away')
        run_js('setTimeout(function(){location.reload();}, 2000)')
        return

    weather_data = input_group(
        'Enter weather params',
        [
            input_pw('temp',  name='temp', required=True),
            slider('humidity', name='humidity', max_value=100, min_value=0, required=True),
        ]
    )
    observing_data.append(weather_data)

    weather_accumulated_data = [['Temperature', 'Humidity']]
    for observation  in observing_data:
        weather_accumulated_data.append(
            [observation['temp'], observation['humidity']]
        )

    put_table(weather_accumulated_data)
    run_js('setTimeout(function(){location.reload();}, 2000)')


if __name__ == '__main__':
    start_server(main, port=16000)
