import yaml
import appium
import phonetest.exception
import phonetest.logcat
import phonetest.phone_dialer

class Phone(object):

    def __init__(self, device_name, config_yml):
        phonetest.logcat.start_logcat_watcher()
        self.config = yaml.load(config_yml)
        self.open(device_name)
        self.build_app_accessor()

    def open(self, device_name):
        startup_activity_name = self.config.get('startup_activity', '')
        activities = self.config.get('activities', {})
        startup_activity = activities.get(startup_activity_name, {})

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': self.config.get('platform_version'),
            'deviceName': device_name,
            'appPackage': startup_activity.get('package'),
            'appActivity': startup_activity.get('activity')
        }
        self.driver = appium.webdriver.Remote(self.config.get('endpoint'), desired_caps)

    def close(self):
        self.driver.quit()
        self.driver = None

    def build_app_accessor(self):
        activities = self.config.get('activities', {})

        phone_dialer_conf = activities.get('PhoneDialer')
        if phone_dialer_conf:
            self.phone_dialer = phonetest.phone_dialer.PhoneDialer(self.driver, phone_dialer_conf)



