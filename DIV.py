no=input("Enter no.")

no=int(no)

if no%3 == 0 and no%5 == 0:
    print("Div by both")
elif no%3 == 0:
    print("Div by 3")
elif no%5 == 0:
    print("Div by 5")
else:
    print("Not div by 3 and 5")