from bs4 import BeautifulSoup
import requests
import string
import csv

# ASCII charecter uppercase list
charecter = list(string.ascii_uppercase)
sum = 0

# Create an object of file
file_obj = open('squarepharma.csv', "w") # File open
# Write the Pharmaceuticals name
file_obj.write("Square Pharmaceuticals Ltd.\n\n")
# Write medicine name header
file_obj.write("Medicine Name,")
# Write Company name header
file_obj.write("Company Name\n")

print("Company ----- Medicine name --------------- Group")
print("=============================================================================")

for char in charecter:
	# URL with trade and char query params
	url = "http://www.squarepharma.com.bd/products-by-tradename.php?type=trade&char="+char
	# Get the requested URL
	req  = requests.get(url)
	# Passing the requested content to Beautiful Soup
	soup = BeautifulSoup(req.content)
	# Targeting data/html content
	data = soup.find_all("div", {"class":"products-holder"})

	for item in data:
		print("Square ----- " +item.contents[2].text+ " ----- " + item.contents[4].text)
		sum +=1 # Count total number of medicine
		print("=============================================================================")

		# Writing the medicine information into CSV file
		file_obj.write(item.contents[2].text.encode("utf-8")+',')
		file_obj.write(item.contents[4].text.encode("utf-8")+"\n")

file_obj.close() # File close
print("Total medicines :  {0}".format(sum)) # Print the total number of medicines
