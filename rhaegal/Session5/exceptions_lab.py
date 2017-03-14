def safe_input(str):
    while 1:
        try:
            user_input=input(str)
            break
        except (EOFError, KeyboardInterrupt):
            print("That's not a valid input")
    return user_input

safe_input("Please provide input")