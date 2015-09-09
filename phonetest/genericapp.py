from appium.webdriver.common.touch_action import TouchAction
from phonetest.exception import LocatorException
from phonetest.logcat import with_logcat_check


class GenericApp(object):

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.elements = config.get('elements', {})

    @with_logcat_check
    def tap(self, element_name):
        self.get_element(element_name).click()

    @with_logcat_check
    def longtap(self, element_name):
        TouchAction(self.driver).long_press(self.get_element(element_name)).release().perform()

    def get_element(self, element_name):
        element_desc = self.elements.get(element_name)
        if not element_desc:
            raise LocatorException('Element not found - {0}'.format(element_name))
        element_id = element_desc.get('id')
        if element_id:
            return self.driver.find_element_by_id(element_id)
        element_xpath = element_desc.get('xpath')
        if element_xpath:
            return self.driver.find_element_by_xpath(element_xpath)
        raise LocatorException('Unknown locator - {0}'.format(str(element_desc)))
