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


@allure.id("540")
@allure.tag("Auth", "login", "UI")
@allure.title("Авторизация по логину в верхнем регистре и паролю(клон)")
@allure.label("owner", "Alex")
@allure.epic("User Auth")
def test_method():
    sharedStep144()
    with allure.step("Ввести логин из таблицы параметров в соответствующее поле. Все символы логина должны быть в верхнем регистре."):
        pass
    with allure.step("Ввести пароль из таблицы параметров в соответствующее поле."):
        pass
    with allure.step("Нажать Продолжить."):
        pass
    with allure.step("Проверить под каким пользователем произошла авторизация, кликнув левой кнопкой мыши на аватарку пользователя в правом верхнем углу."):
        pass
    with allure.step("Перейти в раздел Все проекты кликнув по нему левой кнопкой мыши."):
        pass
    with allure.step("Attachment [150]"):
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
