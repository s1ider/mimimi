from BaseElement import BaseElement


class Text(BaseElement):
    def __init__(self, context, text):
        locator = '//strong[contains(., "{0}")]'.format(text)
        super(Text, self).__init__(context, locator)
