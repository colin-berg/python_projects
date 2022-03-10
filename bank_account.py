"""" 
This program allows you to create and manipulate a personal bank account (accepting deposits, allowing withdrawals, displaying balance, and showing account details)
"""

class BankAccount(object):
  balance = 0

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "This account belongs to %s. Balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    print "Balance: $%.2f" % (self.balance)

  def deposit(self, amount):
    #self.amount = amount

    if amount <= 0:
      print "Error depositing funds. Please enter a valid number."
      return
    else:
      print "You have deposited $%.2f" % (amount) 
      self.balance += amount
      self.show_balance()
    
  def withdraw(self, amount):

    if amount > self.balance:
      print "Error: Cannot withdraw more than current balance."
      return 
    else: 
      print "Withdraw $%.2f" % (amount)
      self.balance -= amount
      self.show_balance()


my_account = BankAccount('Colin')
print my_account    
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account 
