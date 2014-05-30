from selenium import webdriver
from yaml import load


def before_all(context):
    # setup webdriver
    context.browser = webdriver.Firefox()

    # read config
    settings_file = open('settings.yml').read()
    context.settings = load(settings_file)

    # default timeout
    timeout = context.settings['timeout']
    context.browser.implicitly_wait(timeout)


def after_all(context):
    pass
    # context.browser.quit()


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        filename = "{0}.png".format(scenario.name)
        context.browser.save_screenshot(filename)
