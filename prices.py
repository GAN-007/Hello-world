

def getInclusive(prices,vat):
    
    for price in prices:
        # if prices.index(price) < len(prices):
            vatamount=price*vat
            incprice=price+vatamount
            print(incprice)
 
        


getInclusive([222,333,444],0.16)
       