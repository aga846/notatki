import re

# checking methods


def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)


def is_valid_phone(input):
    phone_regex = re.compile("^\d{3} \d{3}-\d{4}$")
    match = phone_regex.search(input)
    if match:
        return True
    return False


def is_valid_phone(input):
    phone_regex = re.compile("\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


# example with replacement
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.I)
result = pattern.sub("REDACTED", text)
print(result)


# exercise with replacement
def censor(single_string):
    censor_regex = re.compile(r"frack[a-z]*", re.IGNORECASE)
    result = censor_regex.sub("CENSORED", single_string)
    return result


print(censor("frack you"))
