import allure
import pytest


@allure.id("2847")
@allure.title("Корректность расчёта скидки на товар")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Акции")
def test_method_1():
    with allure.step("Найдите товар со скидкой"):
        with allure.step("Expected Result"):
            with allure.step("На карточке товара отображается метка скидки (например, «-20%»)"):
                pass
            with allure.step("Старая цена отображается зачёркнутой, новая — выделена цветом"):
                pass
    with allure.step("Проверьте арифметику расчёта скидки"):
        with allure.step("Expected Result"):
            with allure.step("Новая цена соответствует формуле: новая = старая × (1 - скидка/100)"):
                pass
            with allure.step("Разница в цене не превышает округление в пределах 1 рубля"):
                pass
    with allure.step("Откройте карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Процент и итоговая цена совпадают с данными в каталоге"):
                pass
            with allure.step("Никаких расхождений между каталогом и карточкой нет"):
                pass

@allure.id("2834")
@allure.tag("regress")
@allure.title("Переход по категориям каталога")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Навигация")
def test_method_2():
    with allure.step("На странице каталога выберите категорию (например, «Одежда»)"):
        with allure.step("Expected Result"):
            with allure.step("Отображается список товаров выбранной категории"):
                pass
            with allure.step("Заголовок страницы соответствует названию категории"):
                pass
    with allure.step("Перейдите в другую категорию (например, «Обувь»)"):
        with allure.step("Expected Result"):
            with allure.step("Список товаров обновляется, отображая только товары из новой категории"):
                pass
            with allure.step("URL меняется в соответствии с категорией (например, /catalog/shoes)"):
                pass
            with allure.step("Ошибок загрузки не возникает"):
                pass

@allure.id("2844")
@allure.title("Сортировка товаров по популярности")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Сортировка")
def test_method_3():
    with allure.step("Выберите сортировку «По популярности»"):
        with allure.step("Expected Result"):
            with allure.step("Товары сортируются в порядке убывания рейтинга или количества покупок"):
                pass
            with allure.step("Порядок не нарушается при прокрутке или смене страницы"):
                pass
    with allure.step("Обновите страницу"):
        with allure.step("Expected Result"):
            with allure.step("Порядок сортировки сохраняется (если предусмотрено системой)"):
                pass
            with allure.step("Отображаемые значения рейтинга корректны и соответствуют данным в базе"):
                pass

@allure.id("2840")
@allure.title("Применение нескольких фильтров одновременно")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Фильтрация")
def test_method_4():
    with allure.step("Выберите в фильтре «Бренд» — «Brand A»"):
        with allure.step("Expected Result"):
            with allure.step("Бренд отмечен как выбранный"):
                pass
    with allure.step("Установите диапазон «Цена» от 1000 до 3000"):
        with allure.step("Expected Result"):
            with allure.step("В полях/ползунках отображается выбранный диапазон"):
                pass
    with allure.step("Включите фильтр «В наличии»"):
        with allure.step("Expected Result"):
            with allure.step("Переключатель/чекбокс активен"):
                pass
    with allure.step("Нажмите «Применить»"):
        with allure.step("Expected Result"):
            with allure.step("Список товаров показывает результаты, соответствующие всем трём условиям"):
                pass
            with allure.step("Отображаются чипы/индикаторы всех применённых фильтров"):
                pass
            with allure.step("Если результатов нет — отображается понятное сообщение «Нет товаров по заданным параметрам»"):
                pass

@allure.id("2820")
@allure.tag("regress", "smoke")
@allure.title("Просмотр детальной информации по заказу")
@allure.label("owner", "Дмитрий")
@allure.feature("Личный кабинет")
@allure.story("История заказов и детализация")
def test_method_5():
    with allure.step("Перейдите в раздел «Мои заказы»"):
        with allure.step("Expected Result"):
            with allure.step("Отображается список заказов"):
                pass
    with allure.step("Нажмите на номер заказа или кнопку «Подробнее»"):
        with allure.step("Expected Result"):
            with allure.step("Открывается страница/всплывающее окно с деталями заказа"):
                pass
            with allure.step("Отображаются: список товаров, количество, сумма, способ оплаты, адрес доставки и статус"):
                pass
    with allure.step("Проверьте корректность отображения информации"):
        with allure.step("Expected Result"):
            with allure.step("Все данные совпадают с информацией, указанной при оформлении заказа"):
                pass

