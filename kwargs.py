def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("The values of {} is {}".format(key, value))

print_kwargs(my_name = "Sammy", your_name = "Casey")