# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.write('Friedrich Nietzsche\n')

    # Close the file.
    outfile.close()


# Call the main function.
if __name__ == '__main__':
    main()
