# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:08:55 2023

@author: Fayssal
"""
import datetime


class BankAccount:
    
    all = []
    transaction_fee = 0.001
    
    def __init__(self, initial_amount:float, name:str, AccType: str=0):
        
        assert initial_amount > 0, f"Initial amount {initial_amount} is not greater than 0"
        self.balance = initial_amount
        self.name = name
        self.AccType = AccType
        BankAccount.all.append(self)
        print(f'Account name : {self.name} opened with a balance of {self.balance} $')
        
    def account_type(self):
        
        if  10000 <= self.balance<20000:
            self.AccType = "SILVER"
            print(f'Balance : {self.balance}, it is a {self.AccType} account')
        elif  20000 <= self.balance < 50000:
            self.AccType = "GOLDEN"
            print(f'Balance: {self.balance}, it is a {self.AccType} account')
        elif self.balance >= 50000:
            self.AccType = "WHITE"
            print(f'Balance: {self.balance}, it is a {self.AccType} account')
            
    def deposit(self, amount):
        
        assert amount > 0
        self.balance = self.balance + amount
        print(f'New balance of {self.name} account: {self.balance}')
            
    def BankingTransaction(self, OtherAcc:str, Amount:float):
        
        assert Amount >= 0, f"Amount {Amount} is not greater than 0"
        self.cost = Amount + Amount*self.transaction_fee
        if self.cost >= Amount:
            self.balance = self.balance - Amount*self.transaction_fee - Amount
            OtherAcc.balance = OtherAcc.balance + Amount
            #return self.balance, OtherAcc.balance
            print(f'Balance {self.name} : {self.balance} $')
            print(f'Balance {OtherAcc.name} : {OtherAcc.balance} $')
        else :
            print (f'Not enough funds for this transaction, balance: {self.balance}')
            
    def advantages(self):
        if self.AccType == "SILVER" and datetime.datetime.now().strftime("%m-%d") == "10-11":
            self.rate = 0.02
            self.balance += self.balance * self.rate
            print (f'New balance of {self.name} : {self.balance} $')
        elif self.AccType == "GOLDEN" and datetime.datetime.now().strftime("%m-%d") == "10-11":
            self.rate = 0.05
            self.balance += self.balance * self.rate
            print (f'New balance of {self.name} : {self.balance} $')
        elif self.AccType == "WHITE" and datetime.datetime.now().strftime("%m-%d") == "10-11":
            self.rate = 0.10
            self.balance += self.balance * self.rate
            
    def __repr__(self):
        return f'{self.name}, {self.AccType}, {self.balance}'
    
    def withdraw(self, amount):
        assert amount > 0, f"Amount {amount} is not greater than 0"
        if amount > self.balance:
            print(f'{self.name} do not have enough funds, balance: {self.balance}')
        else:
            self.balance = self.balance - amount
            print(f'{self.name} has done succesfully a withdraw of {amount} $ from his Bank Account\nNew balance: {self.balance}')

Account1 = BankAccount(15000,"Fayssal")
Account2 = BankAccount(100000,"John")
Account1.withdraw(2000)

Account1.account_type()
Account2.account_type()
BankAccount.all



