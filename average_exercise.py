def avg(*args):
    if not args or not all([isinstance(item, (int, float)) for item in args]):
        return None

    sum_of_args = sum(args)
    return sum_of_args / len(args)


print(avg(5, 2))