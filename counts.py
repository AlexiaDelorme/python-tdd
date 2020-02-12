def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("12345") == 0, "These are numbers"
assert count_upper_case("Ouzo1282 Caca%%") == 2, "Two upper cases"
assert count_upper_case("HOLA") == 4, "Four upper cases"

print("All the tests passed")