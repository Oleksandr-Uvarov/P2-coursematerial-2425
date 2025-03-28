import re
def is_valid_student_id(string):
    return re.fullmatch("(s|S|r|R)[0-9]{7}", string)