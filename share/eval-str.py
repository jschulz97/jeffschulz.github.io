
def eval_str(num_str, base):
    # Get the length of integer part of number
    # ind is the magnitude of the digit 
    # (increasing from right to left, the first digit to the left of the decimal is 0)
    if('.' in num_str):
        ind = num_str.index('.') - 1
    else:
        ind = len(num_str) - 1

    # Erase the period from the string
    num_str = num_str.replace('.','')

    # Initalize output float
    out = 0.0

    # Iterate through each digit 
    for l in num_str:
        # handle non-number digits
        # val is value of the digit (1 is 1, a is 10, b is 11, etc)
        if(not l.isdigit()):
            val = int(ord(l.lower()) - 87)
        else:
            val = int(l)

        # Find the decimal value of the digit 
        # Add it to the rolling output float
        out += (val * pow(int(base),ind))
        
        # decrease the order of magnitude by one
        ind = ind - 1
        

    return float(out)



print(eval_str('3.14', 10))

print(eval_str('100.101', 2))

print(eval_str('2c', 16))

