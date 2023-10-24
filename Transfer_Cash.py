def transfer_cash():
    sender_account_no=input("Enter your account number:")
    pin=input("Enter your PIN:")
    
    if sender_account_no in user:
        if pin==pin:
            receiver_account_no=input("Enter the receivers account number:")
            if receiver_account_no in user:
                amount=float(input("Enter the amount to transfer: "))
                
                if amount <=user[sender_account_no]:
                    user[sender_account_no]-=amount
                    user[receiver_account_no]+=amount
                    
                    print("Transfer Successfully Done!!!")
                    print(f'Your new balance:${sender[sender_account_no]:.2f}')
                else:
                    print("Insufficient Balance.")
            else:
                print("Receivers account does not exist.")
        else:
            print("Incorrect PIN.")
    else:
        print("Account not found.")
                    