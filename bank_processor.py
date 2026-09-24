def process_transactions(initial_balances, transactions):
    # TODO: apply each transaction in order to a working copy of the balances.
    # Reject invalid transactions without changing balances. Do not modify
    # the `initial_balances` argument.

    #1 copy the initial balances dict
    #2 forms a default mssge
    #3 specify a list of allowed operation
    #4 for each transaction check if the transaction type exists in allowed_type
    # checks if the transaction amount is lesser than or equal to

    balances = {**initial_balances}
    mssge = {"balances": balances, "results": []}

    def update_sucessful(temp_ballance):
        mssge["balances"].update(temp_ballance)
        mssge["results"].append("ok")
    def update_rejected():
        mssge["results"].append("rejected")

    def deposit(transaction, account):
        if account in balances and transaction["amount"] > 0:
            return True
        else:
            return False
    def withdraw(transaction, account):
        if account in balances and transaction["amount"] > 0 and transaction["amount"] <= balances[account]:
            return True
        else:
            return False

    for transaction in transactions:
        temp_balances = {}
        account_type = transaction["type"]
        if account_type == "deposit":
            account = transaction["account"]
            if deposit(transaction, account):
                temp_balances[account] = balances[account] + transaction["amount"]
                update_sucessful(temp_balances)
            else:
                update_rejected()
        elif account_type == "withdraw":
            account = transaction["account"]
            if withdraw(transaction, account):
                temp_balances[account] = balances[account] - transaction["amount"]
                update_sucessful(temp_balances)
            else:
                update_rejected()
        elif account_type == "transfer":
            From, To = transaction["from"], transaction["to"]
            if From in balances and To in balances and withdraw(transaction, From) and deposit(transaction, To):
                temp_balances[From] = balances[From] - transaction["amount"]
                temp_balances[To] = balances[To] + transaction["amount"]
                update_sucessful(temp_balances)
            else:
                update_rejected(temp_result)
        else:
            update_rejected()
    return mssge

print(process_transactions({"A": 100}, [{"type": "deposit", "account": "A", "amount": 0}, {"type": "withdraw", "account": "A", "amount": 100}]))
#{"balances": {"A": 0}, "results": ["rejected","ok"]}
print(process_transactions({"A": 100}, [{"type": "withdraw", "account": "A", "amount": 10}]))
#{"balances": {"A": 90}, "results": ["ok"]}
print(process_transactions({"A": 100, "B": 0}, [{"type": "transfer", "from": "A", "to": "B", "amount": 40}]))
#{"balances": {"A": 60, "B": 40}, "results": ["ok"]}