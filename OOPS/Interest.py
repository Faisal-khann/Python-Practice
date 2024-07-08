# Real Example of Polymorphism
class Bank:
    def get_rate_of_interest(self):
        return 0.0


class SBI(Bank):
    def get_rate_of_interest(self):
        return 8.4


class HDFC(Bank):
    def get_rate_of_interest(self):
        return 7.5


class PNB(Bank):
    def get_rate_of_interest(self):
        return 6.8

def main():
# Creating instance of Parent class and pointing it to child classes
    bank = Bank()

    bank = SBI()
    print(f"SBI Rate of Interest: {bank.get_rate_of_interest()}%")

    bank = HDFC()
    print(f"HDFC Rate of Interest: {bank.get_rate_of_interest()}%")

    bank = PNB()
    print(f"PNB Rate of Interest: {bank.get_rate_of_interest()}%")

if __name__ == "__main__":
    main()
  
