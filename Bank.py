def bank ():
    from datetime import datetime
    bank_accounts = {
        1001: {
            "first_name": "Alice",
            "last_name": "Smith",
            "id_number": "123456789",
            "balance": 2500.50,
            "transactions_to_execute": [
                ("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
            "transaction_history": [
                ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00", 1001, 1002, 1000)]
        },
        1002: {
            "first_name": "Bob",
            "last_name": "Johnson",
            "id_number": "987654321",
            "balance": 3900.75,
            "transactions_to_execute": [("2025-01-23 10:05:00", 1002, 1001, 3000), ("2025-08-17 15:00:00", 1002, 1003, 2000)],
            "transaction_history": [("2024-08-15 09:00:00", 1002, 1004, 500, "2024-08-15 09:30:00", 1002, 1004, 1000)]

        },
        1003: {
            "first_name": "Charles",
            "last_name": "Bronson",
            "id_number": "222014651",
            "balance": 40000000.4,
            "transactions_to_execute": [("2025-01-23 10:05:00", 1003, 1001, 30000), ("2025-02-23 15:00:00", 1003, 1004, 400)],
            "transaction_history": [("2022-01-23 10:05:00", 1003, 1001, 30000), ("2022-02-23 15:00:00", 1003, 1002, 400)]
        },
        1004:{
            "first_name": "Arnon",
            "last_name": "Zadok",
            "id_number": "323395176",
            "balance": -50000,
            "transactions_to_execute": [("2025-07-11 12:00:00", 1004, 1001, 30), ("2025-09-15 10:00:00", 1004, 1003, 15)],
            "transaction_history": [("2014-10-01 14:00:00", 1004, 1002, 1500), ("2001-01-28 12:07:00", 1004, 1002, 9200)]
            }
        }
    sample_account = {
        "first_name": " ",
        "last_name": " ",
        "id_number": " ",
        "balance": 000,
        "transactions_to_execute": [
            ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000), ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000)],
        "transaction_history": [
            ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000, "%Y-%m-%d %H:%M:%S", 0000, 0000, 000)]
    }

    while True:
        operation: str = str(input(F"Hello, which operation would you like to perform? \n Open an New Account [N] \n Work on an Existing Account [E]"))
        if operation.lower() == "n":
            print("Starting a new account creation process:")
            new_account_number: int = int(max(bank_accounts.keys())+1)
            new_account = sample_account.copy()
            new_account.update({
            "first_name" :  input("First Name: "),
            "last_name" : input("Last Name: "),
            "id_number" : input("ID_Number: "),
            "balance" : float(input("Balance: ")),
            "transactions_to_execute" : [],
            "transaction_history" : [],
            })
            
            print(f"New Account created successfully!\nAccount Number: {new_account_number}\nAccount Details: {bank_accounts[new_account_number]}")
        elif operation.lower() == "e":
            account_number: int = int(input(f"Which account number would you like to perform actions for?\n Available accounts are:\n {list(bank_accounts.keys())}"))
            if not account_number in bank_accounts:
                print("Sorry, this account number is not valid")
                continue
            if account_number in bank_accounts:
                action: str = str(input(f"Would you like to:\n Make a New Transaction [Press 1]\n Execute all the Existing Transactions [Press 2]"))
                if action == '1':
                    des_account:int = int(input("To which account should you make the transaction?"))
                    if not des_account in bank_accounts:
                        print("Sorry, this account number does not exist in the system")
                        continue
                    else:
                        trans_amount: int = int(input("What's the amount for transaction?"))
                        trans_details: tuple = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),account_number,des_account,trans_amount)
                        bank_accounts [account_number]["transactions_to_execute"].append(trans_details)
                elif action == '2':
                    try:
                        trans_index: int = int(input(f"Which transaction would you like to execute? choose  0 - {len(bank_accounts [account_number]["transactions_to_execute"])-1}"))
                        trans_to_execute = (bank_accounts[account_number]["transactions_to_execute"][trans_index])
                        trans_to_execute = (list(trans_to_execute))
                        trans_to_execute[0] = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        trans_to_execute = (tuple(trans_to_execute))
                        bank_accounts [account_number]["transaction_history"].append(trans_to_execute)
                        trans_amount = trans_to_execute [3]
                        bank_accounts[account_number].update({"balance": bank_accounts [account_number] ["balance"] - trans_amount})
                        des_account = bank_accounts[account_number]["transactions_to_execute"][trans_index][2]
                        bank_accounts[des_account].update({"balance": bank_accounts[des_account]["balance"] + trans_amount})
                        del (bank_accounts[account_number]["transactions_to_execute"][trans_index])
                    except:
                        print("Out of range. Please try again")
                        continue
                else:
                    print("Sorry, this option is invalid")
                    continue
    print(bank_accounts)

print(bank())
