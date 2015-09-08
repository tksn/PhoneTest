from appium.webdriver.common.touch_action import TouchAction
from phonetest.logcat import with_logcat_check

class PhoneDialer(object):

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.elements = config.get('elements', {})

    @with_logcat_check
    def tap(self, element_name):
        if element_name in self.elements:
            self.driver.find_element_by_id(self.elements[element_name]).click()

    @with_logcat_check
    def longtap(self, element_name):
        if element_name in self.elements:
            TouchAction(self.driver)\
                .long_press(self.driver.find_element_by_id(self.elements[element_name]))\
                .release().perform()

    def dial(self, numbers):
        self.longtap('backspace')
        for digit in numbers:
            self.tap(digit)
        self.tap('call')
