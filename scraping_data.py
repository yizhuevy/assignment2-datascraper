import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

# Fill out the form
br.select_form (nr=0)


br.form['ctl00$MainContent$cboRaces'] = ["460006719"]


# Submit the form - clarify which submit button
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
    {'id': 'MainContent_dgrdCountyRaceResults'}
)

# Get the output file ready
output = open('scraper.csv', 'w')
writer = csv.writer(output)

# Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text.encode('utf-8') for cell in row.find_all({'td','th'})]
    writer.writerow(data)
