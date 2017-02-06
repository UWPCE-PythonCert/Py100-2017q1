from os import listdir
from os import chdir

def main(start_path, end_path = '/home/vagrant/Documents/Py100/Py100-2017q1/kdheard/Week 4/Test_folder'):
    files = listdir(start_path)
    for x in files:
        if x != "__init__.py":
            x = open(x,'rb')
            with x as copy:
                chdir(end_path)
                copy.write(bytes(x, '_copy'))
                chdir(start_path)
    end_result = listdir(end_path)
    print('End Result: {}'.format(end_result))



if __name__ == "__main__":

   main('/home/vagrant/Documents/Py100/Py100-2017q1/kdheard/Week 3')