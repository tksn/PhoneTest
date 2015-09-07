
class PhoneTestException(Exception):
    """ PhoneTest exception class """

    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return 'PhoneTestException: {0}'.format(self.message)
