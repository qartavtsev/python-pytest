import matplotlib.pyplot as plt
import numpy as np
import io
import allure
import pytest


# в данном примере будем тестировать генерацию графиков и добавление их в шаги ТестОпс

# записываем описание теста в отдельную переменную, чтобы потом можно было добавить в нее динамическую часть
description_text = 'Этот тест проверяет построение разных графиков.'

@allure.epic('TestOps')
@allure.feature('UI')
@allure.story('Server')
@allure.description(description_text)
@allure.link('https://ru.wikipedia.org/wiki/Тригонометрические_функции', name='Тригонометрические_функции')
@allure.title('Проверка вложения сгенерированных графиков.')
@pytest.mark.parametrize('fucn_name,func_deal', [
    ('sin_x', np.sin),
    ('cos_x', np.cos)
        ])
def test_plot_generator(fucn_name,func_deal):
    # Установка описания теста с динамическими переменными
    description = f"""
        Тест проверяет построение графика {fucn_name}.
        В диапазоне от 0 до 2π.
        Ожидаемый результат: график построен.
        """
    allure.dynamic.description(description_text+
                               f'\nДалее идет динамическая часть\n{description}')

    # Динамическая ссылка
    allure.dynamic.link(f'https://yandex.ru/search/?text={fucn_name}', name='Динамическая ссылка на поиск функции: {fucn_name}')

    with allure.step('Шаг 1: Генерируем данные для оси X.'):
        x = np.linspace(0, 2 * np.pi, 100)  # генерируем значения от 0 до 2π

    with allure.step('Шаг 2: Вычисляем данные для оси Y.'):
        y = func_deal(x) # вычисляем значение функции. внутри func_deal у нас уже нужная функция sin() или cos(), берется из параметров

    with allure.step('Шаг 3: Строим график.'):
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=fucn_name, color='blue')
        plt.xlabel('Угол (радианы)')
        plt.ylabel('Значение')
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
        plt.legend()
        plt.grid(True)

    with allure.step('Шаг 4: Сохраняем график.'):
        # Сохраняем график в буфер памяти
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

    with allure.step('Шаг 5: Прикрепляем график как вложение.'):
        # Прикрепляем график как вложение в Allure
        allure.attach(
            buf.read(),
            name=f'График_{fucn_name}.png',
            attachment_type=allure.attachment_type.PNG
        )
        buf.close()

    with allure.step('Шаг 6: Закрываем график для освобождения памяти.'):
        # Закрываем график
        plt.close()

# @allure.title('Запуск одного ручного теста.')
# @allure.manual(True)
# @allure.id("431")
# def test_test_test():
#     with allure.step("Перейти в раздел тест-кейсы."):
#         pass
#     with allure.step("Найти ручной тест из таблицы."):
#         pass
#     with allure.step("Инициировать запуск теста через контекстное меню."):
#         with allure.step("Кликнуть ПКМ на названии теста в списке тестов."):
#             with allure.step("Expected Result"):
#                 with allure.step("Открылось контекстное меню."):
#                     pass
#                 with allure.step("В меню есть пункт Запустить."):
#                     pass
#     with allure.step("Кликнуть ЛКМ на пункте Запустить."):
#         with allure.step("Expected Result"):
#             with allure.step(
#                     "Открылось диалоговое окно для создания запуска. В левом верхнем углу информация что хотим запустить 1 ручной тест, см. скрин."):
#                 pass
#     with allure.step("Нажать кнопку Отправить"):
#         with allure.step("Expected Result"):
#             with allure.step("В правом нижнем углу появилось всплывающее сообщение о создании запуска."):
#                 pass
#     with allure.step("Перейти в раздел Запуски."):
#         pass
#     with allure.step("Найти в списке запусков только что созданный запуск."):
#         pass
