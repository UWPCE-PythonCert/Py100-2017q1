

dispatchers_by_driver_dbid = {'44': None, '15': [5], '13': [5], '2': [5], '26': [5], '39': [5], '42': [5], '29': [5], '17': [5], '41': [5], '22': [5], '27': [5], '24': [5], '18': [5], '21': [5], '36': [5], '14': [5], '19': [5], '4': [5], '9': [5], '37': [5], '32': [5], '3': [5], '46': None, '34': [5], '35': [5], '40': [5], '7': [5], '8': [5], '5': [5], '33': [5], '45': None, '12': [5], '6': [5], '38': [5], '10': [5], '31': [5], '1': [3, 5], '23': [5], '25': [5], '30': [5], '20': [5], '43': None, '16': [5], '28': [5], '11': [5]}

driver_dbid = 1
codriver_dbid = 2


driver_dispatchers = set()
codriver_dispatchers = set()
for key, value in dispatchers_by_driver_dbid.items():
    if key == str(driver_dbid):
        driver_dispatchers.update(value)
    elif key == str(codriver_dbid):
        codriver_dispatchers.update(value)

try:
    print(driver_dispatchers.intersection(codriver_dispatchers))

except:
    raise Exception("No common dispatcher found")