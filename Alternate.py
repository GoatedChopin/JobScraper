# import module
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


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
    return (soup)


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
    return (result_1)


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
    return (res)


def get_salary(soup):
    pass


# find the html tag, convert to yearly salary estimate if hourly, return yearly salary
# metadata salary-snippet-container
# id="coinfp-estimatedSalaries-panel" class="mpci-ckbdw4 eu4oa1w0"


def traverse_job_cards(driver, url):

    driver.get(url)
    # driver.find_element(By.CLASS_NAME, "icl-CloseButton vjs-x-button-close").click()
    mosaic_zone = driver.find_element(By.ID, "mosaic-provider-jobcards")
    jobElements = mosaic_zone.find_elements(By.TAG_NAME, "a")
    
    for child in jobElements:
        scrapeData(driver, child)


def scrapeData(driver, element):

    # print(element.text)
    url = element.get_attribute("href")
    
    job_dict = {"url": url}
    
    # Open a new window
    driver.execute_script("window.open('');")
    
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    
    try:
        salary_range = driver.find_element(By.CLASS_NAME, "icl-u-xs-mr--xs").text
        print(salary_range)

    except:
        print("Page wasn't good")
    
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # close the active tab


# Potentially important html components:
# <div class="jobsearch-JobComponent-embeddedHeader"><div class=""><div><div class="jobsearch-JobInfoHeader-title-container "><h1 class="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded">Entry level Python Developer<span class="visually-hidden"> - job post</span></h1></div><div class="jobsearch-CompanyInfoWithoutHeaderImage"><div><div class="icl-u-xs-mt--xs is-embedded jobsearch-JobInfoHeader-subtitle icl-u-xs-mb--md"><div class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs icl-u-xs-mb--md"><div class="icl-u-lg-mr--sm icl-u-xs-mr--xs">Cyber Wave LLC</div></div><div>Remote<span class="jobsearch-JobInfoHeader-bullet">•</span>Remote</div></div></div></div></div><div class="jobsearch-JobMetadataHeader-item "><span class="jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs">Full-time</span></div><div class="jobsearch-EmployerActivity-container icl-u-xs-mt--xs icl-u-textColor--secondary">Employer actively reviewed job 1 day ago</div><div id="employerResponsiveContainer" class="jobsearch-EmployerResponsive"><div class="jobsearch-EmployerResponsive-content"><span class="jobsearch-EmployerResponsive-icon"></span><div class="jobsearch-EmployerResponsive-description">Responded to 51-74% of applications in the past 30 days, typically within 10 days.</div></div></div><div class="icl-Grid icl-Grid--gutters"><div id="jobsearch-ViewJobButtons-container" class="jobsearch-ViewJobButtons-container is-embedded icl-Grid-col icl-u-xs-span12 icl-u-xs-textCenter icl-u-lg-textLeft"><div id="mosaic-aboveViewjobButtons" class="mosaic-zone"></div><div class="jobsearch-ButtonContainer-inlineBlock icl-u-lg-inlineBlock jobsearch-indeedApplyButton-bottomMargin"><div id="indeedApplyButtonContainer" class="jobsearch-IndeedApplyButton"><span class="indeed-apply-widget" id="indeedApplyWidget" data-indeed-apply-apitoken="aa102235a5ccb18bd3668c0e14aa3ea7e2503cfac2a7a9bf3d6549899e125af4" data-indeed-apply-jobtitle="Entry level Python Developer" data-indeed-apply-jobid="825b90f1b1d37c0f7c15" data-indeed-apply-joblocation="Remote" data-indeed-apply-jobcompanyname="Cyber Wave LLC" data-indeed-apply-joburl="https://www.indeed.com/viewjob?jk=ba6706bafd034a75" data-indeed-apply-questions="iq://825b90f1b1d37c0f7c15?v=1" data-indeed-apply-posturl="http://muffit/process-indeedapply" data-indeed-apply-coverletter="optional" data-indeed-apply-phone="optional" data-indeed-apply-resume="required" data-indeed-apply-advnum="4839297484925969" data-indeed-apply-nobuttonui="true" data-indeed-apply-pingbackurl="https://gdc.indeed.com/conv/orgIndApp?co=US&amp;vjtk=1fpabha4rqelf800&amp;jk=ba6706bafd034a75&amp;mvj=0&amp;acct_key=2502e2201453d4c1&amp;tk=1fpa6dnjmochh801&amp;trk.origin=jobsearch&amp;vjfrom=vjs&amp;astse=53df91b501b643bd&amp;assa=5003" data-indeed-apply-onappliedstatus="_updateIndeedApplyStatus" data-indeed-apply-onready="_onButtonReady" data-indeed-apply-jk="ba6706bafd034a75" data-indeed-apply-clickhandler="window.top.postMessage({eventType: 'click'}, '*')" data-indeed-apply-dismisshandler="window.top.postMessage({eventType: 'dismiss'}, '*')" data-indeed-apply-inpageapplyhandler="window.top.postMessage({eventType: 'inpageapply'}, '*')" data-indeed-apply-onclose="indeedApplyHandleModalClose" data-indeed-apply-onapplied="indeedApplyHandleApply" data-indeed-apply-oncontinueclick="indeedApplyHandleModalClose" data-indeed-apply-onclick="indeedApplyHandleButtonClick" data-acc-payload="1,2,22,1,144,1,552,1,3648,1,4392,1" data-indeed-apply-recentsearchquery="{&quot;what&quot;:&quot;Python&quot;,&quot;where&quot;:&quot;New York, NY&quot;}"><div class="icl-u-lg-hide is-embedded" data-reactroot=""><button class="icl-Button icl-Button--branded icl-Button--lg icl-Button--block icl-Button--block" buttonsize="block" id="indeedApplyButton" type="button"><div class="jobsearch-IndeedApplyButton-contentWrapper"><span class="jobsearch-IndeedApplyButton-newDesign">Apply now</span></div></button></div><div class="jobsearch-IndeedApplyButton-buttonWrapper icl-u-lg-block icl-u-xs-hide" data-reactroot=""><button class="icl-Button icl-Button--branded icl-Button--lg icl-Button--block icl-Button--md" buttonsize="md" id="" type="button"><div class="jobsearch-IndeedApplyButton-contentWrapper"><span class="jobsearch-IndeedApplyButton-newDesign">Apply now</span></div></button></div></span></div></div><div id="saveJobButtonContainer" class="icl-u-lg-inlineBlock"><div class=""><div aria-live="assertive"><div><div class="icl-u-lg-hide"><button class="icl-Button icl-Button--secondary icl-Button--lg icl-Button--block" type="button" aria-label="" aria-haspopup="true" aria-expanded="false"><span class="icl-ButtonIcon"><svg role="img" class="icl-Icon icl-Icon--inheritColor icl-Icon--sm" aria-label="save-icon" focusable="false" viewBox="0 0 18 18"><g><path d="M12.38,2.25A4.49,4.49,0,0,0,9,3.82,4.49,4.49,0,0,0,5.63,2.25,4.08,4.08,0,0,0,1.5,6.38c0,2.83,2.55,5.15,6.41,8.66L9,16l1.09-1C14,11.52,16.5,9.21,16.5,6.38A4.08,4.08,0,0,0,12.38,2.25ZM9.08,13.91L9,14l-0.08-.08C5.35,10.68,3,8.54,3,6.38A2.56,2.56,0,0,1,5.63,3.75,2.93,2.93,0,0,1,8.3,5.52H9.7a2.91,2.91,0,0,1,2.67-1.77A2.56,2.56,0,0,1,15,6.38C15,8.54,12.65,10.68,9.08,13.91Z"></path></g></svg></span><span></span></button></div><div class="icl-u-lg-block icl-u-xs-hide"><button class="icl-Button icl-Button--secondary icl-Button--md icl-Button--block" type="button" aria-label="" aria-haspopup="true" aria-expanded="false"><span class="icl-ButtonIcon"><svg role="img" class="icl-Icon icl-Icon--inheritColor icl-Icon--sm" aria-label="save-icon" focusable="false" viewBox="0 0 18 18"><g><path d="M12.38,2.25A4.49,4.49,0,0,0,9,3.82,4.49,4.49,0,0,0,5.63,2.25,4.08,4.08,0,0,0,1.5,6.38c0,2.83,2.55,5.15,6.41,8.66L9,16l1.09-1C14,11.52,16.5,9.21,16.5,6.38A4.08,4.08,0,0,0,12.38,2.25ZM9.08,13.91L9,14l-0.08-.08C5.35,10.68,3,8.54,3,6.38A2.56,2.56,0,0,1,5.63,3.75,2.93,2.93,0,0,1,8.3,5.52H9.7a2.91,2.91,0,0,1,2.67-1.77A2.56,2.56,0,0,1,15,6.38C15,8.54,12.65,10.68,9.08,13.91Z"></path></g></svg></span><span></span></button></div></div></div></div></div><div id="mosaic-belowViewjobButtons" class="mosaic-zone"><div class="mosaic mosaic-provider-acme-survey-collection mosaic-rst mosaic-provider-hydrated" id="mosaic-provider-acme-survey-collection"></div></div><div class="mosaic mosaic-provider-jobsearch-feedback" id="mosaic-provider-jobsearch-feedback"></div></div></div><div id="saveJobInlineCalloutContainer" class="icl-u-lg-block icl-u-lg-mt--md"></div></div><span></span><object style="display: block; position: absolute; top: 0; left: 0; height: 100%; width: 100%; overflow: hidden; pointer-events: none; z-index: -1;" id="resizeListener" tabindex="-1" type="text/html" data="about:blank" aria-hidden="true"></object></div>
# /html/head/meta[9]

