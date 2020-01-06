import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#set target url
my_url = 'https://www.nike.com/ca/t/sportswear-club-fleece-pullover-hoodie-32Tm3L/BV2654-063'

#open browser with the URL
uClient = uReq(my_url)

#store the html page
page_html = uClient.read()

#close the webclient
uClient.close()

#parse the html, using the soup function
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "colorway-container d-sm-ib d-lg-tc pr1-sm css-1eouwf2"})


product = containers[0]
productLink = product.a["href"]
productName = product.a.img["alt"]



#print(price.div.div)
#productPrice = []

filename = 'products.csv'
f = open(filename, "w")

headers = "Nike Hoodie Color, Product Price, Product Link\n"
f.write(headers)

for product in containers:
	productLink = product.a["href"]
	productName = product.a.img["alt"]
	

	uClient = uReq(productLink)
	productPage = uClient.read()
	uClient.close()

	product_Soup = soup(productPage, "html.parser")
	priceContainer = product_Soup.find("div", {"class": "headline-baseline-base ta-sm-r css-1122yjz"})
	
	for price in priceContainer:
		productPrice = price.div.text
		#print(price.div.text)

	#print(productLink)
	#print(productName)
	#print(productPrice)
	#print("\n")
	f.write(productName + "," + productPrice + "," + productLink + "\n")

f.close()

