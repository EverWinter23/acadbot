'''
17th april 2018 tuesday
'''
import urllib.request, json, datetime, pprint
from tabulate import tabulate

def url_response(batch):
    link = "https://s3.ap-south-1.amazonaws.com/juit-webkiosk/2018EVESEM/" + str(batch) + ".json"
    try:
        url = urllib.request.urlopen(link)
    except urllib.error.HTTPError as ex:
        # print('acadbot:', ex)
        print("acadbot: The batch entered may be invalid. Please check again.")
        print('')
        print('acadbot: Exiting...')
        exit()
    except urllib.error.URLError as ex:
        # print('acadbot: ', ex)
        print("acadbot: There is a problem with the connectivity to the server. Please check your internet connection and try again.")
        print("acadbot: If the problem still persists, there might be a server error.")
        print('')
        print('acadbot: Exiting...')
        exit()
    data = json.loads(url.read().decode())
    return data

def cmd_time_table(batch, day=None):
    time_table = url_response(batch)
    if day is not None:
        days = [day]
    else:
        days = ['Mon','Tue', 'Wed', 'Thu', 'Fri']
    hrs = [time_table[day].keys() for day in days]
    day_count = 0
    for day in days:
        print(day)
        l = []
        for time in hrs[day_count]:
            del time_table[day][str(time)]['subjectCode']
            del time_table[day][str(time)]['facultyCode']
            json_list = list(time_table[day][str(time)].values())
            json_list.insert(0, convert_time(time))
            l.append(json_list)
        print(tabulate(l))
        day_count+=1

def convert_time(military_time):
    if len(military_time) != 4:
        military_time = (4 - len(military_time)) * '0' + military_time
    military_time = military_time[0:2] + ":" + military_time[2:]
    std_time = datetime.datetime.strptime(military_time, '%H:%M').strftime('%I:%M %p')
    return std_time