# Exceptions Lab
# Improving input

# The input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
# Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions,
# when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
# Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input


def safe_input():
    """Return None when the user causes an exception."""
    user_input = input("Tell me something >>  ")

    try:
        print(user_input)
    except EOFError:  # User enters ^D (^Z on Windows)
        return None
    except KeyboardInterrupt:  # User enters ^C
        return None
    finally:
        print("End of program.")

if __name__ == '__main__':
    safe_input()
