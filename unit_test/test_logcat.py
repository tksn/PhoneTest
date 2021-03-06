import io
import pytest
from phonetest.exception import LogcatException
from phonetest.logcat import *


def set_fake_adb_data(fake_adb, data):
    fake_adb.stdout.writelines(data)
    fake_adb.stdout.seek(0)


def run_logcat_watcher(fake_adb, data):
    set_fake_adb_data(fake_adb, data)
    lc = LogcatWatcher()
    lc.stop()
    lc.check_errors('test_logcat/run_logcat_watcher')


def test_logcat_fatal_exception_found(fake_adb):
    with pytest.raises(LogcatException) as excinfo:
        run_logcat_watcher(
            fake_adb, [
                b'I/ActivityManager(  999999): -------',
                b'E/AndroidRuntime( 9999): FATAL EXCEPTION: main',
                b'I/ActivityManager(  999999): -------'
            ])
    assert 'fatal' in str(excinfo.value)


def test_logcat_fatal_exception_not_found(fake_adb):
    run_logcat_watcher(
        fake_adb, [
            b'I/ActivityManager(  999999): -------',
            b'E/AndroidRuntime( 9999): --------',
            b'I/ActivityManager(  999999): -------'
        ])

def test_logcat_check_decorator(fake_adb):

    @with_logcat_check
    def func():
        pass

    set_fake_adb_data(
        fake_adb, [b'E/AndroidRuntime( 9999): FATAL EXCEPTION: main'])
    start_logcat_watcher()
    stop_logcat_watcher()

    with pytest.raises(LogcatException) as excinfo:
        func()
    assert 'fatal' in str(excinfo.value)
    assert 'pre_op' in str(excinfo.value)
