from selenium.common.exceptions import NoSuchElementException


class BaseElement(object):
    """ Base element class """
    def __init__(self, context, locator):
        self.locator = locator
        self.context = context
        self.browser = context.browser

    def element(self):
        return self.browser.find_element_by_xpath(self.locator)

    def get_text(self):
        return self.element().text

    def set_text(self, value):
        self.element().clear()
        self.element().send_keys(value)

    def click(self):
        self.element().click()

    def is_displayed(self):
        try:
            return self.element.is_displayed()
        except NoSuchElementException:
            return False
