import allure
import pytest

# В данном тесте мы просто пишем в шаге, что это предусловие
@allure.epic('TestOps')
@allure.feature('UI')
@allure.story('Server')
@allure.title('Предусловия в шагах теста')
def test_with_preconditions_steps():
    with allure.step('Предусловие: Главная страница сайта открывается.'):
        assert True
    with allure.step('Шаг 1: Ввести логин и пароль в соответствующие поля.'):
        assert True

# Эта функция будет фикстурой для нашей тестовой функции
@pytest.fixture
def prepare_data(request):
    # тестовая функция параметризована, чтобы передавать данные поочередно используем .param
    login, password = request.param
    print('Подготовка данных')
    # из полученных данных собираем словарь {ключ: значение}
    data = {login: password}
    with allure.step('Получены логин и пароль для теста.'):
        assert True
    # yield используется для генераторов, мы не будем заморачиваться на эту тему.
    # Для нас все просто: все что до него - предусловие, все что после него - постусловие.
    yield data # передаем данные в тест
    print('Очистка данных после теста')
    with allure.step('Логин и пароль для теста уничтожены.'):
        assert True

# немного усложним декоратор параметром indirect=True, это нужно чтобы поочередно передавать данные в фикстуру
@pytest.mark.parametrize('prepare_data', [('log1', 'pass1'), ('log2', 'pass2')], indirect=True)
@allure.epic('TestOps')
@allure.feature('UI')
@allure.story('Server')
@allure.title('Предусловия через фикстуру.')
# обратите внимание: в качестве аргумента функции передаем другую функцию-фикстуру
def test_with_yield_fixture(prepare_data):
    # login, password в текущей тестовой функции не определены, они есть только в функции-фикстуре
    # так что вытащим их в нашу тестовую функцию
    login, password = list(prepare_data.keys())[0], list(prepare_data.values())[0]
    with allure.step(f'Шаг 1: Ввести логин "{login}" и пароль "{password}" в соответствующие поля.'):
        assert True
    assert prepare_data[login] == password

# В данном тесте мы просто пишем в шаге, что это предусловие
@allure.epic('TestOps')
@allure.feature('UI')
@allure.story('Server')
@allure.title('Предусловия в поле описания')
@allure.description('Предусловия для этого теста: сайт https://demo.qatools.cloud ')
def test_with_preconditions_in_description():
    with allure.step('Посмотреть предусловия и открыть главную страницу сайта.'):
        assert True
    with allure.step('Главная страница сайта открывается.'):
        assert True
    with allure.step('Ввести логин и пароль в соответствующие поля.'):
        assert True
