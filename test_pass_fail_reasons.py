import allure
import pytest

# Этот тест всегда будет пропущен
@pytest.mark.skip(reason="This test was skipped for an important reason.")
@allure.epic('TestOps')
@allure.feature('CORE')
@allure.story('Server')
@allure.title('skip - пропуск теста.')
@allure.step('Шаг 1: Проверить что тест пропущен (skip).')
def test_skip_01():
    assert True

# Этот тест проходит успешно, хотя мы ожидаем ошибку. Тест будет падать с ошибкой
@pytest.mark.xfail(reason="Баг еще не исправлен")
@allure.epic('TestOps')
@allure.feature('CORE')
@allure.story('Server')
@allure.title('xfail - неожиданный успех.')
@allure.step('Шаг 1: Проверить что тест успешен.')
def test_pass_01():
    assert True

# Этот тест проходит успешно, хотя мы ожидаем ошибку.
# То есть неожиданный успех -> будет падать с ошибкой.
@pytest.mark.xfail(reason="Баг еще не исправлен", strict=True)
@allure.epic('TestOps')
@allure.feature('CORE')
@allure.story('Server')
@allure.title('xfail - неожиданный успех, помечен как ошибка.')
@allure.step('Шаг 1: Проверить что тест успешен.')
def test_pass_02():
    assert True

# Тест ожидаемо падает
@pytest.mark.xfail(reason="Ожидаемое падение теста. Баг еще не исправлен.")
@allure.epic('TestOps')
@allure.feature('CORE')
@allure.story('Server')
@allure.title('xfail - ожидаемое падение теста.')
@allure.step('Шаг 1: Проверить что тест упал.')
def test_fail_01():
    assert 1 == 2

# Этот тест всегда будет сломан, так как в самом тесте нарушена логика, ошибка в самом тесте
@allure.epic('TestOps')
@allure.feature('CORE')
@allure.story('Server')
@allure.title('Проверка сломанного теста.')
@allure.step('Шаг 1: Проверить что тест сломан.')
def test_broken_01():
    con = 1 /0
    assert con > 0, 'Не смогли поделить на ноль.'

