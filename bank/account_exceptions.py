class AccountCreationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WithdrawOptionError(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WithdrawOperationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
