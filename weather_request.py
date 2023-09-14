import json
from datetime import datetime
import requests

import config_


def get_request(town: str):
    params_ = {'appid': config_.KEY, 'q': town, 'units': 'metric'}
    request = requests.get(url=config_.URL, params=params_)
    result = request.json()
    return get_weather(result)


def get_weather(res):
    s = ''
    if res['cod'] != 401:
        if res['cod'] != '404':
            description = {'Clear': 'Ясно', 'Clouds': 'Пасмурно', 'Rain': 'Дождь'}
            if res["weather"][0]["main"] in description:
                s = description[res["weather"][0]["main"]]
            result = f'Температура: {res["main"]["temp"]:.1f}\xB0C\n'\
            f'Ощущается: {res["main"]["feels_like"]:.1f}\xB0C\n'\
            f'Влажность: {res["main"]["humidity"]} %\n'\
            f'Восход: {datetime.fromtimestamp(res["sys"]["sunrise"])}\n' \
            f'Закат: {datetime.fromtimestamp(res["sys"]["sunset"])}\n{s}'
        else:
            result = 'Ошибка! Нет такого города'
    else:
        result = 'Ошибка! Неправильный ключ'
    return result


if __name__ == '__main__':
    s = input('Введите город: ')
    result = get_request(s)
    print(result)
    # with open('out1.json', 'w') as f:
    #     json.dump(result, f, indent=4)