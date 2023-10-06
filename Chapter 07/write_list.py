# This program saves a list of strings to a file.
import pickle


def main():
    # Create a list of strings.
    sample_list = [1, 2, 3]
    file_name = "sample.pkl"

    open_file = open(file_name, "wb")
    pickle.dump(sample_list, open_file)
    open_file.close()

    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()

    print(loaded_list)


# Call the main function.
if __name__ == '__main__':
    main()
