def get_number(some_str):
    splited_str = some_str.split(" ", 2)
    without_symb = splited_str[2].replace("\xa0", "")
    without_spaces = without_symb.replace(" ", "")
    for_convert = without_spaces.replace(",", ".")
    converted = float(for_convert)
    return converted
