from sourcecode import addition
#import sourcecode.addition 
#import addition
def perform_operation(multiplier, multiplicand):
    result = 0
    for _ in range(multiplier):
        result = addition.perform_operation(result, multiplicand)
    return result