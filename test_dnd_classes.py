import allure
import pytest
import random
from dnd_classes import Person

# Создадим список типов ошибок, которые могут быть случайно выбраны
ERROR_TYPES = [AssertionError, ValueError, TypeError, KeyError]

@pytest.mark.parametrize("damage, expected", [
    (1, 9),
    (2, 8),
    (3, 7),
    (4, 8), # 4th test already failed
])
@allure.step("Шаг: тест")
def test_take_true_damage(damage, expected):
    # добавляем первый шаг, создание персонажа и проверяем что он создался
    with allure.step('Шаг1: создание персонажа'):
        alex_person = Person('Alex')
        assert alex_person.name == 'Alex'

    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Выполнение операции'):
        allure.attach(f'Создан персонаж с именем {alex_person.name} и у него {alex_person.hp} очков здоровья.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert alex_person.hp == 10

    # Добавляем шаг 3, с ожидаемым результатом
    with allure.step("Шаг 3: Выполняем действие"):
        with allure.step("Выполняем действие деление"):
            result = 10 / 2

        with allure.step("Ожидаемый результат"):
            expected_result = 5
            assert result == expected_result, f"Ожидали: {expected_result}, получили: {result}"

    # Вставляем случайную ошибку, это приведет к сломанному тесту
    if random.random() < 0.2:  # 20% шанс на ошибку
        error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
        raise error_type(f"Случайная ошибка: {error_type.__name__}")

    else:
        alex_person.take_true_damage(damage)
        assert alex_person.hp == expected, f"Ожидалось {expected}, но получено {alex_person.hp}"