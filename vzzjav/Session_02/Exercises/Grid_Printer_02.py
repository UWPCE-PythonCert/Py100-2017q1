# Javier Vazquez
# Grid Printer
# Jan 21, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/grid_printer.html

def print_grid(n):
    n += 1
    line = ""
    for i in range(n+1):
        for j in range(n*2+1):
            if i % n == 0 or i % (n/2) == 0:
                if j % n == 0:
                    if j == n*2:
                        line +="+\n"
                    else:
                        line += "+"
                elif j % 2 == 0 and (j != n or j != n*2):
                    line +="-"
                else:
                    line +=" "
            else:
                if j % (n) == 0:
                    if j == n*2:
                        line +="|\n"
                    else:
                        line += "|"
                else:
                    line +=" "

    print(line)

def main():
    n = input("Size of grid: ")
    print_grid(int(n))


if __name__ == '__main__':
    main()