def build_search_url(keyword, city="", state=""):
    if city == "":
        url = r"https://www.indeed.com/q-" + keyword + r"-jobs.html"
    else:
        if state in us_state_to_abbrev.keys():
            state = us_state_to_abbrev[state]
        
        # https://www.indeed.com/q-Python-l-Austin,-TX-jobs.html
        # url = r"https://in.indeed.com/jobs?q=" + keyword + r"&l=" + city + r"%2C%20" + state
        url = r"https://www.indeed.com/q-" + keyword + r"-l-" + city + r",-" + state + r"-jobs.html"
    print(url)
    return (url)


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

languages = ["Python", "Java", "Javascript", "C", "C++", "PHP", "R", "Objective-C", "Swift", "TypeScript", "Matlab", "Kotlin", "Go", "VBA", "Ruby", "Rust", "Ada", "Dart", "Abap", "Visual Basic", "Scala", "Groovy", "Lua", "Perl", "Haskell", "Julia", "Cobol"]

# driver nodes/main function
if __name__ == "__main__":
    
    df = pd.read_csv("MajorCities.csv")

    s=Service(r"C:\Users\Colby\Documents\GitHub\JobScraper\.idea\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    
    driver.implicitly_wait(5)
    
    # Data for URL
    job = "Python"
    city = "Austin"
    state = "Texas"
    
    # for language in languages:
    #     for i in range(100):
    #         city = df["city"][i]
    #         state = df["state"][i]
    #         # print(city + ", " + us_state_to_abbrev[state] + " has a population of "  + str(df["population"][i]))
    #         url = build_search_url(keyword = language, city = city, state = state)
    #         # driver.get(url)
    
    url = build_search_url(job, city, state)
    traverse_job_cards(driver, url)
    
    
    # Pass this URL into the soup
    # which will return
    # html string
    soup = html_code(url)

