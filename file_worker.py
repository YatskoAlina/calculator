import csv

# file_name = "data_for_counting.csv"


def read_data(file_name):
    try:
        with open("data_for_counting.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                num1 = row[0]
                num2 = row[1]
                add_res = row[2]
                # print(num1, " + ", num2, " = ", add_res)
                return num1, num2, add_res

    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("End try block")


def get_values(num_of_line):
    try:
        with open("data_for_counting.csv", "r", newline="") as file:
            # get data from file
            reader = csv.reader(file)

            # create list of data
            list_of_data = list(reader)
            print(list_of_data)

            # check if expected line exists
            num = num_of_line - 1
            exists = 0 <= num < len(list_of_data)

            if exists:
                # get results
                res = list_of_data[num]
                print(res[0], res[1], res[2])
                return res[0], res[1], res[2]
            else:
                print("Expected line not found")
                return 0

    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("End reading file")


def add_smth(n1, n2, res):
    real_res = int(n1) + int(n2)
    print(int(real_res))
    if real_res == int(res):
        print("Pass")
    else:
        print("Fail")

