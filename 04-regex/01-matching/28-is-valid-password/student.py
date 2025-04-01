import re

def is_valid_password(string):
    numbers = re.fullmatch(r".*[0-9].*", string)
    lowercase = re.fullmatch(r".*[a-z].*", string)
    uppercase = re.fullmatch(r".*[A-Z].*", string)
    special = re.fullmatch(r".*[\+\-\*/\.@].*", string)
    length = re.fullmatch(r"(.){12,}", string)
    
    three_chars = re.fullmatch(r".*(.)\1\1.*", string)
    four_chars = re.fullmatch(r".*(.).*\1.*\1.*\1.*", string)

    if any([three_chars, four_chars]):
        return False
    

    # return all([numbers, lowercase, uppercase, special])
    # return all([numbers, lowercase, uppercase, length]) 
    # return all([numbers, lowercase, special, length]) 
    # return all([numbers, uppercase, special, length]) 
    # return all([lowercase, uppercase, special, length]) 
    return all([numbers, lowercase, uppercase, special, length]) 
 

    
    # return re.fullmatch(r"(.*[0-9]+.*[a-z]+.*[A-Z]+.*[+|-|*|/|.|@]+.*){12,}", string)
    # return re.fullmatch("([A-Z]+.*){12,}", string)

# print(is_valid_password("FQPIQFKg/1"))
# length = re.fullmatch(r"(.){12,}", "FQPIQFKg/1")

# print(bool(length))



# , expected True, received False
# , expected True, received False
# , expected True, received False
# FAILr , expected True, received False
# 


print(bool(is_valid_password("Apfoajaz-4312948")))
print(bool(is_valid_password("FQPIQFKg-4312948")))
print(bool(is_valid_password("FQPIQFKpfoajaz-1")))
print(bool(is_valid_password("FQPIQFKpfoajaz-4312948")))
print(bool(is_valid_password("fjkla9512-FQZJFP")))
