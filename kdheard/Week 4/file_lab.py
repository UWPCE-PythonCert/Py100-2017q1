from os import listdir

def main(start_path):
    files = listdir(start_path)
    for x in files:
        print(x)

if __name__ == "__main__":
    main('/home/vagrant/Documents/Py100/Py100-2017q1/kdheard/Week 4')