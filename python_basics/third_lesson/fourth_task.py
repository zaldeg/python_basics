def my_func(x, y):
    """ raising to a power

    x > 0
    y < 0 and y is contained in integer nambers 

    """
    try:
        x, y = float(x), float(y)
        if x > 0 and y < 0 and int(y) == float(y):
            answer = 1
            for _ in range(int(abs(y))):
                answer /= x
            return answer
            # return x ** y
        else:
            print("You have entered wrong nummbers look to func commnet.")
    except:
        print("Enter numbers not something else!")


a, b = input("Enter two numbers separeted by spaces: ").split()
print(my_func(a, b))
