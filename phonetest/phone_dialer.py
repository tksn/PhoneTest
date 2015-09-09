from phonetest.genericapp import GenericApp


class PhoneDialer(GenericApp):

    def __init__(self, driver, config):
        GenericApp.__init__(self, driver, config)

    def dial(self, numbers):
        self.longtap('backspace')
        for digit in numbers:
            self.tap(digit)
        self.tap('call')
