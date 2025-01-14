import json
import os

import allure
import pytest
import random

# в данном примере будем тестировать динамические вложения разных типов в шаги ТестОпс

@allure.epic("TestOps")
@allure.feature("BackEnd")
@allure.story("Server")
@pytest.mark.parametrize('parametr1, parametr2', [
    ('Велосипед', 2),
    ('Машина', 4)
        ])
def test_add_dynamic_att(parametr1, parametr2):
    with allure.step('Шаг 1: Создание вложения картинки.'):
        allure.attach.file(os.path.join('img', 'logo.jpeg'), name='JPG example', attachment_type=allure.attachment_type.JPG)

    with allure.step('Шаг 2: Создание вложения HTML.'):
        allure.attach(f'<h1>Example html attachment</h1> /n <h2>У {parametr1} {parametr2} колеса.</h2>', name='HTML example', attachment_type=allure.attachment_type.HTML  )

    with allure.step('Шаг 3: Создание вложения TXT.'):
        allure.attach(f'Some text content /n У {parametr1} {parametr2} колеса.', name='TXT example', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Шаг 4: Создание вложения CSV.'):
        allure.attach(f'тип транспорта,количество колес\n{parametr1},{parametr2}', name='CSV example', attachment_type=allure.attachment_type.CSV)

    with allure.step('Шаг 5: Создание вложения JSON.'):
        allure.attach(json.dumps({'vehicle': parametr1, 'wheels': parametr2}, indent=2), name='JSON example', attachment_type=allure.attachment_type.JSON)

    with allure.step('Шаг 6: Создание вложения в виде списка ссылок ссылок.'):
        allure.attach('\n'.join(['https://qatools.ru/', 'https://demo.qatools.cloud/']), name='URI List example', attachment_type=allure.attachment_type.URI_LIST)