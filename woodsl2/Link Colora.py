def func(*args):
    for arg in args:
        print("Color:", arg)

func('red', 'blue', 'yellow', 'chartreuse')

#using just keyword arguments:

def func(**kwargs):
    for key in kwargs:
        print("Keyword arg: %s: $s " % (key, kwargs[key]) )

func(link_colors= 'red', black_colro = 'blue')
print("\n")

#using a combination of positional and keywords
def func(*args, **kwargs):
    for arg in args:
        print("Color :", arg)
    for key in kwargs:
        print("another keyword: %s: %s" % (key, kwards[key]))


func('purple, link_color='red', back_color ='blue')
print("\n")

#using *some_tuple and/or **some_dict
def func(*args, **kwargs):
    for arg in args:
        print("Color :", arg)
    for key in kwargs:
        print("another keyword arg:", kwargs[key])

regular = ('red' , 'blue')
links ={'link_color:' 'chartreuse'}
func(*regular, **links)