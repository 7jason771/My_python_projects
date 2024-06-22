import csv
import os

os.system("cls")

# Welcome screen
name = 'Automated Teller Machine'
box = '='
side_box = '|'
print(box * (len(name) + 4))
print(side_box, name, side_box)
print(box * (len(name) + 4), '\n')


# main function (insert card)
def main():
    insert_card = input("Press Y to Insert Card: ")
    if "y" == insert_card.lower():
        login()
    else:
        print("Thank you for using this ATM!")
        pass


# login function (pin validation)
def login():
    input_pin = input("\nEnter Pin: ")

    with open('ATM.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        temp = next(csv_reader)
        pin = temp[1]

    if input_pin == pin:
        dashboard()
    else:
        print("\nIncorrect Pin")
        go_back = input("\nEnter y to try again, enter n to exit: ")
        while go_back == "y":
            login()
        else:
            exit()


# closes the program (exit function)
def exit():
    print("Thank you for using this ATM!")
    pass

# displays the dashboard and list of transactions
def dashboard():
    print("\n")
    print("==========================")
    print(f'''
Transaction list:

1. Deposit
2. Check Balance
3. Withdraw
4. Exit
    ''')
    print("\n")

    transaction = int(input("Choose your transaction: "))
    if transaction == 1:
        deposit()
        dashboard()
    elif transaction == 2:
        check_balance()
        dashboard()
    elif transaction == 3:
        withdraw()
        dashboard()
    elif transaction == 4:
        exit()
    else:
        dashboard()


# provides deposit transaction for the user (deposit function)
def deposit():
    amount_to_deposit = int(input("Enter Desired Money: "))

    with open('ATM.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        temp = next(csv_reader)
        new_balance = int(temp[2]) + amount_to_deposit
        user = temp[0]
        pin = temp[1]

    with open('ATM.csv', "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([user, pin, new_balance])

    print("\nDeposit Processing...")
    print("Successful Deposit")


# checks the user's balance (check balance function)
def check_balance():
    print("Retrieving balance...")
    with open('ATM.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        print("User balance: ", next(csv_reader)[2])


# withdraws the user's current balance (withdraw function)
def withdraw():
    money_to_withraw = int(input("Input desired money: "))
    with open('ATM.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        temp = next(csv_reader)
        balance = temp[2]
        user = temp[0]
        pin = temp[1]

    if int(balance) >= money_to_withraw:
        deducted_balance = int(balance) - money_to_withraw

        with open('ATM.csv', "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([user, pin, deducted_balance])

        print("SUCCESS! Your new balance is: ", deducted_balance)

    else:
        print("insufficient balance")


# execute the main function
main()
