Exercise 229 - Regular Expressions
Write code on line 5 in order to replace all the digits less than or equal to 5 in the string with 8 using the sub() method.

import re
 
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
 
result = re.sub(r"[0-5]", "8", s)
 
print(result)
