def SparseArray (array):
    pass

sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
len(sa)
sa[5]=12
sa[3]=0
del sa[4]
print(sa)
sa.append(12)
print(sa[2:4])