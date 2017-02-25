def safeinput(inputstring):
    """function for input that catches EOF and Keyboard Interrupts"""
    try:
        data = input(inputstring + '\n')
        print(data)
    except EOFError or KeyboardInterrupt:
        raise
    finally:
        return None

def main():
    """main function"""
    safeinput('stuff')

if __name__ == '__main__':
    main()