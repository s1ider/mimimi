from BaseElement import BaseElement


class Textedit(BaseElement):
    """ Represents text fields with label"""
    def __init__(self, context, label):
        locator = ('//label[contains(text(), "{0}")]/'
                   'following-sibling::div/input'.format(label))
        super(Textedit, self).__init__(context, locator)
