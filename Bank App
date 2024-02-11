3import tkinter as tk

window = tk.Tk()
window.title("GTWorld Bank App")

account_label = tk.Label(window, text="Select Account Type:")
account_label.pack()

account_var = tk.StringVar()

savings_radio = tk.Radiobutton(window, text="Savings Account", variable=account_var, value="Savings")
savings_radio.pack()

current_radio = tk.Radiobutton(window, text="Current Account", variable=account_var, value="Current")
current_radio.pack()

withdraw_label = tk.Label(window, text="Withdraw Amount (₦):")
withdraw_label.pack()
withdraw_entry = tk.Entry(window)
withdraw_entry.pack()

deposit_label = tk.Label(window, text="Deposit Amount (₦):")
deposit_label.pack()
deposit_entry = tk.Entry(window)
deposit_entry.pack()

balance_label = tk.Label(window, text="Account Balance (₦):")
balance_label.pack()
balance_value_label = tk.Label(window, text="₦0.00")
balance_value_label.pack()

account_balance = 0.00


def withdraw():
    amount = float(withdraw_entry.get())
    account_type = account_var.get()

    global account_balance
    account_balance -= amount

    balance_value_label.config(text=f"₦{account_balance:.2f}")

    withdraw_entry.delete(0, tk.END)


def deposit():
    amount = float(deposit_entry.get())
    account_type = account_var.get()

    global account_balance
    account_balance += amount

    balance_value_label.config(text=f"₦{account_balance:.2f}")

    deposit_entry.delete(0, tk.END)


def check_balance():
    account_type = account_var.get()

    balance_value_label.config(text=f"₦{account_balance:.2f}")


withdraw_button = tk.Button(window, text="Withdraw", command=withdraw)
withdraw_button.pack()

deposit_button = tk.Button(window, text="Deposit", command=deposit)
deposit_button.pack()

balance_button = tk.Button(window, text="Check Balance", command=check_balance)
balance_button.pack()

window.mainloop()
