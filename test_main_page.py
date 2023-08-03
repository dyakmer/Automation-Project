from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def go_to_login_page(browser): #переход на страницу входа в систему
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser): #тестовый гость переходит на страницу входа в систему
    browser.get(link)
    go_to_login_page(browser)
