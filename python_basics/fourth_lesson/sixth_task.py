import itertools, sys

try:
    _, type_of_script, start_end = sys.argv

    some_list = ["hello", 1, True, False, (1, 2), {1, True}, "some"]
    counter = 0

    if type_of_script == "cycle":
        for i in itertools.cycle(some_list):
            print(i)
            counter += 1
            if counter == int(start_end):
                break
    elif type_of_script == "count":
        for i in itertools.count(int(start_end)):
            print(i)
            if i > int(start_end) + 10:
                break
except:
    print(
        f"You did something wrong!!!\nU can choose two iterators:\n"
        f"One is 'cycle' with number of elements do you get. (params = 'cycle', number)\n"
        f"Second 'count' with number which to start. (params = 'count', number)"
    )
