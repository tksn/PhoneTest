import os.path
import pytest
from phonetest.phone import Phone


def test_phone_load_config_file(fake_adb, fake_driver):
    p = None
    basedir = os.path.dirname(os.path.realpath(__file__))
    testfile = os.path.join(basedir, 'conf_Xperia_T2_Ultra.yml')
    with open(testfile, 'r', newline='') as f:
        p = Phone('', f)
    activity = p.config.get('activities', {}).get('PhoneDialer', {}).get('activity')
    assert activity == '.DialerEntryActivity'


def test_phone_load_config_text(fake_adb, fake_driver):
    p = Phone('', 'hoge: fuga')
    assert p.config.get('hoge') == 'fuga'


def test_phone_driver_init(fake_adb, fake_driver):
    p = Phone('abc',
              """
              endpoint: def
              platform_version: '4.4'
              startup_activity: Act0
              activities:
                Act0:
                  package: com.example.app
                  activity: .Act0
              """)
    assert fake_driver.endpoint == 'def'
    assert fake_driver.desired_caps['deviceName'] == 'abc'
    assert fake_driver.desired_caps['platformName'] == 'Android'
    assert fake_driver.desired_caps['platformVersion'] == '4.4'
    assert fake_driver.desired_caps['appPackage'] == 'com.example.app'
    assert fake_driver.desired_caps['appActivity'] == '.Act0'
