# ----------------------------
# Stock Fair Value Calculator
#
#  version:  Python 3.x
# ----------------------------
import time

KLARGECAP=1000
KMEDIUMCAP=500
KSMALLCAP=200

companySize = ["large", "medium", "small"]
KLARGE=0
KMEDIUM=1
KSMALL=2

action = ["Buy", "Hold", "Sell"]
KBUY=0
KHOLD=1
KSELL=2

print("---------------------------")
print("Stock Fair Value Calculator")
print("---------------------------\n")
print(time.strftime('%m/%d/%Y'))

# Get inputs (ticker, date, price, previous EPS, est EPS, market cap)
name = input("Name of company: ")
ticker = input("Enter ticker symbol: ")
today = input("Today's date: ")
price = input("Current stock price: ")
lastYearEPS = input("Earnings per share (EPS) for last fiscal year: ")
estEPS = input("Estimated earnings per share (EPS) for current fiscal year: ")
marketCap = input("Company's market capitalization: ")

# Processing
growthRate = (int(estEPS) - int(lastYearEPS)) / int(lastYearEPS) * 100

# Calculate PE value
pe = (int(price)/int(lastYearEPS))

# Determine company size
if int(marketCap) > KLARGECAP:
    companySizeType = KLARGE
elif int(marketCap) <= KSMALLCAP:
    companySizeType = KSMALL
else:
    companySizeType = KMEDIUM

# Calculate fair value based on PEG ratio and company size
if int(growthRate) > pe:
    currentValue = "undervalued"
    recommendation = action[KBUY]
elif int(growthRate) == pe:
    currentValue = "fairly valued"
    recommendation = action[KHOLD]
else:
    currentValue = "overvalued"
    recommendation = action[KSELL]


# Output results
print("\n")
print("Result of Analysis")
print("------------------")
print(name, "is a", companySize[companySizeType], "company with a growth rate of", growthRate, "%")
print("It has a P/E value of", pe)
print("At the current price of ", price, ", ", ticker, " is ", currentValue, sep='')
print("\n")
print("Recommendation:", recommendation)


