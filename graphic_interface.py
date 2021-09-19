import tkinter as tk
import ctypes
import json
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

##Config##
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Windows/chromedriver.exe', chrome_options=chrome_options)
####

with open('C:/Users/hp/Desktop/Dictionary_Project/Languages.json', 'r') as f:
    json_dict = json.load(f)
lgs = dict(json_dict)

lgs_list = []
for key, value in json_dict.items():
    lgs_list.append(key)

def Translate_text(in_text,lg1,lg2):
    #Urls
    url_1 = "https://translate.google.com/?hl=fr&sl="
    url_2 = "&tl="
    url_3 = "&op=translate"
    ##
    
    if ((len(in_text) > 0 )& (in_text != 'Enter your text' )&(lg1 in lgs_list)&(lg2 in lgs_list)):

        if ((lg1 != None)&(lg2 != None)):
            lg1_code = lgs[lg1]
            lg2_code = lgs[lg2]
            url = url_1 + lg1_code + url_2 + lg2_code + url_3
            #open the webpage of Google Translation
            driver.get(url)
            #target input text
            input_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-label='Texte source']")))
            #enter input text
            input_text.clear()
            input_text.send_keys(in_text)

            time.sleep(2)

            outs = driver.find_elements_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
            for out in outs:
                output_text = out.text
                lbl_out['text']= output_text
    
window = tk.Tk()
window.title('Chachia Dictionary')
window.geometry("1700x100")


ent_text = tk.Entry(master = window,width=50)
ent_text.pack(side=tk.LEFT)
ent_text.insert(0,'Enter your text')

ent_lg1 = tk.Entry(master = window,width=10)
ent_lg1.pack(side=tk.LEFT)
ent_lg1.insert(1,'Language 1')

ent_lg2 = tk.Entry(master = window,width=10)
ent_lg2.pack(side=tk.LEFT)
ent_lg2.insert(2,'Language 2')

lbl_left = tk.Label(text='Input language', width=5) 
lbl_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

btn = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}",command=Translate_text(ent_text.get(),ent_lg1.get(),ent_lg2)) 
btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 

lbl_out = tk.Label(text='', width=50)
lbl_out.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lbl_right = tk.Label(text='Output language')
lbl_right.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

window.mainloop()