class AddCustomerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class LoginCustomerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)