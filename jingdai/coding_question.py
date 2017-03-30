#Dictionary of driver database ids with a list of dispatchers ids assigned.

dispatchers_by_driver_dbid = {'44': None, '15': [5], '13': [5], '2': [5], '26': [5], '39': [5], '42': [5], '29': [5], '17': [5], '41': [5], '22': [5], '27': [5], '24': [5], '18': [5], '21': [5], '36': [5], '14': [5], '19': [5], '4': [5], '9': [5], '37': [5], '32': [5], '3': [5], '46': None, '34': [5], '35': [5], '40': [5], '7': [5], '8': [5], '5': [5], '33': [5], '45': None, '12': [5], '6': [5], '38': [5], '10': [5], '31': [5], '1': [3, 5], '23': [5], '25': [5], '30': [5], '20': [5], '43': None, '16': [5], '28': [5], '11': [5]}

#driver.dbid = 1

#codriver.dbid = 2

drivers=[]
for key, value in dispatchers_by_driver_dbid.items():
    if key==str(1):
        drivers.append(value)

individual_drivers=[]
for driver in drivers:
    for individual_driver in driver:
        individual_drivers.append(individual_driver)
print(individual_drivers)

codrivers=[]
for key, value in dispatchers_by_driver_dbid.items():
    if key==str(2):
        codrivers.append(value)

individual_codrivers=[]
for codriver in codrivers:
    for individual_codriver in codriver:
        individual_codrivers.append(individual_codriver)
print(individual_codrivers)


for dispatcher in individual_codrivers:
    if dispatcher in individual_drivers:
        print("this is the common dispatcher: %s." % dispatcher)
    else:
        print("no common")





# Find the dispatcher id that applies to both drivers.
#
# Can it be improved:
#
#         driver_dispatchers = []
#
#         codriver_dispatchers = []
#
#         for key, value in dispatchers_by_driver_dbid.items():
#
#             if key == str(driver.dbid):
#
#                 driver_dispatchers = value
#
#             elif key == str(codriver.dbid):
#
#                 codriver_dispatchers = value
#
#         for dispatcher in driver_dispatchers:
#
#             for co_dispatcher in codriver_dispatchers:
#
#                 if dispatcher == co_dispatcher:
#
#                     return dispatcher
#
#         else:
#
#             raise Exception("No common dispatcher found")
