from BasePage import BasePage


class HomePage(BasePage):
    """ Represents Login page """
    def __init__(self, context):
        super(HomePage, self).__init__(context)
        self.url = context.settings['base_url']
        self.title = "World's Largest Professional Network | LinkedIn"
