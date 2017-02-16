#Doesn't handle parens and quotes well
#Assumption: If the key doesn't exist, that's the end of a sentence.

#f = open('/media/sf_UWPython100/sherlock_small.txt', 'r')
f = open('/media/sf_UWPython100/sherlock.txt', 'r')
f2 = open('/media/sf_UWPython100/newstory.txt', 'w')
import random

#verify each of the conditionals
def verify(value, char, conditional):
    if (conditional):
        if (value.startswith(char)):
            return False, conditional
        elif (value.endswith(char)):
            return True, False
        return True, conditional
    else:
        if (value.endswith(char)):
            return False, conditional
        elif (value.endswith(char)):
            return True, False
        return True, conditional


if __name__ == '__main__':
    size=1000
    new_story=""
    key1,key2,values="","",""
    paren_open = ['(', False]
    quote_open = ['"', False]
    single_quote_open = ["'", False]
    conditionals=[paren_open, quote_open, single_quote_open]
    capitalize=True
    first_cap=True #This makes it so the story doesn't start with a space
    gud_english_check=False #so we don't have double open parens/quotes

    big_dict={}
    #Read each word in- strip whitespace and newlines and split them
    for word in (f.read().strip()).split():
        big_dict.setdefault(" ".join([key1, key2]), []).append(word)
        key1=key2
        key2=word
    look_up_key = random.choice(list(big_dict.keys()))
    for i in range(0,size,1):
        if not look_up_key in big_dict:
            look_up_key = random.choice(list(big_dict.keys()))
            new_story=". ".join([new_story])
            capitalize=True
        values = big_dict[look_up_key]

        #there has to be a better way of writing this. Essentially keep pulling values if you have a double open quote/paren value
        count=0 #this has a habit of getting stuck
        while not gud_english_check:
            #We assume it's correct
            gud_english_check=True
            count+=1
            value=random.choice(values)
            #enumerate here, but I cant get it to work
            #k,i,j for enumerate(conditionals):
            k=-1
            for i,j in conditionals:
                k+=1
                #run verify and update boolean for that character
                if i in value:
                    gud_english_check, conditionals[k][1]=verify(value,i,j)
                    print(value,i,j,gud_english_check)
                    #if one of the conditionals fails, break out to reset
                if not gud_english_check:
                    break
                #get a new look up key if this was/is stuck.
            if count >10:
                look_up_key = random.choice(list(big_dict.keys()))
                values = big_dict[look_up_key]
                count=0
        gud_english_check=False

        if capitalize:
            if first_cap:
                new_story = "".join([new_story, value.title()])
                first_cap=False
            else:
                new_story=" ".join([new_story,value.title()])
        else:
            new_story = " ".join([new_story, value])
        first, second = look_up_key.split(" ")
        look_up_key=" ".join([second,value])
        capitalize=False
    #print(big_dict)
    #print(new_story)
    f2.write(new_story)
