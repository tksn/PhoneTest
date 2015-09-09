import os.path
from phonetest.phone import Phone

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_YML = os.path.join(BASE_PATH, 'emulator.yml')
TESTPROBE_APK = os.path.join(BASE_PATH, 'testprobe.apk')


def before_all(context):
    with open(CONFIG_YML, 'r', newline='') as config_file:
        context.phone = Phone(config_yml=config_file,
                              deviceName='emulator-5554',
                              app=TESTPROBE_APK)


def after_all(context):
    pass
    #context.phone.close()
