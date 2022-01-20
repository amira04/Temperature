def temp_converter(temp, given_unit, desired_unit):
    if given_unit =='C' and desired_unit == 'F':
        converted_temp = (temp * 9/5) +32
        print (f'{converted_temp:.2f} {desired_unit}')

    if given_unit =='C' and desired_unit == 'K':
        converted_temp = temp+ 273.15
        print (f'{converted_temp:.2f} {desired_unit}')

    if given_unit =='F' and desired_unit == 'K':
        converted_temp = (temp -32) * 5/9 + 273.15
        print (f'{converted_temp:.2f} {desired_unit}')

    if given_unit =='F' and desired_unit == 'C':
        converted_temp = (temp -32) * 5/9
        print (f'{converted_temp:.2f} {desired_unit}')

    if given_unit =='K' and desired_unit == 'C':
        converted_temp = temp  -273.15
        print (f'{converted_temp:.2f} {desired_unit}')

    if given_unit =='K' and desired_unit == 'F':
        converted_temp = (temp -273.15) * 9/5 + 32
        print (f'{converted_temp:.2f} {desired_unit}')

    return
