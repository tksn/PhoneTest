import yaml
import appium
import phonetest.exception
import phonetest.logcat
import phonetest.phone_dialer
import phonetest.genericapp

class Phone(object):

    def __init__(self, config_yml, **kwargs):
        phonetest.logcat.start_logcat_watcher()
        self.config = yaml.load(config_yml)
        self.open(**kwargs)
        self.build_app_accessor()

    def open(self, **kwargs):
        startup_activity_name = self.config.get('startup_activity', '')
        activities = self.config.get('activities', {})
        startup_activity = activities.get(startup_activity_name, {})

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': self.config.get('platform_version'),
            'appPackage': startup_activity.get('package'),
            'appActivity': startup_activity.get('activity')
        }
        desired_caps.update(kwargs)
        self.driver = appium.webdriver.Remote(self.config.get('endpoint'), desired_caps)

    def close(self):
        self.driver.quit()
        self.driver = None

    def build_app_accessor(self):
        activities = self.config.get('activities', {})

        self.etc = {}
        for activity_name, activity_desc in activities.items():
            if activity_name == 'PhoneDialer':
                self.phone_dialer = phonetest.phone_dialer.PhoneDialer(self.driver, activity_desc)
            else:
                self.etc[activity_name] = phonetest.genericapp.GenericApp(self.driver, activity_desc)



