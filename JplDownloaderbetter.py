import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
import pyautogui


PATH = "/Users/sagarsaluja/Documents/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://members.jamplay.com/lessons/artist-series")

search = driver.find_element_by_id("username")  
search.send_keys("sagarsaluja1998@gmail.com")
search = driver.find_element_by_id("password")
search.send_keys("JamPlayPassword")
search = driver.find_element_by_class_name("login-btn")
search.click()
Artist = driver.find_element_by_link_text("Mike Keneally")  #ARTIST NAME GOES HERE
Artist.click()

# try:
L=[]
num_lesson=20                                             #ENTER NUMBER OF LESSONS IN THE COURSE(exact number)
for i in range(num_lesson):
    l1 = driver.find_element_by_id("seriesLessons")
    xpath = '//*[@id="seriesLessons"]/div[' + str(i+1) + ']'
    l2 = l1.find_element_by_xpath(xpath)
    l3 = l2.find_element_by_tag_name("h3")
    lesson = l3.find_element_by_tag_name("a").get_attribute('href')
    L.append(lesson)
print(L)

#Loop Over lessons begins here
k=0                                                    #LESSON NUMBER -1 TO START DOWNLOADING LESSONS FROM
while(k<num_lesson):
    driver.get(L[k])
    #Video page is open now

    # video =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"video")))
    time.sleep(7)

    # number of videos on the page

    num = driver.find_element_by_xpath('//*[@id="mCSB_2"]/div[1]')
    time.sleep(1)
    number = num.find_elements_by_tag_name("li")
    time.sleep(1)
    num_vids_on_page = len(number)

    print(num_vids_on_page)

    #looping through the videos on that page and downloading each of them
    i=0
    while (i <= num_vids_on_page-1):
        time.sleep(3)
        video = driver.find_element_by_tag_name("video")
        url = video.get_attribute('src')
        video_name = str(k+1) + "_" + str(i) + ".mp4"        
        urllib.request.urlretrieve(url, video_name)
        time.sleep(3)
        if(i==num_vids_on_page):
            break
        pyautogui.click(x=356, y=455)
        i+=1
    k+=1
    driver.back()
    time.sleep(1)