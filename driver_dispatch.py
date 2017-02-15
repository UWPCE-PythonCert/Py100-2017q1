# 	$Id: play03.py,v 1.3 2017/02/04 20:32:31 larry Exp larry $	

# Dictionary | key = int of driver ID | val = list of dispatcher ID
dis_dr_id = {'44': None,'15': [5], '13': [5], '2': [5], '26': [5], '39': [5],
             '42': [5], '29': [5], '17': [5], '41': [5], '22': [5], '27': [5],
             '24': [5], '18': [5], '21': [5], '36': [5], '14': [5], '19': [5],
             '4': [5], '9': [5], '37': [5], '32': [5], '3': [5], '46': None,
             '34': [5], '35': [5], '40': [5], '7': [5], '8': [5], '5': [5],
             '33': [5], '45': None, '12': [5], '6': [5], '38': [5], '10': [5],
             '31': [5], '1': [3, 5], '23': [5], '25': [5], '30': [5], '20': [5],
             '43': None, '16': [5], '28': [5], '11': [5]}

def find_dispatcher (dr_id, co_id):
    """
    Find dispatcher function
    - Arguments are driver ID & co-driver ID
    - Returns dispatcher common to both or None if not found
    Example ...
    dis_dr_id = {"1":[5],"2":[5]}
    find_dispatcher(1,2) returns [5]
    """

    # Highest possible driver number
    top_num = 100
    tst_lst = [x for x in range(1, top_num + 1)]

    # Various error checks
    # Does database exist
    if not 'dis_dr_id' in globals():
        return "Database does not exist!"
    # Test if driver & co-driver ID are integers
    elif not type(dr_id) is int or not type(co_id) is int:
        return "Driver ID & co-driver ID must be integers!"
    # Test values of driver & co-driver IDs
    elif not dr_id in tst_lst or not co_id in tst_lst:
        return "Driver ID & co-driver ID must be between 1 and " + str(top_num)
    # Check if driver in database
    elif not str(dr_id) in dis_dr_id:
        return "Driver ID not in database."
    # Check if co-driver in database
    elif not str(co_id) in dis_dr_id:
        return "Co-driver ID not in database."

    # Driver, list of lists
    dr_lst = []

    # Co-driver, list of lists
    co_lst = []

    # Create list of dispatchers for driver & co-driver
    for x in dis_dr_id:
        if x == str(dr_id) and dis_dr_id[x] != None:
            dr_lst.append((dis_dr_id[x]))
        if x == str(co_id) and dis_dr_id[x] != None:
            co_lst.append((dis_dr_id[x]))

    # Common dispatcher list
    dis_lst = []

    for a in dr_lst:
        for b in a:
            for c in co_lst:
                if b in c:
                    dis_lst.append(b)

    if len(dis_lst) > 0:
        return list(set(dis_lst))
    else:
        return None

if __name__ == "__main__":
    print(find_dispatcher(1, 2))