@allure.id("2811")
@allure.tag("regress", "smoke")
@allure.title("Успешное изменение данных профиля")
@allure.label("owner", "Дмитрий")
@allure.feature("Личный кабинет")
@allure.story("Просмотр и редактирование профиля")
def test_method_6():
    with allure.step("Перейдите на страницу «Профиль»"):
        with allure.step("Expected Result"):
            with allure.step("Данные профиля загружены"):
                pass
    with allure.step("Нажмите кнопку «Редактировать»"):
        with allure.step("Expected Result"):
            with allure.step("Поля становятся доступными для редактирования"):
                pass
    with allure.step("Измените одно или несколько полей (например, имя или номер телефона)"):
        with allure.step("Expected Result"):
            with allure.step("Измененные данные отображаются в полях"):
                pass
    with allure.step("Нажмите «Сохранить изменения»"):
        with allure.step("Expected Result"):
            with allure.step("Появляется сообщение «Изменения сохранены»"):
                pass
            with allure.step("Новые данные сохраняются в профиле и отображаются после обновления страницы"):
                pass

@allure.id("2816")
@allure.tag("regress")
@allure.title("Удаление существующего адреса доставки")
@allure.label("owner", "Дмитрий")
@allure.feature("Личный кабинет")
@allure.story("Управление адресами доставки")
def test_method_7():
    with allure.step("Перейдите в раздел «Мои адреса»"):
        with allure.step("Expected Result"):
            with allure.step("Отображается список адресов с кнопкой «Удалить» у каждого"):
                pass
    with allure.step("Нажмите кнопку «Удалить» рядом с нужным адресом"):
        with allure.step("Expected Result"):
            with allure.step("Появляется всплывающее окно подтверждения удаления"):
                pass
    with allure.step("Подтвердите удаление"):
        with allure.step("Expected Result"):
            with allure.step("Адрес удалён из списка"):
                pass
            with allure.step("Отображается сообщение «Адрес успешно удалён»"):
                pass
            with allure.step("Список адресов обновлён"):
                pass

