import allure
import pytest


@allure.title('Запуск одного ручного теста.')
@allure.manual(True)
@allure.id("431")
def test_run_one_manual_test():
    with allure.step("Перейти в раздел тест-кейсы."):
        pass
    with allure.step("Найти ручной тест из таблицы."):
        pass
    with allure.step("Инициировать запуск теста через контекстное меню."):
        with allure.step("Кликнуть ПКМ на названии теста в списке тестов."):
            with allure.step("Expected Result"):
                with allure.step("Открылось контекстное меню."):
                    pass
                with allure.step("В меню есть пункт Запустить."):
                    pass
    with allure.step("Кликнуть ЛКМ на пункте Запустить."):
        with allure.step("Expected Result"):
            with allure.step(
                    "Открылось диалоговое окно для создания запуска. В левом верхнем углу информация что хотим запустить 1 ручной тест, см. скрин."):
                pass
    with allure.step("Нажать кнопку Отправить"):
        with allure.step("Expected Result"):
            with allure.step("В правом нижнем углу появилось всплывающее сообщение о создании запуска."):
                pass
    with allure.step("Перейти в раздел Запуски."):
        pass
    with allure.step("Найти в списке запусков только что созданный запуск."):
        pass


@allure.id("848")
@allure.title("Проверка переключения на темную тему")
@allure.label("owner", "Alex")
def test_method():
    sharedStep144()
    with allure.step("Перейти в меню пользователя"):
        with allure.step("Expected Result"):
            with allure.step("123"):
                pass
    with allure.step("Открыть настройки оформления"):
        pass
    with allure.step("Переключить тему оформления на темную"):
        pass
    with allure.step("Убедиться что интерфейс переключился на темную тему"):
        pass


@allure.step("Зайти на портал")
def sharedStep144():
    with allure.step("Открыть новую вкладку в режиме Incognito."):
        pass
    with allure.step("Ввести в адресную строку адрес портала. Нажать Enter."):
        with allure.step("Expected Result"):
            with allure.step("Открылась страница авторизации на портале"):
                pass
            with allure.step("Attachment [35]"):
                pass


