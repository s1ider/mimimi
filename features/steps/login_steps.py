from support.pages import HomePage
from support.ui import *


@given("I am on '{page}' page")
def step(context, page):
    page_cls = globals()[page + 'Page']
    page = page_cls(context)
    page.open()


#--- when ---
@when("Enter text '{value}' in textedit with label '{label}'")
def step(context, value, label):
    Textedit(context, label).set_text(value)


@when("Fill form")
def step(context):
    for row in context.table:
        Textedit(context, row['label']).set_text(row['value'])


@when("Click on {obj_type} '{obj_name}'")
def step(context, obj_type, obj_name):
    obj = globals()[obj_type.capitalize()]
    obj(context, obj_name).click()


#--- then ---
@then("Text '{text}' should be displayed")
def step(context, text):
    assert Text(context, text).is_displayed()

