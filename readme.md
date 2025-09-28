# 🏦 Bank Management System
A **Python-based** application designed with a focus on Object-Oriented Programming (OOP) and Test-Driven Development (TDD). It simulate the bank management system core operations including create account, withdraw, deposit, and transfer.

## 💳 Description
The application demonstrates the transaction that can be done by the customer such as withdraw money, deposit money, or transfer money between customer's account or from customer to another. A `bank.csv` file used in this application to simulate the real data storing and muniplation. The application implements the design of OOP by including 3 classes (plus testing classes) and structured based on the Test-Driven Development (TDD) principles as shown below:

```
/Banking_Project
    ├── bank.csv
    ├── main.py
    ├── readme.md
    ├── bank/
    │   ├── __init__.py
    │   ├── account_exceptions.py
    │   ├── account.py
    │   ├── bank_exceptions.py
    │   ├── bank.py
    │   ├── customer_exceptions.py
    │   └── customer.py
    │
    └── tests/
        ├── __init__.py
        ├── test_customer.py
        ├── test_deposit_operation.py
        ├── test_overdraft_portection_fee.py
        ├── test_transfer_between_accounts.py
        ├── test_transfer_to_customer_account_operation.py
        └── test_withdraw_operation.py
```

## 💸 Features
* User-friendly interface for smooth interaction.
* Create customer account with checking balance, savings balance, or both.
* Withdraw money from checking account or savings account.
* Deposit money into checking account or savings account.
* Transfer money between customer's checking and savings account or from one customer to another.
* Applies ACME overdraft protection fee and deactivation for the account after 2 overdraft attempts.
* Account reactivation throught deposit the charged amount.

## 💻 Code Blocks
### 💰 Initate checking or savings account:
`account.py`
```
try:
    print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
    account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
    match account_creation:
        case 'yes':
            try:
                checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                if type(int(checking_balance)) == int:
                    if int(checking_balance) >= 0:
                        bank_customers.customers[row_index][4] = int(checking_balance)
                        bank_customers.update_customers()
                        print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                        deposit_completed = True
                        operation_completed = True
                        break
                    elif int(checking_balance) < 0:
                        operation_completed = True
                        raise accountExp.DepositOperationError('Can not initiate your checking account with neigative amount\n')
            except ValueError:
                raise accountExp.DepositOperationError('Enter 0 or a POSITIVE NUMBER')
        case 'no':
            print('💰 | Your checking account still not created\n')
            deposit_completed = True
            operation_completed = True
            break
        case _:
            operation_completed = True
            raise ValueError
except ValueError:
    raise accountExp.DepositOperationError('Enter a YES or NO only')
```

### ⚠️ Account Deactivation after 2 over draft attempts prompt:
`bank.py`
```
def overdraft_protection_fee(self, customer_id, amount):
    overdraft_fee_applied = False
    bank_customers = Bank()
    bank_customers.retrieve_customers()
    overdraft_fee = 35
    with open(self.file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        row_index = 1
        for row in reader:
            if customer_id == row[0]:
                if int(bank_customers.customers[row_index][7]) == 0:
                    print(f'⚠️  | You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                    bank_customers.customers[row_index][4] = int(bank_customers.customers[row_index][4]) - int(amount) - overdraft_fee
                    bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                    print(f'\n⚠️  | Based on the Overdraft Protection Rules, you are charged ${overdraft_fee} for this overdraft\nℹ️  | Number of attemtps before deactivate the account = {bank_customers.customers[row_index][7]}\n💲 | The checking account balance now is {bank_customers.customers[row_index][4]}')
                    bank_customers.update_customers()
                    overdraft_fee_applied = True
                    break

                elif int(bank_customers.customers[row_index][7]) == 1:
                    print(f'⚠️  | You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                    bank_customers.customers[row_index][4] = int(bank_customers.customers[row_index][4]) - int(amount) - overdraft_fee
                    bank_customers.customers[row_index][6] = 'deactive'
                    bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                    print(f'\n⚠️  | Based on the Overdraft Protection Rules, you are charged ${overdraft_fee} for this overdraft\nℹ️  | You have reached the maximum overdraft attempts = {bank_customers.customers[row_index][7]}, and your account now is DEACTIVE\n💲 | The checking account balance now is {bank_customers.customers[row_index][4]}')
                    bank_customers.update_customers()
                    overdraft_fee_applied = True
                    break
            row_index += 1
    return overdraft_fee_applied
```

### ☑️ Account Reactivation prompt:
`bank.py`
```
    def activate_customer(self, customer_id, amount):
        account_activated = False
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row_index = 1
            for row in reader:
                if customer_id == row[0]:
                    if int(bank_customers.customers[row_index][7]) == 2 and int(bank_customers.customers[row_index][4]) < 0:
                        print(f'✔️  | Your account has been reactivated as the checking account balance now is {int(bank_customers.customers[row_index][4]) + int(amount)}')
                        bank_customers.customers[row_index][4] = str(int(bank_customers.customers[row_index][4]) + int(amount))
                        bank_customers.customers[row_index][6] = 'active'
                        bank_customers.customers[row_index][7] = 0
                        bank_customers.update_customers()
                        account_activated = True
                        return account_activated
                row_index += 1
```

`account.py`
```
try:
    print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
    reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
    match reactivate:
        case 'yes':
            print(f'\n💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
            charge_amount = int(input('💳 | Charge Amount: '))
            aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
            if aprroved_balance < 0:
                operation_completed = True
                raise accountExp.WithdrawOperationError(f'This {charge_amount} can not reactivate your account')
            else:
                bank_customers.activate_customer(customer_id, charge_amount)
                withdraw_completed = True
                operation_completed = True
        case 'no':
            withdraw_completed = True
            operation_completed = True
            raise accountExp.WithdrawAlert('Your account remain DEACTIVE')
        case _:
            operation_completed = True
            raise ValueError
except ValueError:
    raise accountExp.WithdrawOperationError('Enter a YES or NO only')
except accountExp.WithdrawAlert as e:
    print(f'💰 | WithdrawAlert: {e}\n')
```




## 💡 Learned Ideas
* The logic of access, read, and manipulate a .csv file data.
* How to build a project that must be carried out using a test-driven development (TDD) approach.
