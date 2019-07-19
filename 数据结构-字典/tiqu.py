prices = {'ASP.NET':49.9, 'Python':69.9, 'Java':59.9, 'C':45.9, 'PHP':79.9}
p = {key:value for key,value in prices.items() if value > 50}
print(p)