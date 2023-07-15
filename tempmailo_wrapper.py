import requests
from bs4 import BeautifulSoup
import json
import re

class TempMail:
    BASE_URL = 'https://tempmailo.com/'

    def __init__(self):
        self._session, self._requestverificationtoken, self._email_address = self._get_session()
    

    def _get_session(self):
        session = requests.Session()

        requestverificationtoken, email_address = None, None

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        response = session.get(self.BASE_URL, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            try:
                requestverificationtoken = soup.find('input', {'name':'__RequestVerificationToken'})['value']
            except TypeError:
                requestverificationtoken = ''

            headers['referer'] = self.BASE_URL
            headers['requestverificationtoken'] = requestverificationtoken

            response = session.get(f'{self.BASE_URL}changemail', headers=headers)
            if response.status_code == 200 and re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', response.text.strip()):
                email_address = response.text.strip()
        
        if len(session.cookies.get_dict()) < 1:
            print('Failed to create a valid session.')
            session = None

        return session, requestverificationtoken, email_address


    def get_messages(self):
        if self._session and self._requestverificationtoken:
            headers = {
                'referer': self.BASE_URL,
                'requestverificationtoken': self._requestverificationtoken,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }

            json_data = {
                'mail': self._email_address,
            }

            response = self._session.post(self.BASE_URL, headers=headers, json=json_data)

            try:
                recieved_mails = json.loads(response.content)
                return recieved_mails
            except ValueError:
                print('Returned response is not a valid JSON object.')
            except Exception as e:
                print(f'An error occurred while retrieving messages: {str(e)}')
        else:
            print('Valid session not found.')
        


    def get_email_address(self):
        if self._email_address:
            return self._email_address
        else:
            print('Email not found.')
