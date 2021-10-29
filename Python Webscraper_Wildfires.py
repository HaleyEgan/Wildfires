"""
Python: Web Scraper from National Interagency Fire Center Website
Haley Egan
"""
from bs4 import BeautifulSoup #import BeautifulSoup to parse html and extract data 
import requests #open URL, download html and pass it to BeautifulSoup.
import csv #import to write to file
import pandas as pd #import for visualizations
import matplotlib.pyplot as plt #import for visualizations
import seaborn as sns #import for visualizations

'''
Resource Citations:
- National Interagency Fire Center: https://www.nifc.gov/fire-information/statistics/wildfires
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- csv module: https://docs.python.org/3/library/csv.html
- requests: https://docs.python-requests.org/en/latest/
- matplotlib: https://matplotlib.org/
- seaborn: https://seaborn.pydata.org/
'''

#right click "View Source" to view html code
#right click on table and select "Inspect" to see html code of specific portion of site (table)

#url of fire data for United States 
url = 'https://www.nifc.gov/fire-information/statistics/wildfires'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) #request html from url
html = response.content #raw, unformatted html from site 
#print(html)

soup = BeautifulSoup(html, 'lxml') #parse html as string 
#print(soup.prettify()) #format html to make it more readable 

#find pattern/identifier in code for elements to extract #extract table of fire data from site 
#can index because html is now string
table = soup.find_all('table')[0] #grab first table
#print(table) #check to make sure we got table 
#print(table.prettify()) #format html 

#convert rows in table to list #loop through list and get information out
list_of_rows = []
for row in table.find_all('tr'): #get list of rows using html <tr>
    #print(row.prettify()) #check to make sure we got row/format it 
    list_of_cells = [] #create empty list
    #loop through each cell in each row by selecting them inside loop. <td> in html
    for cell in row.findAll('td'): 
        #print(cell.text)
        text = cell.text.replace('&nbsp;', '') #delete '&nbsp;' = non-breaking space, at end of rows 
        text = cell.text.replace(",", '') #remove commas from numbers in data 
        list_of_cells.append(text) #append cell text to empty list 
    #structure data for csv file 
    list_of_rows.append(list_of_cells) #append cell text to rows list. makes a list of lists with all the table data
#print(list_of_rows) #check output 
list_of_rows.remove(list_of_rows[-1]) #remove extra writing at end of table
#print(list_of_rows) #check output 
list_of_rows.remove(list_of_rows[0]) #remove extra writing at beginning of table 
#print(list_of_rows) #check output 
list_of_rows.remove(list_of_rows[0]) #remove extra writing at beginning of table 
print(list_of_rows) #check output 

#create and write to csv file
outfile = open("Wildfires.csv", "w") #open, name, and write to file
writer = csv.writer(outfile) #use csv module to write to file 
writer.writerows(list_of_rows) #tool to dump out list of lists into file 

#create visualizations of data
# open and read csv file
df = pd.read_csv("Wildfires.csv")
df.head() #print first few rows of data 

#plot a histogram of frequency of fires 
df['Fires'].plot(kind='hist')
#this plott shows that the frequency of fires has increased over time

#distribution plot of fires to show density
sns.distplot(df['Fires'])
#this plot shows that the density is a bell curve shape, with less fires on
#either side, but more in the middle

#line graph to show amount of fires over time
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Year", "Fires"]
df = pd.read_csv("Wildfires.csv", usecols=columns)
#print("Contents in csv file:\n", df)
plt.plot(df.Year, df.Fires)
plt.show()
#this plot shows the number of fires per year. It appears that every other year,
#or every few years, there is a severe fire season with lots of fires, followed by a year 
#with less fires. 