##################################################################################
#\                      Lin-Odikko V1.0 - 29/9/2018                             \#
#\          Created By Subin Varghese [www.5ub.in]                 		 \#
#\                        ❤ with Python & Life                                 \#
#\                                                                              \#
##################################################################################
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import re
import os
import getpass
import random

print("""\
    __    _             ____      ___ __   __       
   / /   (_)___        / __ \____/ (_) /__/ /______ 
  / /   / / __ \______/ / / / __  / / //_/ //_/ __ \
 / /___/ / / / /_____/ /_/ / /_/ / / ,< / ,< / /_/ /
/_____/_/_/ /_/      \____/\__,_/_/_/|_/_/|_|\____/                                              
..... (¯`v´¯)♥---- Version 1.0 © www.5ub.in // Date:29/9/18 -------------------------
.......•.¸.•´
....¸.•´    
... (  This 4 U, My Love!!!    
 ☻/
/▌♥♥
/ \ ♥♥ 
                    """)

email = input("[?] Enter your account email: ")
password = getpass.getpass("[?] Enter your account password: ") # Pedikenda Its Secure!!!
no_of_profiles = int(input("[?] Enter how many LinkedIn profiles you wish to view? (Approx): "))
keyword = input("[?] Enter your search term: ")
inv = input("[?] Sent invites to them? (*Beta) [Y/N]: ")
feedpg = input("[?] Start viewing from homepage? [Y/N]: ")

# We need to scrap some pages out of it
def churandi():
    # Churandi edukenda page
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    page_urls = []
    for url in soup.find_all('a'):
        page_urls.append(str(url.get('href')))
    return page_urls
# Create a tracking page for the given keyword
if(os.path.exists("Data/Query Page/" + keyword) is False):
    with open("Data/Query Page/" + keyword, "w") as text_file:
        text_file.write("1")
# Read from search query page file to determine what pages already viewed
with open("Data/Query Page/" + keyword, "r") as text_file:
    i = int(text_file.read())


			
print("[+] Starting up Mozilla Firefox in auto mode")			
page_max = round(no_of_profiles/10) + i

# Instance of the Firefox driver // Ithokke Onnu Odikende
driver = webdriver.Firefox()

# Navigate to LinkedIn login page and log in
driver.get('https://linkedin.com/uas/login')
emailElement = driver.find_element_by_id('session_key-login')
emailElement.send_keys(email)
passElement = driver.find_element_by_id('session_password-login')
passElement.send_keys(password)
passElement.submit()
time.sleep(random.uniform(2.5,6.5))
print("[+] Success! Logged In, Bot Starting... Scrolling Now!")
scl = 100
for ab in range(1,50):
    driver.execute_script("window.scrollTo(0, 100 + 50 * " +str(ab)+")")
    time.sleep(random.uniform(0.1,0.9))

# Ethhi nokenda profiles ivide save cheyunnu
profile_urls_storage = []
while i <= page_max:

# Home Feed or Search Page    
    if feedpg in ["Y","y"]:
        print("[+] Loading Home Feed...")
        feedpage= "https://www.linkedin.com/feed/"
        driver.get(feedpage)
        feedpg = "N"
    else: 
        print("[+] Loading Search Page...")
        search_page_url = "https://www.linkedin.com/search/results/people/v2/?keywords=" + keyword + "&page=" + str(i)# + "&title=" + keyword
        print("[+] Searching Key = " + keyword + " & Page = " + str(i))
        driver.get(search_page_url)
		
		
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i += 1
    time.sleep(2)
    urls_on_search_page = churandi()
    for url in urls_on_search_page:
        if ("/in/" in url):
            if url not in profile_urls_storage:
                profile_urls_storage.append(url)

    
    print("[+] We Are Ready 2 Go! " + str(len(profile_urls_storage)) + " profiles to visit!")
#Looping in through Namude swantham ppls
num_profiles_visited = 0
for url in profile_urls_storage:
    driver.get("https://www.linkedin.com" + url)
    print ("[+] Visiting: " + url)
    time.sleep(2 + 1 * i)

    #Invitation Senting Section. *Beta work.    
    if inv in ["Y","y"]:
        invnum = random.randint(0,100)
                
        if (invnum % 2 == 0):
            print("[+] Sending Random Invite to : " + str(url))
            #Error may occur if connect button is not display. Njanille muthe ithinokke exception kodukkan
            try: 
                driver.execute_script("document.getElementsByClassName('pv-s-profile-actions pv-s-profile-actions--connect button-primary-large mr2 mt2')[0].click();")
                time.sleep(1)
                driver.execute_script("document.getElementsByClassName('button-primary-large ml1')[0].click();")
                print("[+] Invite Sent")
                time.sleep(random.uniform(0.5,1.5))
                driver.execute_script("window.history.go(-1)")
                time.sleep(random.uniform(1.5,3.5))
            except JavascriptException:
                print("[!] Invite Not Sent. Java Script Error")
                pass    

   
    driver.execute_script("window.scrollTo(0, 200 + 100 * " +str(i)+")")
    time.sleep(random.uniform(1.5,5.5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5 + 2 * i)
    num_profiles_visited += 1
    driver.execute_script("window.history.go(-1)")
    time.sleep(random.uniform(2,3.5))

print("[+] Visited", num_profiles_visited, "profiles")
print("[#] Thank You... Exiting...")
driver.quit()

# Write to query page file to keep track of how many pages viewed
with open("Data/Query Page/" + keyword, "w") as text_file:
    text_file.write(str(i))
