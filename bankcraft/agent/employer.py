from bankcraft.agent.general_agent import GeneralAgent
from bankcraft.transaction import *
from bankcraft.steps import steps
import random


class Employer(GeneralAgent):
    def __init__(self, model):
        super().__init__(model)
        self.pay_period = random.choice([steps['biweekly'], steps['month']])
        self.employees = []
        self.initial_fund = 1000000
        self.bank_accounts = self.assign_bank_account(model, self.initial_fund)
        # These are for use of agent reporter and needs to be handled better in the future
        self.money = self.initial_fund
        self.motivation = None

    def is_pay_date(self, date):
        return date % self.pay_period == 0

    def step(self):
        if self.is_pay_date(self.model.schedule.steps):
            for i in self.employees:
                self.pay(i.salary_per_pay, i, 'cheque', 'salary')
