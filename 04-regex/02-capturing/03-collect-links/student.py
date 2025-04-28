import re
def collect_links(string):
    match = re.findall(r'<a href="(.*)">.*</a>', string)

    return match
