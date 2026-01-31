from selene import have



# Открываем браузер
def test_practice_form(driver):
    browser = driver

    browser.open('https://demoqa.com/automation-practice-form')

    # Убираем банеры
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    # Заполняем обязательные поля
    browser.element('#firstName').type('Filipp')
    browser.element('#lastName').type('Smirnov')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8923275899')

    # Нажимаем кнопку submit
    browser.element('#submit').click()

    # Проверяем текст модального окна
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверяем заполнение полей
    browser.element('.modal-body table tbody').all('tr').should(
        have.exact_texts(
            'Student Name Filipp Smirnov',
            'Student Email',
            'Gender Male',
            'Mobile 8923275899',
            'Date of Birth 31 January,2026',
            'Subjects',
            'Hobbies',
            'Picture',
            'Address',
            'State and City'
        )
    )