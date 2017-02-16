import os
path = os.path.abspath('../')

def main(start_path, end_path = path + '/Week 4/Test_folder/'):
    for root, subdir, files in os.walk(start_path):
        for file in files:
            found_file = open(start_path + file, 'rb').read()
            with open(end_path + file, 'wb') as copy:
                for file_bytes in found_file:
                    copy.write(bytes(file_bytes))
    end_result = os.listdir(end_path)
    print('End Result: {}'.format(end_result))

if __name__ == "__main__":
   main(start_path=path + '/Week 3/')