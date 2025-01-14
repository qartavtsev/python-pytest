import allure
import pytest

# в данном тесте проверим добавление разных описаний и предусловий к тестам в ТестОпс

# записываем описание теста в отдельную переменную, чтобы потом можно было добавить в нее динамическую часть
description_text = 'Этот тест проверяет корректность добавления описания в виде текста.'
description_html = '''
    Тест проверяет описание с разметкой <b>HTML</b>/n
    <h2>Сценарий:</h2>
    <ul>
    <li>Не нумерованный список, пункт 1</li>
    </ul>
        '''
@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_add_description_text_01():
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_add_description_text_with_dynamic_01():
    dymanic_text = 'Это динамическая часть описания, она меняеться от теста к тесту.\nТекст из теста 02.'
    allure.dynamic.description(description_text + f'\n{dymanic_text}')
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_add_description_text_02():
    '''
    Это описание теста сделано без использования декоратора.
    Описание взято из закомментированных строк кода.
    "Не нумерованный список:
     - шаг 1
     - шаг 2
    '''
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_add_description_text_with_dynamic_02():
    '''
    Это описание теста сделано без использования декоратора.
    Описание взято из закомментированных строк кода.
    "Не нумерованный список:
     - шаг 1
     - шаг 2
    '''
    dymanic_text = 'Это динамическая часть описания, она меняеться от теста к тесту.\nТекст из теста 02.'
    allure.dynamic.description(test_add_description_text_with_dynamic_02.__doc__ + f'\n{dymanic_text}')
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description_html(description_html)
@allure.step('Шаг 1: Проверить есть ли описание в виде HTML у теста.')
def test_add_description_html_01():
    assert True