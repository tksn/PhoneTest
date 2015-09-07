
import phonetest.exception
import phonetest.logcat


class Phone(object):

    def __init__(self):
        phonetest.logcat.init_logcat_watcher()
