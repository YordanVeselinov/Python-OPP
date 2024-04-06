from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INITIAL_INTEREST_RATE = 1.5
    INITIAL_AMOUNT = 2000
    INCREASE_INTEREST_RATE = 0.2

    def __init__(self):
        super().__init__(self.INITIAL_INTEREST_RATE, self.INITIAL_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST_RATE
