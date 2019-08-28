import csv

# file_name = "data_for_counting.csv"


def get_values(num_of_line):
    try:
        with open("data_for_counting.csv", "r", newline="") as file:
            # get data from file
            reader = csv.reader(file)

            # create list of data
            list_of_data = list(reader)
            # print("List of data from file \n-------------------------------\n", list_of_data, "\n")

            # check if expected line exists
            num = num_of_line - 1
            exists = 0 <= num < len(list_of_data)

            if exists:
                # get results
                res = list_of_data[num]
                print("Data for assertion: \n", res[0], " + ", res[1], " = ", res[2])
                return res[0], res[1], res[2]
            else:
                print("Expected line not found")
                return 0

    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("End reading file! \n")


def write_res_to_file(num_of_test, res_of_test):
    try:
        with open("tests_result.csv", "a", newline="") as file:
            for_writing = ["Test number {test}".format(test=num_of_test),
                           "\tTest status: {status}".format(status=res_of_test)]
            writer = csv.writer(file)
            writer.writerow(for_writing)
    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("End writing file! \n")


def add_smth(n1, n2, res):
    real_res = int(n1) + int(n2)
    print(int(real_res))
    if real_res == int(res):
        print("Pass")
    else:
        print("Fail")

