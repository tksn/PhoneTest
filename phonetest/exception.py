
class PhoneTestException(Exception):
    """ PhoneTest exception class """

    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return 'PhoneTestException: {0}'.format(self.message)


class LogcatException(PhoneTestException):
    """ Logcat exception class """

    def __init__(self, message=''):
        PhoneTestException.__init__(self, message)


class LocatorException(PhoneTestException):
    """ Locator exception class """

    def __init__(self, message=''):
        PhoneTestException.__init__(self, message)


