#!/usr/bin/env python3
import random

def open_file(file):

    with open(file,'r') as f:
        s=f.read()
        s = s.replace("\n", " ") # remove  line feed
        s = s.replace("--"," ")
        s = s.replace(",","")
        s = s.replace(".","")
        s = s.replace("(","")
        s = s.replace(")","")

    return s


def build_dict(s):
    l=s.split(' ')
    d={}
    for i in range(len(l)-2):
            values=[]
            key=l[i]+ ' '+l[i+1]
            value=l[i+2]
            values.append(value)
            if key in d:
                for i in range(len(d[key])): # get all the elements from the value list
                    values.append(d[key][i])
                    values.reverse()
            d[key]=values

    key_count={} # store number of values of a key
    key_list=list(d.keys())
    for key in key_list:
        if key in d.keys():
            count=len(d[key])
            key_count[key]=count

    return (d, key_count, key_list)

def trigram(d,key_count,key_list):
    seed=random.randint(0,len(key_list)) # choose a random number as a starting point
    start_point=key_list[seed-1]
    new_string=start_point
    key_point={}   # store the number of how many times a key was hit
    key_point=key_count.copy()
    for key in key_point:
        values=0
        key_point[key]=values

    for i in range(len(d)):

        nl=new_string.split(' ')
        new_key=nl[i] + ' '+nl[i+1]
        if new_key in d:
            if key_count[new_key]==1:
                new_string= new_string+ ' ' + d[new_key][0]
                key_point[new_key]=1
            elif key_count[new_key]>1:
                if key_point[new_key]<key_count[new_key]:
                    i=0
                    new_string= new_string+ ' ' + d[new_key][key_point[new_key]] # if a key has multiple values, then return each value one after another
                    key_point[new_key]=(key_point[new_key]+1)
        else:
            break

    return(new_string)


if __name__ == "__main__":
    file='/home/vagrant/github/Py100-2017q1/jingdai/sherlock_small.txt'
    try:
        f = open(file)
    except OSError:
        print("file is not there!!")
        raise


    s=open_file(file)#read file and transform file
    d, key_count, key_list=build_dict(s)
    string=trigram(d, key_count, key_list)
    print(string)



