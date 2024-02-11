import tkinter as tk

window = tk.Tk()


class Account:
    name = "John Jude"
    account_number = 6377987241
    account_balance = 1000


def __init__(self):
    self.name = "John Jude"
    self.account_number = 6377987241
    self.account_balance = 1000


def account_balance():
    account_balance = 1000
    print(account_balance)


def deposit(self, amount):
    self.account_balance = self.account_balance + amount
    print(self.account_balance)


def withdrawal(self, amount):
    self.account_balance = self.account_balance - amount
    print(self.account_balance)
    
class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

        current = CurrentAccount()
        current.deposit(amount=None)
        print(self.account_balance)

        current.withdrawal(amount=None)
        print(self.account_balance)
        
class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

        savings = SavingsAccount()
        savings.deposit(amount=None)
        print(self.account_balance)

        savings.withdrawal(amount=None)
        print(self.account_balance)


window.title("Welcome to GTWorld Bank😁")

frame = tk.Frame(master=window)
lbl_user = tk.Label(master=window, text="Username:")
ent_user = tk.Entry(master=window)
lbl_pass = tk.Label(master=window, text="Password:")
ent_pass = tk.Entry(master=window)
btn_lgb = tk.Button(master=window, text="Login")
lbl_lnk = tk.Label(master=window, text="Don't have an account?")
btn_crt = tk.Button(master=window, text="Create Account")
lbl_account = tk.Label(master=window, text="Account Type")
t = tk.StringVar()
t.get()
savings_radio = tk.Radiobutton(master=window, text="Savings", variable=t, value="1")
current_radio = tk.Radiobutton(master=window, text="Current", variable=t, value="2")
lbl_trans = tk.Label(master=window, text="Perform Transaction")
r = tk.StringVar()
r.get()
deposit_radio = tk.Radiobutton(master=window, text="Deposit", variable=r, value="1")
withdraw_radio = tk.Radiobutton(master=window, text="Withdraw", variable=r, value="2")
lbl_amount = tk.Label(master=window, text="Select Amount")
rad = tk.IntVar()
rad.get()
th_radio = tk.Radiobutton(master=window, text="1000", variable=rad, value=1)
th2_radio = tk.Radiobutton(master=window, text="3000", variable=rad, value=2)
th3_radio = tk.Radiobutton(master=window, text="5000", variable=rad, value=3)
th4_radio = tk.Radiobutton(master=window, text="10000", variable=rad, value=4)
th5_radio = tk.Radiobutton(master=window, text="20000", variable=rad, value=5)
th6_radio = tk.Radiobutton(master=window, text="30000", variable=rad, value=6)
th7_radio = tk.Radiobutton(master=window, text="50000", variable=rad, value=7)
th8_radio = tk.Radiobutton(master=window, text="100000", variable=rad, value=8)
lbl_ent = tk.Label(master=window, text="Or enter amount👇")
ent_account = tk.Entry(master=window)
btn_deposit = tk.Button(master=window, text="Deposit")
btn_withdraw = tk.Button(master=window, text="Withdraw")
btn_balance = tk.Button(master=window, command=account_balance, text="Check Balance")
lbl_pin = tk.Label(master=window, text="Enter Pin:")
ent_pin = tk.Entry(master=window)
btn_pin = tk.Button(master=window, text="Confirm")


frame.grid(row=0, column=0)
lbl_user.grid(row=0, column=1)
ent_user.grid(row=0, column=2)
lbl_pass.grid(row=1, column=1)
ent_pass.grid(row=1, column=2)
btn_lgb.grid(row=2, column=2)
lbl_lnk.grid(row=3, column=1)
btn_crt.grid(row=3, column=2)
lbl_account.grid(row=4, column=1)
savings_radio.grid(row=5, column=1)
current_radio.grid(row=6, column=1)
lbl_trans.grid(row=7, column=1)
deposit_radio.grid(row=8, column=1)
withdraw_radio.grid(row=9, column=1)
lbl_amount.grid(row=10, column=1)
th_radio.grid(row=11, column=1)
th2_radio.grid(row=12, column=1)
th3_radio.grid(row=13, column=1)
th4_radio.grid(row=14, column=1)
th5_radio.grid(row=11, column=2)
th6_radio.grid(row=12, column=2)
th7_radio.grid(row=13, column=2)
th8_radio.grid(row=14, column=2)
lbl_ent.grid(row=15, column=1)
ent_account.grid(row=16, column=1)
btn_deposit.grid(row=17, column=1)
btn_withdraw.grid(row=18, column=1)
btn_balance.grid(row=19, column=1)
lbl_pin.grid(row=20, column=1)
ent_pin.grid(row=20, column=2)
btn_pin.grid(row=21, column=2)


window.mainloop()
