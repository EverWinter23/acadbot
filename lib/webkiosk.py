'''
18th april 2018 Wednesday
'''

from lib.juit_client import JuitClient
import lib.links as links

class WebKiosk:
        
    def __init__(self):
        self.user = JuitClient(links.URL_BASE)

    def login(self, args):
        result = self.user.login(args).json()
        # estd. session
        session_key = None
        if result['response'] == 'Login Successfull':
            session_key = result['loginCookies']
            return session_key
        else:
            print("acadbot: could not estd. session...")
            exit()
    
    def attendance(self, args):
        query = {}
        print("acadbot: fetching attendance...")
        query['session'] = self.login(args)
        result = self.user.get_attendance(query).json()
        return result['attendance']

    def cgpa_sgpa(self, args):
        query = {}
        query['session'] = self.login(args)
        result = self.user.get_sgpa_cgpa(query).json()
        return result['cgsg']
