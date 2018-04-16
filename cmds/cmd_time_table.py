import urllib.request, json
from tabulate import tabulate

def min_time_table(time_table):
    hrs = [time_table[day].keys() for day in ['Mon','Tue', 'Wed', 'Thu', 'Fri']]
    day_count =0
    for day in ['Mon','Tue', 'Wed', 'Thu', 'Fri']:
        for time in hrs[day_count]:
            #print(element)
            del time_table[day][str(time)]['subjectCode']
            del time_table[day][str(time)]['facultyCode']
        day_count+=1
    return time_table

def url_response(batch):
    link = "https://s3.ap-south-1.amazonaws.com/juit-webkiosk/2018EVESEM/"+str(batch) + ".json"
    try:
        url = urllib.request.urlopen(link)
    except urllib.error.HTTPError:
        print("acadbot: The batch name '" +str(batch) + "' is an invalid batch")
        print('')
        print('acadbot: Exiting...')
        exit()
    data = json.loads(url.read().decode())
    return min_time_table(data)

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
            json_list = list(time_table[day][str(time)].values())
            json_list.insert(0, str(time))
            l.append(json_list)
        print(tabulate(l))
        day_count+=1