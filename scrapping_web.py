# web scraping using python 


# step 1 : import the required libraries 

# step2:get the url that you want to scrape 


# step 3: download the html content of the web page


# step4: parse the html content

# step5: extract the data that you need


# step 6: store the data in the required format 



import requests


#making a get request




r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')



# check the status code of the request 

# success code-200


print(r)



print(r.content)


