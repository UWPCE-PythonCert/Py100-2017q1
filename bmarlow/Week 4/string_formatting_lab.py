def main():
    print("format string for (2, 123.4567, 10000)")
    tup = (2, 123.4567, 1000)
    print(" file_{:03d} {:.2f} {:e}".format(*tup))

    print("print first 3 values of an arbitrarily long tuple")
    newtup = (1,2,3,4,5,6)
    print("the first 3 numbers are: {:d}, {:d}, {:d}".format(*newtup))


if __name__ == '__main__':
    main()