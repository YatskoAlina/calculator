from calculator_setting import run_calculator
from calculator_additional_func import get_number
from file_worker import get_values, write_res_to_file
import time


def addition(num1, num2, res):
    dlg = run_calculator()  # run a program
    # enter data
    dlg.type_keys(num1)
    dlg.child_window(auto_id='plusButton').click()
    time.sleep(2)
    dlg.type_keys(num2)

    # get result
    dlg.child_window(auto_id='equalButton').click()
    time.sleep(2)
    real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
    dlg.close()

    # assert results
    try:
        assert real_res == int(res)
        test_res = "Test Pass"
        print(test_res)
        return test_res
    except AssertionError:
        test_res = "Test Fail"
        print(test_res, AssertionError)
        return test_res


print("Please, enter number of test: ")
try:
    num_of_test = int(input())
    a = get_values(num_of_test)
    if type(a) == int:
        print("Incorrect test number")
        time.sleep(10)
    else:
        print("Start testing")
        res_of_test = addition(a[0], a[1], a[2])
        write_res_to_file(num_of_test, res_of_test)
except:
    print("Incorrect input. It`s not integer. Try again.")
