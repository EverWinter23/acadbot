'''
17th april 2018
old dominion - written in the sand
'''

import links, uplink, requests
# pretty print
import pprint
# for testing purposes
from getpass import getpass

def get_key_from_heroku():
    """Gets API key from acadbot server"""
    try:
        return requests.get(links.HEROKU_ACADBOT_SERVER_URL).json()[links.KEY]        
    except Exception as ex:
        print('acadbot:', ex)
        print('acadbot: Our server is down, pls contact @authors...')
        exit()


# time alloted for fetching each request is 60s
# must provide api key for using the api
@uplink.headers({links.KEY: get_key_from_heroku()})
class JuitClient(uplink.Consumer):
    @uplink.timeout(60)
    @uplink.get(links.URL_LOGIN)
    # query[uid] = username
    # query[pwd] = password
    def login(self, args : uplink.QueryMap("args")):
        """Log onto remote server using username and passwd."""
        pass

    # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_USER_DETAILS)
    def get_user_details(self, query: uplink.QueryMap("query")):
        """Fetch client's personal details."""
        pass

    # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_ATTENDANCE)
    def get_attendance(self, query: uplink.QueryMap("query")):
        """Fetch client's attendance."""
        pass

    # q['session'] = session_key
    # q['data'] = detailAttendanceData
    # q['code'] = subject_code
    @uplink.timeout(60)
    @uplink.get(links.URL_ATTENDANCE_DETAIL)
    def get_attendance_details(self, query: uplink.QueryMap("query")):
        """Fetch client's attendance in detail."""
        pass

   # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_SUBJECT_REGISTD)
    def get_registered_subjects(self, query: uplink.QueryMap("query")):
        """Fetch client's registered subjects."""
        pass

   # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_SUBJECT_FACULTY)
    def get_subject_faculty(self, query: uplink.QueryMap("query")):
        """Fetch client's subject faculty."""
        pass

   # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_SGPA_CGPA)
    def get_sgpa_cgpa(self, query: uplink.QueryMap("query")):
        """Fetch client's sgpa and cgpa."""
        pass

    # q['session'] = session_key
    # q['sem'] = sem_code
    @uplink.timeout(60)
    @uplink.get(links.URL_EXAM_GRADES)
    def get_exam_grades(self, query: uplink.QueryMap("query")):
        """Fetch client's exam grades."""
        pass
    
    # query[session] = session_key
    @uplink.timeout(60)
    @uplink.get(links.URL_SEM_LIST)
    def get_sem_list(self, query: uplink.QueryMap("query")):
        """Fetch client's semester list."""
        pass

