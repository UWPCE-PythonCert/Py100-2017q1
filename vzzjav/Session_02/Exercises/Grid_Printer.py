# Javier Vazquez
# Grid Printer
# Jan 21, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/grid_printer.html

def main():
    character = ["+", " ", "-"]
    line = ""
    for i in range(11):
        for j in range(21):
            if i == 0 or i == 5 or i == 10:
                if j == 0 or j == 10 or j == 20:
                    line +="+"
                elif j % 2 == 0 and (j != 10 or j != 20):
                    line +="-"
                else:
                    line +=" "
            line += "\n"
    print(line)






    # print("{0:<20}{1:>5}{2:<5}{3:<20}{4:>5}"
    #       .format([i])

if __name__ == '__main__':
    main()

