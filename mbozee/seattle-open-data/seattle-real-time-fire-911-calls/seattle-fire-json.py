import json
import pprint
import urllib2

data = json.load(urllib2.urlopen('https://data.seattle.gov/resource/grwu-wqtk.json'))


def print_json(n):
    """Print n number of records."""
    count = 1

    for record in data[:n]:
        try:
            # JSON datetime format example : u'2016-04-06T14:55:00.000'
            year = record['datetime'][:4]
            month = record['datetime'][5:7]
            day = record['datetime'][8:10]
            my_street = ''
            if my_street in record['address']:
                print('Record #', count)
                # pprint.pprint(record['datetime'])
                print(month + "/" + day + "/" + year)
                pprint.pprint(record['address'])
                print('\n')
                count += 1
        except:
            KeyError

print_json(1000000)
