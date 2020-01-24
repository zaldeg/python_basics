def div(a, b):
    """ its return quotient of division
    
    a - dividend
    b - divisor

    some protection against fools is present
    """
    try:
        return round(float(a) / float(b), 4)
    except ZeroDivisionError:
        print("You are trying to create singularity!!!")
    except ValueError:
        print("Doesn't fool me it's not numbers!!!")


a, b = input("Enter two numbers separeted by spaces: ").split()

print(div(a, b))
