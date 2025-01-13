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
def test_take_true_damage(damage, expected):
    with allure.step('Шаг1: создание персонажа'):
        alex_person = Person('Alex')
        assert alex_person.name == 'Alex'

    # Вставляем случайную ошибку для симуляции фолта
    if random.random() < 0.2:  # 20% шанс на ошибку
        error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
        raise error_type(f"Случайная ошибка: {error_type.__name__}")

    else:
        alex_person.take_true_damage(damage)
        assert alex_person.hp == expected, f"Ожидалось {expected}, но получено {alex_person.hp}"