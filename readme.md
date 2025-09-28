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
* Create customer account with checking balance and savings balance.
* Withdraw money from checking account or savings account.
* Deposit money into checking account or savings account.
* Transfer money between customer's checking and savings account or from one customer to another.
* Applies ACME overdraft protection fee and deactivation for the account after 2 overdraft attempts.
* Account reactivation throught deposit the charged amount.

## 💡 Learned Ideas
* The logic of access, read, and manipulate a .csv file data.
* How to build a project that must be carried out using a test-driven development (TDD) approach.
