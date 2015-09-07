
class PhonetestException(Exception):

    """
    """

    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return 'PhonetestException: {0}'.format(self.message)
