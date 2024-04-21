from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPE_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_TYPE_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    MATCHING_TYPES = {
        "StudentLoan": "Student",
        "MortgageLoan": "Adult"
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        try:
            loan = self.VALID_TYPE_LOANS[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        try:
            client = self.VALID_TYPE_CLIENTS[client_type](client_name, client_id, income)
        except KeyError:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan: BaseLoan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))
        client: BaseClient = next(filter(lambda l: l.client_id == client_id, self.clients))

        client_type = client.__class__.__name__

        if not (client_type == "Student" and loan_type == "StudentLoan") and not (
                client_type == "Adult" and loan_type == "MortgageLoan"):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client: BaseClient = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_loans += 1
        return f"Successfully changed {number_of_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        number_of_clients = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                number_of_clients += 1

        return f"Number of clients affected: {number_of_clients}."

    def get_statistics(self):
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = 0
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([l.amount for l in self.loans])
        
        if len(self.clients) == 0:
            avg_client_interest_rate = 0
        else:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)

        for c in self.clients:
            for l in c.loans:
                granted_sum += l.amount

        result = f"Active Clients: {len(self.clients)}\n" \
                 f"Total Income: {sum([c.income for c in self.clients]):.2f}\n" \
                 f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
                 f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n" \
                 f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

        return result
