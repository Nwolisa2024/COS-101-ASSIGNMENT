import tkinter as tk
from tkinter import messagebox


def create_account():
    account_number = account_number_entry.get()
    account_type = account_type_var.get()


    if not account_number.isdigit():
        messagebox.showerror("Error", "Invalid account number. Please enter a valid account number🤔.")
        return


    if account_number in accounts:
        messagebox.showerror("Error", "Account number already exists. Please choose a different number😉.")
        return


    accounts[account_number] = account_type
    messagebox.showinfo("Success", "Account created successfully.")


def perform_transaction():
    account_number = account_number_entry.get()
    amount = float(amount_entry.get())
    transaction_type = transaction_type_var.get()


    if account_number not in accounts:
        messagebox.showerror("Error", "Account not found🙄.")
        return


    current_balance = balances.get(account_number, 0.0)
    if transaction_type == "Deposit":
        current_balance += amount
    elif transaction_type == "Withdraw":
        if amount > current_balance:
            messagebox.showerror("Error", "Insufficient funds😟.")
            return
        current_balance -= amount

    balances[account_number] = current_balance
    messagebox.showinfo("Success", "Transaction completed successfully🤗👍.")


def display_account():
    account_number = account_number_entry.get()


    if account_number not in accounts:
        messagebox.showerror("Error", "Account not found.")
        return


    account_type = accounts[account_number]
    balance = balances.get(account_number, 0.0)

    messagebox.showinfo("Account Details✌", f"Account Number: {account_number}\nAccount Type: {account_type}\nBalance: {balance}")


window = tk.Tk()
window.title("Welcome to nazzybank☺")


account_number_label = tk.Label(window, text="Account Number:")
account_number_label.pack()
account_number_entry = tk.Entry(window)
account_number_entry.pack()


account_type_label = tk.Label(window, text="Account Type:")
account_type_label.pack()

account_type_var = tk.StringVar()
account_type_var.set("Savings")

savings_radio = tk.Radiobutton(window, text="Savings", variable=account_type_var, value="Savings")
savings_radio.pack()

current_radio = tk.Radiobutton(window, text="Current", variable=account_type_var, value="Current")
current_radio.pack()


transaction_type_label = tk.Label(window, text="Transaction Type:")
transaction_type_label.pack()

transaction_type_var = tk.StringVar()
transaction_type_var.set("Deposit")

deposit_radio = tk.Radiobutton(window, text="Deposit", variable=transaction_type_var, value="Deposit")
deposit_radio.pack()

withdraw_radio = tk.Radiobutton(window, text="Withdraw", variable=transaction_type_var, value="Withdraw")
withdraw_radio.pack()


amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()


create_account_button = tk.Button(window, text="Create Account", command=create_account)
create_account_button.pack()

perform_transaction_button = tk.Button(window, text="Perform Transaction", command=perform_transaction)
perform_transaction_button.pack()

display_account_button = tk.Button(window, text="Display Account Details", command=display_account)
display_account_button.pack()


accounts = {}
balances = {}


window.mainloop()
