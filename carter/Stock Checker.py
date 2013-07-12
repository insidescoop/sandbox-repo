# Stock Checker
# The purpose of this program is to test if stock price is a fair value.

# get inputs
name=input("Name of Company")
price=input("Stock Price")
date=input("Date")
lEPS=input("Last Year EPS")
fEPS=input("Estimated EPS")
marketcap=input("Market Cap")


# do calculations
PE=int(price)/int(lEPS)
growth=(int(fEPS)-int(lEPS))/int(lEPS)*100
PEG=(int(PE)/int(growth))

print("PEG Ratio = ", PEG)


# display results 
if PEG==1:
    print ("Fair Value")
elif PEG>1:
    print ("Hold")
elif PEG>2:
    print ("Sell")
elif PEG<1 and PEG>0:
    print ("Buy")	
else:
    print ("Sell since PEG is negative")
