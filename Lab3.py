"""Polymorphism is basically "one interface, many actions.
   It allows different classes to be treated as instances of the same parent class.
   This means you can send the same message to different objects,
   and each object will respond in its own unique way based on its specific class.
   You don't need to write complex "if-else" logic to check every type
"""


#################################################
# Challenge: Polymorphism in Contract Submission
# Student Name: Cen Li
#################################################

# Parent Class
class Contract:
    def __init__(self, title):
        self.title = title

    def submit(self):
        pass


# Subclass: Normal Contract
class NormalContract(Contract):
    def submit(self):
        return f"Contract '{self.title}': Submitted successfully. Status: COMPLETED."


# Subclass: Financial Contract
class FinancialContract(Contract):
    def submit(self):
        return f"Contract '{self.title}': Submitted. Status: PENDING FINANCIAL APPROVAL."


# Subclass: Business Contract
class BusinessContract(Contract):
    def submit(self):
        return f"Contract '{self.title}': Submitted. Status: PENDING BUSINESS REVIEW."


def click_submit_button(contract_object):
    result = contract_object.submit()
    print(result)


def run():
    c1 = NormalContract("Office Supplies Purchase")
    c2 = FinancialContract("Annual Audit Report")
    c3 = BusinessContract("Global Partnership Agreement")

    print("--- Processing Contract Submissions ---")

    click_submit_button(c1)
    click_submit_button(c2)
    click_submit_button(c3)


if __name__ == "__main__":
    run()