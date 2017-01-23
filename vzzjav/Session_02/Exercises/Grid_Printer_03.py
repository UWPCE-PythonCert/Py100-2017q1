# Javier Vazquez
# Grid Printer
# Jan 21, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/grid_printer.html

def print_grid(n, m):
    line = ""
    for i in range(n*m+n+1):
        for j in range((n*m+n)*2+1):
            if i % (m+1) == 0:
                if j % ((m+1)*2) == 0:
                    if j == (n*m+n)*2:
                        line +="+\n"
                    else:
                        line += "+"
                elif j % 2 == 0 and (j != n or j != n*2):
                    line +="-"
                else:
                    line +=" "
            else:
                if j % ((m+1)*2) == 0:
                    if j == (n*m+n)*2:
                        line +="|\n"
                    else:
                        line += "|"
                else:
                    line +=" "

    print(line)

def main():
    n = input("Columns: ")
    m = input("Rows: ")
    print_grid(int(n), int(m))

if __name__ == '__main__':
    main()