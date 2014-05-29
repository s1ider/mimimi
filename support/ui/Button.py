from BaseElement import BaseElement


class Button(BaseElement):
    """ Represents all buttons """
    def __init__(self, context, name):
        self.name = name
        locator = '//input[@type="submit" and @value="{0}"]'.format(name)
        super(Button, self).__init__(context, locator)
