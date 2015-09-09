import io
import pytest


@pytest.fixture()
def fake_adb(monkeypatch):
    fake_process = type('FakeAdbProcess', (), {})()
    fake_process.stdout = io.BytesIO()
    fake_process.kill = lambda: None
    fake_process.communicate = lambda: None

    def fake_popen(_, stdout):
        return fake_process

    monkeypatch.setattr('subprocess.Popen', fake_popen)
    return fake_process


@pytest.fixture()
def fake_driver(monkeypatch):
    fake_driver_obj = type('FakeDriver', (), {})()

    def fake_driver_remote(endpoint, desired_caps):
        fake_driver_obj.endpoint = endpoint
        fake_driver_obj.desired_caps = desired_caps
        return fake_driver_obj

    monkeypatch.setattr('appium.webdriver.Remote', fake_driver_remote)
    return fake_driver_obj