@allure.id("2803")
@allure.title("Авторизация с неверным паролем")
@allure.label("owner", "Анна")
@allure.feature("Регистрация и авторизация")
@allure.story("Авторизация")
def test_method_8():
    with allure.step("Откройте страницу входа интернет-магазина"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются поля «Email», «Пароль» и кнопка «Войти»"):
                pass
    with allure.step("Введите корректный адрес почты существующего пользователя в поле «Email»"):
        with allure.step("Expected Result"):
            with allure.step("Email корректно отображается в поле"):
                pass
    with allure.step("Введите неверный пароль в поле «Пароль»"):
        with allure.step("Expected Result"):
            with allure.step("Пароль введен и скрыт точками"):
                pass
    with allure.step("Нажмите «Войти»"):
        with allure.step("Expected Result"):
            with allure.step("Запрос аутентификации отклонен"):
                pass
            with allure.step("Отображается сообщение об ошибке, например: «Неверный логин или пароль»"):
                pass
            with allure.step("Сессия не создается, пользователь остается на странице входа"):
                pass

@allure.id("2807")
@allure.title("Валидация формата email при восстановлении пароля")
@allure.label("owner", "Анна")
@allure.feature("Регистрация и авторизация")
@allure.story("Восстановление пароля")
def test_method_9():
    with allure.step("Откройте страницу восстановления пароля («Забыли пароль?»)"):
        with allure.step("Expected Result"):
            with allure.step("Отображается поле «Email» и кнопка «Восстановить пароль»"):
                pass
    with allure.step("Введите email в неправильном формате (например, «user@», «@domain.com», «userdomain.com»)"):
        with allure.step("Expected Result"):
            with allure.step("Под полем отображается сообщение валидации, например: «Некорректный формат email»"):
                pass
            with allure.step("Кнопка «Восстановить пароль» не активна или запрос не отправляется"):
                pass
    with allure.step("Исправьте адрес на корректный формат"):
        with allure.step("Expected Result"):
            with allure.step("Сообщение валидации исчезает; кнопка «Восстановить пароль» становится активной"):
                pass

@allure.id("2799")
@allure.tag("regress")
@allure.title("Валидация обязательных полей формы регистрации")
@allure.label("owner", "Анна")
@allure.feature("Регистрация и авторизация")
@allure.story("Регистрация")
def test_method_10():
    with allure.step("Откройте страницу регистрации интернет-магазина"):
        with allure.step("Expected Result"):
            with allure.step("Форма регистрации отображается с обязательными полями, помеченными индикатором обязательности (например, «*»)"):
                pass
    with allure.step("Не заполняя ни одно поле, нажмите «Зарегистрироваться»"):
        with allure.step("Expected Result"):
            with allure.step("Появляются сообщения валидации под обязательными полями («Поле обязательно для заполнения»)"):
                pass
            with allure.step("Запрос на создание учетной записи не отправляется; пользователь остается на странице регистрации"):
                pass
    with allure.step("Последовательно заполняйте по одному полю и нажимайте «Зарегистрироваться»"):
        with allure.step("Expected Result"):
            with allure.step("Сообщения валидации исчезают для заполненных полей"):
                pass
            with allure.step("Сообщение валидации сохраняется для первого незаполненного обязательного поля"):
                pass
    with allure.step("Заполните все обязательные поля корректными значениями"):
        with allure.step("Expected Result"):
            with allure.step("Сообщения об ошибках исчезают; кнопка «Зарегистрироваться» становится доступной"):
                pass

@allure.id("2851")
@allure.tag("regress", "smoke")
@allure.title("Отображение статуса наличия товара на складе")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Карточка товара")
def test_method_11():
    with allure.step("Откройте каталог товаров"):
        with allure.step("Expected Result"):
            with allure.step("На карточке каждого товара отображается статус наличия"):
                pass
            with allure.step("Цветовое обозначение соответствует статусу (зелёный — в наличии, серый — нет)"):
                pass
    with allure.step("Перейдите в карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Статус отображается под ценой или в блоке характеристик"):
                pass
            with allure.step("Формулировка статуса совпадает с данными склада"):
                pass
    with allure.step("Для товаров «Нет в наличии» проверьте поведение кнопки «Добавить в корзину»"):
        with allure.step("Expected Result"):
            with allure.step("Кнопка неактивна или заменена на «Сообщить о поступлении»"):
                pass

@allure.id("2858")
@allure.tag("regress")
@allure.title("Добавление отзыва авторизованным пользователем")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Отзывы")
def test_method_12():
    with allure.step("step 1] Откройте карточку товара, для которого хотите оставить отзыв"):
        with allure.step("Expected Result"):
            with allure.step("Отображается форма «Оставить отзыв» с полями «Оценка», «Комментарий» и кнопкой «Отправить»"):
                pass
    with allure.step("Выберите оценку (например, 5 звёзд) и введите текст отзыва"):
        with allure.step("Expected Result"):
            with allure.step("Поля заполнены корректно; кнопка «Отправить» становится активной"):
                pass
    with allure.step("Нажмите кнопку «Отправить»"):
        with allure.step("Expected Result"):
            with allure.step("Отображается сообщение «Спасибо за ваш отзыв»"):
                pass
            with allure.step("Новый отзыв появляется в списке отзывов с указанием автора, даты и текста"):
                pass
            with allure.step("Средний рейтинг обновляется с учётом нового отзыва (если реализовано)"):
                pass

@allure.id("2855")
@allure.title("Возможность поставить оценку авторизованным пользователем")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Рейтинг")
def test_method_13():
    with allure.step("Авторизуйтесь и откройте карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Блок выставления оценки доступен (звёзды, ползунок, кнопки)"):
                pass
    with allure.step("Поставьте оценку (например, 5 звёзд)"):
        with allure.step("Expected Result"):
            with allure.step("Выбранная оценка подсвечивается"):
                pass
            with allure.step("Появляется сообщение «Спасибо за вашу оценку»"):
                pass
    with allure.step("Обновите страницу"):
        with allure.step("Expected Result"):
            with allure.step("Средний рейтинг обновился с учётом новой оценки"):
                pass
            with allure.step("Повторная оценка недоступна или заменяет предыдущую (в зависимости от логики)"):
                pass

@allure.id("2824")
@allure.tag("regress")
@allure.title("Отправка письма при смене пароля")
@allure.label("owner", "Дмитрий")
@allure.feature("Уведомления")
@allure.story("Email-уведомления")
def test_method_14():
    with allure.step("Выполните смену пароля в разделе «Безопасность»/«Профиль» (старый → новый пароль)"):
        with allure.step("Expected Result"):
            with allure.step("Отображается сообщение «Пароль успешно изменён»"):
                pass
    with allure.step("Откройте почтовый ящик пользователя"):
        with allure.step("Expected Result"):
            with allure.step("Получено новое письмо «Смена пароля» от адреса магазина"):
                pass
    with allure.step("Проверьте тему/отправителя/время доставки"):
        with allure.step("Expected Result"):
            with allure.step("Тема отражает событие, отправитель корректен, время близко ко времени операции"):
                pass
    with allure.step("Откройте письмо"):
        with allure.step("Expected Result"):
            with allure.step("Письмо содержит уведомление о смене пароля и рекомендации (если не вы — обратитесь в поддержку/сбросьте пароль)"):
                pass
            with allure.step("Конфиденциальные данные (полный пароль) не раскрываются"):
                pass

@allure.id("2832")
@allure.title("Сохранение настроек уведомлений после выхода из аккаунта")
@allure.label("owner", "Дмитрий")
@allure.feature("Уведомления")
@allure.story("Настройки уведомлений")
def test_method_15():
    with allure.step("Перейдите в раздел «Настройки уведомлений»"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются текущие значения переключателей уведомлений"):
                pass
    with allure.step("Измените настройки (например, отключите все уведомления о заказах)"):
        with allure.step("Expected Result"):
            with allure.step("Появляется сообщение «Настройки сохранены»"):
                pass
    with allure.step("Выйдите из аккаунта"):
        with allure.step("Expected Result"):
            with allure.step("Сессия завершается, пользователь перенаправлен на страницу входа"):
                pass
    with allure.step("Войдите снова и откройте раздел «Настройки уведомлений»"):
        with allure.step("Expected Result"):
            with allure.step("Ранее изменённые настройки сохранены"):
                pass
            with allure.step("Переключатели отображают актуальные значения, соответствующие последнему состоянию"):
                pass

@allure.id("2828")
@allure.tag("regress", "smoke")
@allure.title("Отображение системного уведомления об ошибке")
@allure.label("owner", "Дмитрий")
@allure.feature("Уведомления")
@allure.story("Системные уведомления")
def test_method_16():
    with allure.step("Введите неверные данные при авторизации и нажмите «Войти»"):
        with allure.step("Expected Result"):
            with allure.step("Появляется уведомление об ошибке (toast, баннер, модальное окно)"):
                pass
            with allure.step("Текст информативен, например: «Неверный логин или пароль»"):
                pass
            with allure.step("Цветовая схема и иконка соответствуют статусу ошибки (например, красный крест)"):
                pass
    with allure.step("Повторите действие для другого типа ошибки (например, потеря связи с сервером)"):
        with allure.step("Expected Result"):
            with allure.step("Уведомление отображает корректный текст системной ошибки («Ошибка соединения», «Попробуйте позже»)"):
                pass
            with allure.step("Предыдущее уведомление скрывается, если показ нового уведомления не допускает дублирования"):
                pass
