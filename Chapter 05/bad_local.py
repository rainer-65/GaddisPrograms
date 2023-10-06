# Definition of the main function.
name = ""


def main():
    get_name()
    print(f'Hello {name}.')  # This causes an error!


# Definition of the get_name function.
def get_name():
    global name
    name = input('Enter your name: ')


# Call the main function.
main()
