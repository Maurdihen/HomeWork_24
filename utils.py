def some_functions(cmd, val, file):
    if cmd == "filter":
        res = list(filter(lambda s: val in s, file))
    if cmd == "map":
        res = "\n".join(map(lambda s: s.split()[int(val)], file))
    if cmd == "limit":
        res = list(file)[:int(val)]
    if cmd == "unique":
        res = list(set(file))
    if cmd == "sort":
        is_reverse = val == 'desc'
        res = sorted(file, reverse=is_reverse)
    return res