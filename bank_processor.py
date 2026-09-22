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
        temp_result = ["ok"]
        mssge["results"] = temp_result
    def update_rejected():
        temp_result = ["rejected"]
        mssge["results"] = temp_result

    def deposit(transaction, account):
        if account in balances:
            temp_balances[account] = balances[account] + transaction["amount"]
            update_sucessful(temp_balances)
        else:
            update_rejected()

    def withdraw(transaction, account):
        if account in balances:
            if transaction["amount"] <= balances[account]:
                temp_balances[account] = balances[account] - transaction["amount"]
                update_sucessful(temp_balances)
            else:
                update_rejected()
        else:
            update_rejected()

    for transaction in transactions:
        temp_balances = {}
        account_type = transaction["type"]
        if account_type == "deposit":
            account = transaction["account"]
            deposit(transaction, account)
        elif account_type == "withdraw":
            account = transaction["account"]
            withdraw(transaction, account)
        elif account_type == "transfer":
            _, From, To,_ = transaction.values()
            if From in balances and To in balances:
                withdraw(transaction, From)
                deposit(transaction, To)
            else:
                update_rejected(temp_result)
    return mssge

print(process_transactions({"A": 100}, [{"type": "deposit", "account": "A", "amount": 50}, {"type": "withdraw", "account": "A", "amount": 100}]))
#{"balances": {"A": 150}, "results": ["ok"]}
print(process_transactions({"A": 100}, [{"type": "withdraw", "account": "A", "amount": 200}]))
#{"balances": {"A": 100}, "results": ["rejected"]}
print(process_transactions({"A": 100, "B": 0}, [{"type": "transfer", "from": "A", "to": "B", "amount": 40}]))
#{"balances": {"A": 60, "B": 40}, "results": ["ok"]}