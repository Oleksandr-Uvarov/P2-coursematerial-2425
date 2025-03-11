def string_with_consecutive_characters(strings):
    def consecutive(string):
        for i in range(len(string) - 1):
            if string[i] == string[i+1]:
                return True
        return False

    return find(strings, consecutive)    
    # for string in strings:
    #     for index in range(len(string) - 1):
    #         if string[index] == string[index + 1]:
    #             return string
    # return None


def find(lst, funct):
    for object in lst:
        if funct(object):
            return object
    return None


print(find(["monkey", "banana", "computer", "yellow", "oddish"], string_with_consecutive_characters))