import json
import os

import allure
import pytest
import random

# в данном примере будем тестировать динамические вложения разных типов в шаги ТестОпс

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description('Этот тест проверяет корректность возможности предоставления информации о количество колес транспортного средства пользователю.')
@pytest.mark.parametrize('parametr1, parametr2', [
    ('Car', 4),
    ('Bike', 2)
        ])
def test_add_dynamic_att(parametr1, parametr2):
    with allure.step('Шаг 1: Создание вложения картинки.'):
        allure.attach.file(os.path.join('img', 'logo.jpeg'), name='JPG_example.jpg', attachment_type=allure.attachment_type.JPG)

    with allure.step('Шаг 2: Создание вложения HTML.'):
        allure.attach(f'<h1>The {parametr1} has {parametr2} wheels.</h1>', name='HTML_example.html', attachment_type=allure.attachment_type.HTML  )

    with allure.step('Шаг 3: Создание вложения TXT.'):
        allure.attach(f'The {parametr1} has {parametr2} wheels.', name='TXT_example.txt', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Шаг 4: Создание вложения CSV.'):
        allure.attach(f'vehicle type,wheels count\n{parametr1},{parametr2}', name='CSV_example.csv', attachment_type=allure.attachment_type.CSV)

    with allure.step('Шаг 5: Создание вложения JSON.'):
        allure.attach(json.dumps({'vehicle': parametr1, 'wheels': parametr2}, indent=2), name='JSON_example.json', attachment_type=allure.attachment_type.JSON)

    with allure.step('Шаг 6: Создание вложения в виде списка ссылок ссылок.'):
        allure.attach('\n'.join(['https://qatools.ru/', 'https://demo.qatools.cloud/']), name='URL_List_example', attachment_type=allure.attachment_type.URI_LIST)