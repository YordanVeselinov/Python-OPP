from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INITIAL_INTEREST_RATE = 3.5
    INITIAL_AMOUNT = 50_000
    INCREASE_INTEREST_RATE = 0.5

    def __init__(self):
        super().__init__(self.INITIAL_INTEREST_RATE, self.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST_RATE
