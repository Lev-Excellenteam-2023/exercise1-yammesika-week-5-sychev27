def join(*args, sep="-"):
    if not args:
        return []
    elif len(args) == 1:
        return args[0]

    amount_of_args = len(args)
    new_list = []

    for i in range(0, amount_of_args - 1):
        new_list += args[i]
        new_list.append(sep)

    return new_list + args[amount_of_args - 1]


print(join([1]))