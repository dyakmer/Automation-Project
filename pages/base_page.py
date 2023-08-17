class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_display_success_message_with_text(self, expected_text):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert expected_text in success_message.text, f"{expected_text} is not present in success message"

    def should_display_info_message_with_text(self, expected_text):
        info_message = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE)
        assert expected_text in info_message.text, f"{expected_text} is not present in info message"