import allure
import pytest

# в данном тесте проверим добавление разных описаний и предусловий к тестам в ТестОпс

# записываем описания и предусловия в отдельные переменные, чтобы потом можно было добавить динамические части
description_text = 'Этот тест проверяет корректность добавления описания в виде текста.'
description_html = '''
    Тест проверяет описание с разметкой <b>HTML</b>\n
    <h2>Сценарий:</h2>
    <ul>
    <li>Не нумерованный список, пункт 1</li>
    </ul>
        '''
preconditions = 'demo'

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.label('preconditions_info', preconditions)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_description_text_01():
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.label('preconditions_info', preconditions)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста. Есть ли динамическая часть описания.')
def test_description_text_with_dynamic_01():
    dymanic_description_text = 'Это динамическая часть описания, она меняется от теста к тесту.\nТекст из теста 01.'
    allure.dynamic.description(description_text + f'\n{dymanic_description_text}')
    dymanic_preconditions_text = 'dynamic'
    allure.dynamic.label("preconditions_info", preconditions +'_'+ f'{dymanic_preconditions_text}')
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.label('preconditions_info', preconditions)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_description_text_02():
    '''
    Это описание теста сделано без использования декоратора.
    Описание взято из закомментированных строк кода.
    Не нумерованный список:
     - шаг 1
     - шаг 2
    '''
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.label('preconditions_info', preconditions)
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста. Есть ли динамическая часть описания.')
def test_description_text_with_dynamic_02():
    '''
    Это описание теста сделано без использования декоратора.
    Описание взято из закомментированных строк кода.
    Не нумерованный список:
     - шаг 1
     - шаг 2
    '''
    dymanic_description_text = 'Это динамическая часть описания, она меняется от теста к тесту.\nТекст из теста 02.'
    allure.dynamic.description(test_description_text_with_dynamic_02.__doc__ + f'\n{dymanic_description_text}')

    dymanic_preconditions_text = 'dynamic'
    allure.dynamic.label("preconditions_info", preconditions +'_'+ f'{dymanic_preconditions_text}')
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description_html(description_html)
@allure.label('preconditions_info', preconditions)
@allure.step('Шаг 1: Проверить есть ли описание в виде HTML у теста.')
def test_description_html_01():
    assert True



@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description_html(description_html)
@allure.label('CheckType', 'last')
@allure.step('Шаг 1: Проверить есть ли поле CheckType с параметром last.')
def test_сhecktype():
    assert True