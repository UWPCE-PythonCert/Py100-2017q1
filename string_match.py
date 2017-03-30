
import sys

def string_match(var1, var2):
    '''
    Count the number of matching 2 character sequences in 2 passed in strings
    Example: string_match("aabb", "bbaa") returns 2 [the "aa" & the "bb"]
    >>> string_match("aabb", "ccbbaa")
    2
    '''
    ans = 0
    # Make sure both arguments are strings & @ least 2 characters long
    if not type(var1) == str or not \
           type(var2) == str or not \
           len(var1) > 1 or not \
           len(var2) > 1:
        print('Both arguments must be a string, please try again.')
        sys.exit()
    else:
        cnt = 0
        for x in var1:
            if cnt == len(var1) - 1:
                break
            tst = x + var1[cnt + 1]
            cnt += 1
            if var2.find(tst) != -1:
                ans += 1
    return ans

if __name__ == "__main__":
    var1 = 'aabbcc'
    var2 = 'zzbbddaaccab'
    print(string_match(var1, var2))
