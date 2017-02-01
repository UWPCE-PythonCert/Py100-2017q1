# Session 3 Lab: String Formatting Lab

sample = (2, 123.4567, 10000)


def format_string(raw_info):
    """Format input for file info."""
    file_name = raw_info[0]
    file_float = raw_info[1]
    file_number = raw_info[2]

    # Pad file name with 0s, to produce name length 3.
    while len(str(file_name)) < 3:
        file_name = '0' + str(file_name)
    file_name = 'file_' + file_name

    # Round float to 2 decimal places.
    file_float = round(file_float, 2)

    # Formatting to be done later.

    print(file_name + ' :   ' + str(file_float) + ', ' + str(file_number))

format_string(sample)
