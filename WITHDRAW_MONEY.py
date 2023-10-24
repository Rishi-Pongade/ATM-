def WithdrawMoney():
    askpin=int(input("Please Enter Your PIN: "))
    chkpin=(f"SELECT * FROM USER WHERE U_PIN = {askpin}")
    if chkpin == True:
        entamt=(int(input("Enter the amount You want to Withdraw: ")))
        balqry=(f"SELECT u_balance FROM USER WHERE U_PIN = {askpin} ")
        updated_bal=(balqry-entamt)
        upbalqry=("UPDATE USER SET u_balance = {updated_bal} WHERE U_PIN = {askpin}")
        print(f"Money Withdrawn Successfully\n Your Updated Nalanace is {updated_bal}")
    else:
        print("Wrong PIN!")
    