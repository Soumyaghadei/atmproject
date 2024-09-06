from ATMMenu import menu
from ATMOperations import deposite,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposite() # Function Call
                except DepositError:
                    print("\tDon't try to Deposit -VE and Zero Amount")
                except ValueError:
                    print("\tDon't try to Deposit alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("\tDon't try to Withdraw -VE and Zero Amount")
                except InSuffFundError:
                    print("\tUr Account does not have funds--Read Python Notes")
                except ValueError:
                    print("\tDon't try to Withdraw alnums,strs and symbols")
            case 3:
                balenq()
            case 4:
                print("Thx for Using Program")
                break
            case _:
                print("Ur Selection of Operations is wrong-try again")
    except ValueError:
        print("\tDon't enter strs,alnums,symbols for Choice of Ints")