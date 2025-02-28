# in this second tutorial we will learn how to scrap a website using beautifulsoup library



# this library provides a simple methods  it automatically  converts incoming records to unicode and outgoing form to UTF-8 


import requests



from bs4 import BeautifulSoup



# making a get request




r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')

print(r)



soup=BeautifulSoup(r.content,'html.parser')


print(soup.prettify())


