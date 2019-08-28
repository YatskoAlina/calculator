import csv


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
        print("End reading file!")


def write_res_to_file(num_of_test, c_num1, c_num2, c_res, res_of_test, exec_time):
    try:
        with open("tests_result.csv", "a", newline="") as file:
            # formatted_time = "{:.4f}".format(exec_time)
            for_writing = ["Test number {test}".format(test=num_of_test),
                           "\tTest data: {n1} + {n2} = {res}".format(n1=c_num1, n2=c_num2, res=c_res),
                           "\tTest status: {status}".format(status=res_of_test),
                           "\tExecution time: {ex_time}".format(ex_time=exec_time)]
            writer = csv.writer(file)
            writer.writerow(for_writing)
    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("End writing file!")


def get_set_of_values():
    try:
        with open("data_for_counting2.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for i in reader:
                yield i

    except FileNotFoundError:
        print(FileNotFoundError)
