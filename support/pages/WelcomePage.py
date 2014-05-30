from BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import support.ui as ui


class WelcomePage(BasePage):
    """ Represents Login page """
    def __init__(self, context):
        super(WelcomePage, self).__init__(context)
        self.url = context.settings['base_url']
        self.title = "Welcome! | LinkedIn"

    def is_logged_in(self):
        loc = "//li[contains(@class, 'account-settings-tab')]"
        try:
            return ui.BaseElement(self.context, loc).element().is_displayed()
        except NoSuchElementException:
            return False

