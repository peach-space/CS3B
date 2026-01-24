#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 3
# Student Name: Cen Li
# SID: 20713344
#################################################


class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_shift_number(self, shift):
        self._shift_number = shift

    def set_hourly_pay_rate(self, rate):
        self._hourly_pay_rate = rate

def run():
    print("--- Enter Employee Details ---")

    name = input("Enter name: ")
    number = input("Enter employee number: ")
    shift = int(input("Enter shift number (1 for Day, 2 for Night): "))
    pay_rate = float(input("Enter hourly pay rate: "))

    worker = ProductionWorker(name, number, shift, pay_rate)

    print("\n--------------------------")
    print("      Worker Information")
    print("--------------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")

    shift_str = "Day" if worker.get_shift_number() == 1 else "Night"
    print(f"Shift: {shift_str} (Code: {worker.get_shift_number()})")

    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

    print("Hello from Question 3!")


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()