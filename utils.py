import re
from typing import List, Union, TextIO

def some_functions(cmd: str, val: str, file: TextIO) -> Union[str, List]:
    if cmd == "filter":
        return list(filter(lambda s: val in s, file))
    if cmd == "map":
        return "\n".join(map(lambda s: s.split()[int(val)], file))
    if cmd == "limit":
        return list(file)[:int(val)]
    if cmd == "unique":
        return list(set(file))
    if cmd == "sort":
        is_reverse: bool = val == 'desc'
        return sorted(file, reverse=is_reverse)
    if cmd == "regex":
        regexp: re.Pattern = re.compile(val)
        return list(filter(lambda x: regexp.findall(x), file))
    return ""