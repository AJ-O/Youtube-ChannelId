from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from buildYoutube import getData


path = "C:\\WebDrivers\\chromedriver.exe"
driver = webdriver.Chrome(path)
baseUrl = "https://www.youtube.com/channel/"

def extractData():

    data = getData()
    channelIdList = data['channelId']
    subscriberCountList = []
    imgSrcList = []
    infoDict = {}

    for channelId in channelIdList:

        driver.get(baseUrl + channelId)
        subCount = driver.find_element_by_id('subscriber-count')
        subscriberCountList.append(subCount.text)

        imgId = driver.find_element_by_id('img')
        imgSrc = imgId.get_attribute('src')
        imgSrcList.append(imgSrc)

    infoDict['subscriberCount'] = subscriberCountList
    infoDict['imgSrc'] = imgSrcList
    infoDict['channelTitles'] = data['channelTitle']
    infoDict['channelIdList'] = data['channelId']
    
    return infoDict
