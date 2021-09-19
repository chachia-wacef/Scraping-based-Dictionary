from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import wget
import json 
import time
from bs4 import BeautifulSoup
import requests


#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Windows/chromedriver.exe', chrome_options=chrome_options)


#######################################  Scrap the list of languages #######################################
url_list = 'https://cloud.google.com/translate/docs/languages'
#Extract Information
website = requests.get(url_list)
soup = BeautifulSoup(website.text, 'html.parser')

#Extract languages and their codes
lgs = soup.find_all('td')
languages = []
codes = []
for elt in lgs:
    elt1 = str(elt)
    if 'translate' in elt1:
        if len(elt.text) > 2:
            code = elt.text.split()[0]
            codes.append(code)
        else:
            codes.append(elt.text)
    else:
        languages.append(elt.text.lower())

print(len(languages))
print('+++++++++++++++++++++++++++')
print(len(codes))

if len(languages) == len(codes):
    lgs_dict = {}
    for k in range(len(languages)):
        lgs_dict[languages[k]] = codes[k]

'''
#Now , we will convert this list of lists into json file. 
with open("C:/Users/hp/Desktop/Dictionary_Project/Languages.json", "w" ,encoding='ascii') as file:
    json.dump(lgs_dict, file)

file.close()
'''



############################################  Open Google Translate  ###################################################
url_1 = "https://translate.google.com/?hl=fr&sl="
url_2 = "&tl="
url_3 = "&op=translate"

lg1 = 'English'
lg2 = 'French'

text_tr = 'hello world, im wacef from tunisia'

#Cases
#First case : we know the language of our text
#Second case : we don't know the language of our text so google will detect the language and tell us

if ((lg1 != None)&(lg2 != None)):
    lg1_code = lgs_dict[lg1]
    lg2_code = lgs_dict[lg2]

    url = url_1 + lg1_code + url_2 + lg2_code + url_3

    #open the webpage of Google Translation
    driver.get(url)

    #target input text
    input_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-label='Texte source']")))

    #enter input text
    input_text.clear()
    input_text.send_keys(text_tr)

    time.sleep(2)

    outs = driver.find_elements_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
    for out in outs:
        output_text = out.text
        print("*******")
        print(output_text)
    
