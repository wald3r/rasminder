from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from dateutil import parser
from raspberry import raspberry

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']


def main():
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = getCredentials()

    try:
        service = build('tasks', 'v1', credentials=creds)
        # Call the Tasks API

        results = service.tasklists().list(maxResults=10).execute()

        tasklists = results.get('items', [])

        flag = 0
        for list in tasklists:
            tasks = service.tasks().list(tasklist=list['id']).execute()
            items = tasks.get('items', [])
            for item in items:
                if 'due' in item.keys():
                   flag = checkDate(item)

        if flag == 1:
            raspberry().startBlinking()

    except HttpError as err:
        print('error')


def checkDate(item):

    date = parser.isoparse(item['due'])
    if datetime.today().date() == date.date():
        return 1



def getCredentials():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


if __name__ == '__main__':
    main()

