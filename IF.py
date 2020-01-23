def ComInt():
    # Calculating of compound interest by years
    r = int(input("Enter your interest rate: "))
    PV = int(input("Enter your inital deposit: "))
    t = int(input("Enter the number of time intervals: "))
    FV = PV * (1 + (r/100))**t
    print(FV)
def SimInt():
    # Calculating of simple interest 
    PV = int(input("Enter your inital deposit: "))
    r = int(input("Enter your interest rate: "))
    t = int(input("Enter the number of time intervals: "))
    U = PV * (r/100) * t
    print(U)
