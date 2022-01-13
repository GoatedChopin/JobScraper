# import module
import requests
from bs4 import BeautifulSoup
import pandas as pd

# user define function
# Scrape the data
# and get in string
def getdata(url):
	r = requests.get(url)
	return r.text

# Get Html code using parse
def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# return html code
	return(soup)

# filter job data using
# find_all function
def job_data(soup):
	
	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	for item in soup.find_all("a", class_="jobtitle turnstileLink"):
		data_str = data_str + item.get_text()
	result_1 = data_str.split("\n")
	return(result_1)

# filter company_data using
# find_all function


def company_data(soup):

	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	result = ""
	for item in soup.find_all("div", class_="sjcl"):
		data_str = data_str + item.get_text()
	result_1 = data_str.split("\n")

	res = []
	for i in range(1, len(result_1)):
		if len(result_1[i]) > 1:
			res.append(result_1[i])
	return(res)

def get_salary(soup):
  
  # find the html tag, convert to yearly salary estimate if hourly, return yearly salary
  # metadata salary-snippet-container
  # id="coinfp-estimatedSalaries-panel" class="mpci-ckbdw4 eu4oa1w0"

def build_search_url(keyword, city = "", state = ""):
  
  if location == "":
    url = "https://in.indeed.com/jobs?q="+keyword
  else:
    if state in us_state_to_abbrev.keys:
	state = us_state_to_abbrev[state]
    url = "https://in.indeed.com/jobs?q="+keyword+"&l="+city+"%2C%20"+state
  return(url)

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

# driver nodes/main function
if __name__ == "__main__":

	# Data for URL
	job = "Python"
	location = ""
	url = build_search_url(keyword = job)

	# Pass this URL into the soup
	# which will return
	# html string
	soup = html_code(url)

	# call job and company data
	# and store into it var
	job_res = job_data(soup)
	com_res = company_data(soup)

	# Traverse the both data
	temp = 0
	for i in range(1, len(job_res)):
		j = temp
		for j in range(temp, 2+temp):
			print("Company Name and Address : " + com_res[j])

		temp = j
		print("Job : " + job_res[i])
		print("-----------------------------")
