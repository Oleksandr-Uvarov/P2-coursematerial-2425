def merge_dictionaries(d1, d2, merge_function):
    merged_dict = d1.copy()

    for key in d2:
        if key not in merged_dict:
            merged_dict[key] = d2[key]
        else:
            merged_dict[key] = merge_function(d1[key], d2[key])

    return merged_dict


# If a key only appears in d1, simply copy it and its corresponding value to the resulting dictionary.
# Same for d2.
# If a key k appears both in d1 and d2, then the corresponding values d1[k] and d2[k] are fed to merge_function. The return value of this merge_function then the value for k in the resulting dictionary.

