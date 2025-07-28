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

@pytest.fixture
def prepare_data(request):
    login, password = request.param
    print('Подготовка данных')
    data = {login: password}

    with allure.step('Получены логин и пароль для теста.'):
        # Прикрепляем картинку предусловия
        try:
            with open('img/preconditions.jpg', 'rb') as image_file:
                allure.attach(
                    image_file.read(),
                    name='Скриншот предусловия',
                    attachment_type=allure.attachment_type.JPG
                )
        except FileNotFoundError:
            print("Предупреждение: файл 'img/preconditions.jpg' не найден.")

    yield data  # передаем данные в тест

    print('Очистка данных после теста')
    with allure.step('Логин и пароль для теста уничтожены.'):
        # Прикрепляем картинку постусловия
        try:
            with open('img/postconditions.jpg', 'rb') as image_file:
                allure.attach(
                    image_file.read(),
                    name='Скриншот постусловия',
                    attachment_type=allure.attachment_type.JPG
                )
        except FileNotFoundError:
            print("Предупреждение: файл 'img/postconditions.jpg' не найден.")

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
