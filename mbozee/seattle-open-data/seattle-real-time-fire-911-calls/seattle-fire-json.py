import json
import pprint
import urllib2

data = json.load(urllib2.urlopen('https://data.seattle.gov/resource/grwu-wqtk.json'))


def print_json(n):
    """Print n number of records."""
    count = 1
    for record in data[:n]:
        try:
            if ' 8th Av Ne' in record['address']:
                print('Record #', count)
                pprint.pprint(record['datetime'])
                pprint.pprint(record['address'])
                print('\n')
                count += 1
        except:
            KeyError

print_json(1000000)
