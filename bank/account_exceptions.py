class AccountCreationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WithdrawError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
