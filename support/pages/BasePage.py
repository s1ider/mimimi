class BasePage(object):
    """ Base page for all PageObjects"""
    def __init__(self, context):
        self.url = None
        self.title = None

        self.context = context
        self.browser = context.browser

    def open(self):
        self.browser.get(self.url)

    def is_displayed(self):
        return self.title in self.browser.title
