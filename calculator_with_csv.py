from calculator_setting import run_calculator
from calculator_additional_func import get_number
from file_worker import get_values


def addition(num1, num2, res):
    dlg = run_calculator()  # run a program
    # enter data
    dlg.type_keys(num1)
    dlg.child_window(auto_id='plusButton').click()
    dlg.type_keys(num2)
    dlg.child_window(auto_id='equalButton').click()
    real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
    dlg.close()
    assert real_res == int(res)
    print("Pass")


num1, num2, res = get_values(2)
addition(num1, num2, res)
