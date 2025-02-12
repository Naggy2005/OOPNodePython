from Account import (
    SavingsAccount, CheckingAccount, HighInterestSavingsAccount, 
    OverDraftCheckingAccount, PremiumOverdraftCheckingAccount
)

def main():
    # Create and interact with Account
    savings = SavingsAccount("12345", "Bob Smith", 1000)
    premium = PremiumOverdraftCheckingAccount("67890", "Alice Johnson", 2000)

    # perfomr some operation
    savings.deposit(500)
    premium.withdraw(2500)
    premium.deposit(1000)

    #Display balances
    savings.display_balance()
    premium.display_balance()

if __name__ == "__main__":
    main()
