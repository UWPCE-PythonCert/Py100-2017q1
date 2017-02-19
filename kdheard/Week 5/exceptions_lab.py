from time import sleep

def safe_input(text):
    redefined_function = text
    try:
        print(redefined_function)
        sleep(60)
    except EOFError as error:
        raise None from error
    except KeyboardInterrupt as error:
        raise Exception("I'm cool") from error

safe_input("test")