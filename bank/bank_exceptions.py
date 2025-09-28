class BankActionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class BankOptionError(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
