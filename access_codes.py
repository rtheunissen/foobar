"""
Returns a set of unique values where identical is
defined as either naturally equal or equal in reverse
"""
def palindromic_unique(values):

    collection = set()

    for value in values:
        if value[::-1] not in collection:
            collection.add(value)

    return collection

def answer(access_codes):
    return len(palindromic_unique(access_codes))
