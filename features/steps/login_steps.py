@given("I am on 'Home' page")
def step(context):
    url = context.settings['base_url']
    context.browser.get(url)
