from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00
def deposite():
    dmat=float(input("Enter your deposite amount:"))
    if(dmat<=0):
        raise DepositError
    else:
        global bal
        bal=bal+dmat
        print("Ur Account xxxxxxxxx123 Credited with INR:{}".format(dmat))
        print("Now Ur Account xxxxxxxxx123 Bal after Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Ur Withdraw Amount:"))
    if(wamt<=0):
        raise WindowsError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxxxxx123 Bal after withdraw INR:{}".format(bal))

def balenq():
    print("Now Ur Account xxxxxxxxx123 Bal INR:{}".format(bal))
