from calculator_setting import run_calculator
from calculator_additional_func import get_number
from file_worker import get_values, write_res_to_file, get_set_of_values
from datetime import datetime
import time


def addition(num1, num2, res):
    # start timer
    start_time = datetime.now()

    # run a program
    dlg = run_calculator()

    # enter data
    dlg.type_keys(num1)
    c_num1 = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())
    dlg.child_window(auto_id='plusButton').click()
    dlg.type_keys(num2)
    c_num2 = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())

    # get result
    dlg.child_window(auto_id='equalButton').click()
    real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())
    dlg.close()

    # assert results
    try:
        assert real_res == int(res)
        test_res = "Pass"
    except AssertionError:
        test_res = "Fail"
    finally:
        end_time = datetime.now() - start_time
        print("End testing!")

    return c_num1, c_num2, real_res, test_res, end_time


def add(n1, n2, res):
    start_time = datetime.now()
    real_res = int(n1) + int(n2)

    if real_res == int(res):
        test_res = "Pass"

    else:
        test_res = "Fail"

    time.sleep(1.4)
    end_time = datetime.now() - start_time
    return test_res, end_time


def run_addition_test():
    print("Please, enter number of test: ")

    try:
        num_of_test = int(input())
        a = get_values(num_of_test)

        if type(a) == int:
            print("Incorrect test number")
        else:
            print("Start testing...")

            # get test data and results
            c_num1, c_num2, c_res, res_of_test, exec_time = addition(a[0], a[1], a[2])

            # write information to file
            write_res_to_file(num_of_test, c_num1, c_num2, c_res, res_of_test, exec_time)
    except:
        print("Incorrect input. It`s not integer. Try again.")


def run_set_of_tests(amount_of_iter):
    # get generator
    generator_data = get_set_of_values()

    for i in range(amount_of_iter):
        # get one row of data
        data = next(generator_data)

        # convert data to list for correct using
        list_data = list(data)
        print(list_data[0], list_data[1], list_data[2])

        # perform addition
        c_num1, c_num2, c_res, res_of_test, exec_time = \
            addition(list_data[0], list_data[1], list_data[2])

        # write information to file
        write_res_to_file(i + 1, c_num1, c_num2, c_res, res_of_test, exec_time)


run_set_of_tests(2)
