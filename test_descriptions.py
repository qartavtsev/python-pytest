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

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.title('Проверка текстового описания 01.')
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста.')
def test_description_text_01():
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description(description_text)
@allure.title('Проверка текстового описания с динамической частью 01.')
@allure.step('Шаг 1: Проверить есть ли у теста описание в виде текста. Есть ли динамическая часть описания.')
def test_description_text_with_dynamic_01():
    dymanic_description_text = 'Это динамическая часть описания, она меняется от теста к тесту.\nТекст из теста 01.'
    allure.dynamic.description(description_text + f'\n{dymanic_description_text}')
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.title('Проверка текстового описания 02.')
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
@allure.title('Проверка текстового описания с динамической частью 02.')
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
    assert True

@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
@allure.description_html(description_html)
@allure.title('Проверка HTML описания.')
@allure.step('Шаг 1: Проверить есть ли описание в виде HTML у теста.')
@allure.tag('Тэг')
def test_description_html_01():
    assert True



@allure.id("467")
def test_test_21:
    with allure.step("Зайти на портал"):
        with allure.step("Открыть новую вкладку в режиме Incognito."):
            pass
    with allure.step("Ввести в адресную строку адрес портала. Нажать Enter."):
        with allure.step("Expected Result"):
            with allure.step("Открылась страница авторизации на портале"):
                pass
    with allure.step("123"):
        pass
    with allure.step(
            "Ввести логин из таблицы параметров в соответствующее поле. Все символы логина должны быть в верхнем регистре."):
        pass
    with allure.step("Ввести пароль из таблицы параметров в соответствующее поле."):
        pass
    with allure.step("Нажать Продолжить."):
        pass
    with allure.step(
            "Проверить под каким пользователем произошла авторизация, кликнув левой кнопкой мыши на аватарку пользователя в правом верхнем углу."):
        pass
    with allure.step("Перейти в раздел Все проекты кликнув по нему левой кнопкой мыши."):
        pass
    with allure.step("Просмотреть список доступных проектов."):
        with allure.step("Expected Result"):
            with allure.step("В списке доступных проектов есть соответствующий проект из таблицы параметров."):
                pass
            with allure.step("В списке доступных проектов отсутствует соответствующий проект из таблицы параметров."):
                pass
            with allure.step("В списке доступных проектов есть публичные проекты."):
                pass
    with allure.step("Перейти в соответствующий проект из таблицы параметров."):
        pass
    with allure.step("Перейти в меню настройки проекта."):
        pass
    with allure.step("Перейди в подраздел настроек доступ."):
        pass
    with allure.step("Убедится что у нужного пользователя уровень прав - владелец."):
        pass