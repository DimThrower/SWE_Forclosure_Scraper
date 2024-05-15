import re

def ends_with_five_or_more_numbers(string):
    # Regular expression pattern: \d{5,}$
    # \d represents a digit, {5,} means five or more, and $ signifies the end of the string.
    return bool(re.search(r'\d{3,}$', string))

def remove_name_suffixes(name):
    # Define the pattern for matching the suffixes
    pattern = r'\s*(?:Jr\.?|Sr\.?|III|II|I)\b'
    # Replace the matched suffixes with an empty string
    cleaned_name = re.sub(pattern, '', name, flags=re.IGNORECASE)
    return cleaned_name

def split_names(name):
    # Initialize all parts to None
    owner_1_first_name = None
    owner_1_last_name = None
    owner_2_first_name = None
    owner_2_last_name = None

    # Split the name on '-' if it indicates two owners
    if '*' in name:
        names = name.split(' * ')
        owner_1_first_name, owner_1_last_name = names[0].split(' ', 1)
        if len(name) > 1:
            # print(f"Names: {name}")
            owner_2_first_name, owner_2_last_name = names[1].split(' ', 1)
    else:
        # Split the single owner name
        parts = name.split(' ')
        owner_1_first_name = parts[0]
        if len(parts) > 1:
            owner_1_last_name = ' '.join(parts[1:])

    return owner_1_first_name, owner_1_last_name, owner_2_first_name, owner_2_last_name

def transform_names_no_middle_initials(name):
    # print(f"Name string to split: {name}")

    # Remove suffixes
    name = remove_name_suffixes(name)
    # Pattern for names with middle initial (e.g., "Dustin J Weatherly")
    pattern_middle_initial = r"(\w+)\s\w+\s(\w+)"
    # Pattern for names with "&" including middle initials (e.g., "Robert B & Jacqueline Davis")
    pattern_double_with_initial = r"(\w+)\s\w*\s&\s(\w+\s)(\w+)"
    # Pattern for names with "&" but without middle initials (e.g., "Nelda & Bernice Spell")
    pattern_double_without_initial = r"(\w+)\s&\s(\w+\s)(\w+)"

    # Check if the name matches the middle initial pattern
    if re.match(pattern_middle_initial, name):
        return re.sub(pattern_middle_initial, r"\1 \2", name)
    # Check if the name matches the double name with initial pattern
    elif re.match(pattern_double_with_initial, name):
        return re.sub(pattern_double_with_initial, r"\1 \3 * \2\3", name)
    # Check if the name matches the double name without initial pattern
    elif re.match(pattern_double_without_initial, name):
        return re.sub(pattern_double_without_initial, r"\1 \3 * \2\3", name)
    # For single names, just return the name as is
    else:
        return name

def replace_after_last_slash(original_str, new_sub_str):
    pattern = r"(.*\\)[^\\]*$"
    result_string = re.sub(pattern, r"\1" + new_sub_str, original_str)

    return result_string