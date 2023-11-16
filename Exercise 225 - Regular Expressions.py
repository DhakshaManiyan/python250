Exercise 225 - Regular Expressions
Write code on line 5 in order to match all the words starting with a or c and that have at least 3 letters in the string using the findall() method.

import re
 
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
 
result = re.findall(r"\s([ac]\w{2,})\s", s)
 
print(result)
