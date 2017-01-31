
    #
    # Write a format string that will take:
    #
    #     ( 2, 123.4567, 10000)
    #
    #     and produce:
    #
    #     'file_002 :   123.46, 1.00e+04'


print("file_{:0>3d}: {:.2f}, {:.2e}".format(2, 123.4567, 10000))

t=(1,2,3)
print("the 3 numbers are: {:d}, {:d}, {:d}".format(*t))
