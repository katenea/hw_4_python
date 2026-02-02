import os
from selene import have


# Открываем браузер
def test_practice_form(driver):
    browser = driver

    browser.open('/automation-practice-form')

    # Убираем банеры
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    # Имя и фамилия
    browser.element('#firstName').type('Filipp')
    browser.element('#lastName').type('Smirnov')

    # Почта
    browser.element('#userEmail').type('example@mail.ru')

    # Гендер
    browser.element('[for="gender-radio-1"]').click()

    # Номер телефона
    browser.element('#userNumber').type('8923275899')

    # Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('//option[@value="1"]').click()
    browser.element('//option[@value="2000"]').click()
    browser.element('[aria-label="Choose Wednesday, February 9th, 2000"]').click()

    # Предметы
    browser.element('#subjectsInput').type('English').press_enter()

    # Хобби
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Загружаем картинку
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))

    # Адрес
    browser.element('#currentAddress').type('Kaliningrad, Gorkogo, 98')

    # State & City
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    # Нажимаем кнопку submit
    browser.element('#submit').click()

    # Проверяем текст модального окна
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверяем заполнение полей
    browser.element('.modal-body table tbody').all('tr').should(
        have.exact_texts(
            'Student Name Filipp Smirnov',
            'Student Email example@mail.ru',
            'Gender Male',
            'Mobile 8923275899',
            'Date of Birth 09 February,2000',
            'Subjects English',
            'Hobbies Music',
            'Picture photo.jpg',
            'Address Kaliningrad, Gorkogo, 98',
            'State and City Uttar Pradesh Agra'
        )
    )