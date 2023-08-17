from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # Открываем страницу товара с параметром "?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    # Получаем название товара и цену
    product_title = product_page.get_product_title()
    product_price = product_page.get_product_price()

    # Добавляем товар в корзину и решаем математическое выражение
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    # Проверяем сообщение о добавлении в корзину и стоимость корзины
    product_page.should_display_success_message_with_product_name(product_title)
    product_page.should_display_basket_total_with_product_price(product_price)
