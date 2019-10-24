from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from buildYoutube import getData

#Path where the driver exists
path = ".\\chromedriver.exe"#Enter the path where you have saved the driver
driver = webdriver.Chrome(path)
baseUrl = "https://www.youtube.com/channel/"

def extractData():

    data = getData()#call the getData function from buildYoutube file
    channelIdList = data['channelId']#Extract the list of channelids from the data dictionary
    subscriberCountList = []
    imgSrcList = []
    infoDict = {}

    for channelId in channelIdList:

        driver.get(baseUrl + channelId)
        subCount = driver.find_element_by_id('subscriber-count')#subscriber-count id contains number of subscribers for the particular channel
        subscriberCountList.append(subCount.text)

        imgId = driver.find_element_by_id('img')#this id contains the channels' image
        imgSrc = imgId.get_attribute('src')#src contains the link of the channels' image
        imgSrcList.append(imgSrc)

    #Add all this data to infoDict dictionary which will be displayed in the app.py file
    infoDict['subscriberCount'] = subscriberCountList
    infoDict['imgSrc'] = imgSrcList
    infoDict['channelTitles'] = data['channelTitle']
    infoDict['channelIdList'] = data['channelId']
    driver.quit()

    return infoDict