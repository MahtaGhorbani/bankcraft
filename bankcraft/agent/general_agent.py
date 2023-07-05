from mesa import Agent
from bankcraft.bank_account import BankAccount
from uuid import uuid4


class GeneralAgent(Agent):
    def __init__(self, model):
        self.unique_id = uuid4().int
        super().__init__(self.unique_id, model)
        self.bank_accounts = None
        self.wealth = 1

    def step(self):
        pass

    def assign_bank_account(self, model, initial_balance):
        account_types = ['chequing', 'saving', 'credit']
        bank_accounts = [[0] * len(account_types)] * len(model.banks)
        for (bank, bank_counter) in zip(model.banks, range(len(model.banks))):
            for (account_type, account_counter) in zip(account_types, range(len(account_types))):
                bank_accounts[bank_counter][account_counter] = BankAccount(self, bank, initial_balance, account_type)

        return bank_accounts
    
    def updateMoney(self):
        self.wealth = sum(account[0].balance for account in self.bank_accounts)
