import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def authorization():

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    #Authorizing the account
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials = credentials)
    
    #Using the search request of youtube api to search only channel name and maximum 3
    query = input("Enter channel name: ")
    request = youtube.search().list(part = "snippet", q = query, type = 'channel', maxResults = 3)
    response = request.execute()

    return response

#storing the results fetched from response in a dictionary
def getData():

    #storing response in data, returned by call to authorization function
    data = authorization()
    channelIdList = []
    channelTitleList = []
    infoDict = {}

    #data['items'] contains searchResource
    for item in data['items']:

        id = item['id']['channelId']
        channelIdList.append(id)

        title = item['snippet']['title']
        channelTitleList.append(title)

    infoDict['channelId'] = channelIdList
    infoDict['channelTitle'] = channelTitleList

    return infoDict
    