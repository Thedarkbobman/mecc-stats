from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect('database.db')

r = requests.get('https://www.sunnyportal.com/Templates/PublicPage.aspx?page=1e5855c0-b7c1-4b96-8e77-533a0dc07111')
r.encoding='utf-8'

print(r.text.encode('ascii', 'ignore'))
soup = BeautifulSoup(r.text.encode('ascii', 'ignore'), 'html.parser')

print(soup.prettify())
imageUrl = soup.find("img", { "id" : "ctl00$ContentPlaceHolder1$PublicPagePlaceholder1$PageUserControl$ctl00$UserControl1$_diagram" })["src"]
print(imageUrl)
dateString = soup.find("input", { "name" : "ctl00$ContentPlaceHolder1$PublicPagePlaceholder1$PageUserControl$ctl00$GlobalDatePicker$textBox" })["value"]
print(dateString)

# c = conn.cursor()

# # Create table
# c.execute('''CREATE TABLE day_graphs
#              (date text, url text, type text)''')

# # Insert a row of data
# c.execute("INSERT INTO day_graphs VALUES (dateString,'BUY','RHAT'")

# # Save (commit) the changes
# conn.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()