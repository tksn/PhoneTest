from behave import *
from phonetest.exception import LogcatException

use_step_matcher("re")


@given("PhoneProbe is activated")
def step_impl(context):
    context.testprobe = context.phone.etc.get('TestProbe')
    assert context.testprobe


@when("I tap crash button")
def step_impl(context):
    context.exception_raised = True
    try:
        context.testprobe.tap('crash')
        context.exception_raised = False
    except LogcatException:
        pass


@then("logcat raises exception")
def step_impl(context):
    assert context.exception_raised
