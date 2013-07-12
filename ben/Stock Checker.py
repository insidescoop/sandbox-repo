# Stock Checker 
# The purpose of this program is to determine is the stock price is of fair value
# Get inputs
name=input("Name of company= ")
price=input("Price of stock: ")
date=input("Current date: ")
lEPS=input("Last year EPS: ")
fEPS=input("Future EPS: ")
MarketCap=input("Market cap: ")


# Do calculations 
PE=(int(price)/int(fEPS))
print (PE)
growth=((int(fEPS)-int(lEPS))/int(lEPS))*100
print (growth)
PEG=(int(PE)/int(growth))
print ("PEG ratio = ", PEG)

# Display result
if PEG==1:
    print ("Fair Value")
elif PEG<1 and PEG>0:
    print ("Buy")
elif PEG>1:
    print ("Hold")
else:
    print ("Sell") 