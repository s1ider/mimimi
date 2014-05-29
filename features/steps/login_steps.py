from support.pages import HomePage


@given("I am on 'Home' page")
def step(context):
    HomePage(context).open()
