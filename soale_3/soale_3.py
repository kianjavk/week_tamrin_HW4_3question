identifier = 0

class BankAccount:
    def __init__(self, name, balance,minimum_balance):
        global identifier
        self.id = identifier
        self.name = name
        self.balance = balance
        self.minimum_balance = minimum_balance
        identifier += 1

    def __str__(self):
        return f'{self.id}, {self.name} , {self.balance} , {self.minimum_balance}'


    def withdraw(self, amount_withdraw):
        if amount_withdraw < self.balance:
            if self.balance - amount_withdraw < self.minimum_balance:
                print("can't withdraw if balance gets less than minimum balance")
            else:
                self.balance -= amount_withdraw
                print(f'balance :{self.balance}')
        else:
            print('You cannot withdraw more than your balance')


    def deposit(self, amount_deposit):
        if amount_deposit > 0:
            self.balance += amount_deposit
            print(f'balance :{self.balance}')
            return f'deposit amount :{amount_deposit}'
        else:
            print('deposit amount cant be ziro')

    def transit(self, bank_account, amount_transit):
        if amount_transit <= 0:
            print("transit amount can't be ziro")
        else:
            if bank_account.id == self.id:
                print("transit id can't be same as user id")
            else:
                if amount_transit < self.balance:
                    if self.balance - amount_transit < self.minimum_balance:
                        print("can't withdraw if balance gets less than minimum balance")
                    else:
                        self.balance -= amount_transit
                        bank_account.balance += amount_transit
                        print(f'my account balance :{self.balance}')
                        print(f'target account balancce :{bank_account.balance}')
                else:
                    print('You cannot withdraw more than your balance')


def main():
    try:
        minimum_balance = int(input("enter minimum balance for accounts:"))
        my_depos = BankAccount(input('Enter your name :'), int(input('Enter your balance:')), minimum_balance)
        print(my_depos.__str__())
        print()
        deposits = []
    except ValueError:
        print("input is incorrect")
    while True:
        try:
            print()
            print('1. To withdraw')
            print('2. To deposit')
            print('3. To transfer')
            print('4. To create new bank account')
            choice = input("Enter your choice: ")
            if choice == '1':
                amount_withdraw = int(input('Enter amount of withdraw: '))
                my_depos.withdraw(amount_withdraw)
                print()
            elif choice == '2':
                amount_deposit = int(input('Enter amount of deposit: '))
                my_depos.deposit(amount_deposit)
                print('')
            elif choice == '3':
                amount_transit = int(input('Enter amount of deposit: '))
                trasit_id = int(input('Enter id which you want to transfer: '))
                exist = False
                for depose in deposits:
                    if depose.id == trasit_id:
                        exist = True
                        my_depos.transit(depose, amount_transit)
                        break
                if not exist:
                    print("this account dosn't exist")
                print()
            elif choice == '4':
                new_depose = BankAccount(input('Enter your name :'), int(input('Enter your balance :')), minimum_balance)
                deposits.append(new_depose)
                print(new_depose.__str__())

        except ValueError:
            print('Please enter only numbers')

        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()





