from selenium.webdriver.common.by import By


def test_find_card_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    text_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert isinstance(text_button, str)  # проверка assert, что в кнопке есть строка
