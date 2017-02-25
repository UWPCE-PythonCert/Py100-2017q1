def main():
    dict1 = {'name': 'Kayla', 'cake': 'Double Layer Fudge', 'city': 'Seattle'}
    print("Our dictionary: {}".format(dict1))
    for key, item in dict1.items():
        if key == 'cake':
            del dict1['cake']
            break
    print("Deleting cake: {}".format(dict1))
    dict1['fruit'] = 'Mango'
    print("Adding fruit: {}".format(dict1))

    print("Our keys now: {}".format(dict1.keys()))
    print("And our values: {}".format(dict1.values()))

    try:
        print(dict1['cake'])
    except:
        print("\nTHERE IS NO CAKE HERE, YOU HEATHENS.")
    try:
        for key,item in dict1.items():
            if item == 'Mango':
                print("\nBut we have mangos!")
    except:
        print("There are no mangos here either, this sucks!")


    for key,item in dict1.items():
        new_value = "t"*len(item)
        dict1[key] = new_value

    print("ALL THE T'S! {}".format(dict1))

    s2 = set()
    s3 = set()
    s4 = set()
    for n in range(0,21):
        if n % 2 == 0:
            s2.add(n)
        if n % 3 == 0:
            s3.add(n)
        if n %4 == 0:
            s4.add(n)
    print("SETS: \n", s2, "\n", s3, "\n", s4)

    print("Is the middle set a subset of the first set? {}".format(s3.issubset(s2)))
    print("Is the last set a subset of the first set? {}".format(s4.issubset(s2)))

if __name__ == "__main__":

   main()
