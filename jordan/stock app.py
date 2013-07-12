# stock checker
# the purpose of this program is to determine if the stock price is at a fair value.
# get inputs from user
name=input("Name of company: ")
price=input("Price of stock: ")
date=input("Current date: ")
lEPS=input("Last year EPS: ")
fEPS=input("Future estimated EPS: ")
marketcap=input("Market cap: ")
# do calculations
PE=int(price)/int(lEPS)
growth=(int(lEPS)-int(fEPS))/int(lEPS) * 100
PEG=(int(PE)/int(growth))
# display results
if PEG==1:
    print ("Fair value")
elif PEG<1:
    print ("Buy")
elif PEG>1:
    print ("Hold")
else:
    print ("Sell")