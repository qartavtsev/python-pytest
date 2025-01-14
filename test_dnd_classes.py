from logging import CRITICAL

import allure
import pytest
import random
from dnd_classes import Person

# в данном примере будем тестировать класс Person

# создадим список типов ошибок, которые могут быть случайно выбраны
ERROR_TYPES = [IndexError, ValueError, TypeError, KeyError]

@pytest.mark.parametrize('damage, expected', [
    (1, 9),
    (2, 8),
    (3, 7),
    (4, 8), # 4th test already failed
])
#@allure.step('Шаг: тест')
@allure.description('Этот тест проверяет базовую функциональность системы.\nВ части получения чистого урона.')
def test_take_true_damage(damage, expected):
    # добавляем первый шаг, создание персонажа и проверяем что он создался
    with allure.step('Шаг 1: Создание объекта класса персонаж с именем "Alex".'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        alex_person = Person('Alex')
        assert alex_person.name == 'Alex'

    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем количество базовых очков здоровья.'):
        allure.attach(f'Создан персонаж с именем {alex_person.name} и у него {alex_person.hp} очков здоровья.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert alex_person.hp == 10

    # Добавляем шаг 3, с ожидаемым результатом
    with allure.step('Шаг 3: Проверяем наносится ли урон объекту.'):
        with allure.step('Шаг 3.1: Наносим чистый урон.'):
            if random.random() < 0.95:  # 95% шанс нанести урон
                alex_person.take_true_damage(damage)
        with allure.step('Шаг 3.2: Проверяем действие'):
            allure.attach(f'Персонажу с именем {alex_person.name} нанесли урон {damage} и у него осталось {alex_person.hp} очков здоровья.',
                          name='Лог операции', attachment_type=allure.attachment_type.TEXT)

            assert alex_person.hp == expected, f'Crit Error: Чистый урон не прошел, не изменяются данные объекта {alex_person}.'

    with allure.step('Шаг 4: Шаг со случайной ошибкой'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')

        with allure.step('Шаг 5: проверка реальности'):
            assert alex_person.hp == expected, f'Ожидалось {expected}, но получено {alex_person.hp}'

@pytest.mark.parametrize('name, expected', [
    ('Alex', 'Alex'),
    (123, 123),
    ('Leo', 'Leo')
])
@allure.epic('TestOps')
@allure.feature('BackEnd')
@allure.story('Server')
#@allure.id('')
@allure.description('Этот тест проверяет базовую функциональность системы.\nВ части корректности имени персонажа.')
def test_naming(name, expected):
    # добавляем первый шаг, создание персонажа и проверяем что он создался
    with allure.step('Шаг 1: Создание персонажа с корректным именем.'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс_Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        alex_person = Person(name)

    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем корректность имени.'):
        allure.attach(f'Создан объект {alex_person}.', name='Лог_операции.txt', attachment_type=allure.attachment_type.TEXT)
        assert alex_person.name == expected, f'Name Error: Неверное имя объекта {alex_person}.'

    # Добавляем шаг 3, проверяем тип данных в имени
    with allure.step('Шаг 3: Имя должно быть строкой.'):
        with allure.step('Шаг 3.1: Проверяем тип данных'):
            result = type(alex_person.name)
            assert result == str, f'Name Error: Имя должно быть строкой. Ожидали: str, получили: {result}'
        with allure.step('Шаг 3.2: Проверяем первый символ строки. Не должно бить подчеркивания или цифры.'):
            result = alex_person.name[0]
            expected_result = expected[0]
            assert result == expected_result, f'Name Error: На первом месте должна быть буква. Ожидали: не "{expected_result}", получили: "{result}"'
    with allure.step('Шаг 4: Шаг на везение. Генерация случайной ошибки.'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')

# def test_add_some_reasons():
#    pass