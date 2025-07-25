#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

cossprice=float(input("Inter the buyying price"))
sellingprice=float(input("Enter the seelling price"))
if sellingprice>cossprice:
    print("You are at a profit of ",sellingprice-cossprice)
else:
    print("Sorry you are at a loss of",cossprice-sellingprice)