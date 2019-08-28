from calculator_setting import run_calculator
from calculator_additional_func import get_number
from file_worker import get_values, write_res_to_file
import time


def addition(num1, num2, res):
    # start timer
    start_time = time.time()

    # run a program
    dlg = run_calculator()

    # enter data
    dlg.type_keys(num1)
    c_num1 = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())
    dlg.child_window(auto_id='plusButton').click()
    # time.sleep(2)
    dlg.type_keys(num2)
    c_num2 = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())

    # get result
    dlg.child_window(auto_id='equalButton').click()
    # time.sleep(2)
    real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())
    dlg.close()

    # assert results
    try:
        assert real_res == int(res)
        test_res = "Pass"
        end_time = time.time() - start_time
    except AssertionError:
        test_res = "Fail"
        end_time = time.time() - start_time
    finally:
        print("End testing!")

    return c_num1, c_num2, real_res, test_res, end_time


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
