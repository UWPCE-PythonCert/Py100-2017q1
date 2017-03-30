class report (object):
    def __init__(self):
        names=[]
        sum_lists=[]

    def build_a_report(self):
        for pair in donation:
            if pair[0] + pair[1] not in names:
                name=pair[0]+pair[1]
                names.append(name)

             for i in names:
                sum=0
                count=0
                for j in donation:
                    if i==j[0]+j[1]:
                        sum=j[2]+sum
                        count=1+count
                sum_list=(i,sum,count,float(sum/count))
                sum_lists.append(sum_list)
            print(sum_lists)
