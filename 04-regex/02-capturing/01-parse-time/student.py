import re
def parse_time(string):
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)

    if match:
        h, m, s, ms = match.groups(0)
        h = int(h)
        m = int(m)
        s = int(s)
        if isinstance(ms, int) != True:
            ms = int(ms[1:])
        return (h, m, s, ms)

    return None

