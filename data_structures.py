<<<<<<< HEAD

def filter_and_sort_evens(numbers):
    """Filter even numbers from the list and return them sorted."""
    evens = [n for n in numbers if n % 2 == 0]
    return sorted(evens)

def count_character_frequency(text):
    """Count frequency of each character in the given string."""
=======
def filter_and_sort_evens(numbers):
    """Return a sorted list of even numbers from the input list."""
    return sorted([n for n in numbers if n % 2 == 0])


def count_character_frequency(text):
    """Return a dictionary with character frequencies in the given text."""
>>>>>>> 368e060317a66df300dcbef080e78f94263404f3
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

<<<<<<< HEAD
# Test cases
print("Filtered & sorted evens:", filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))
print("Character frequency:", count_character_frequency("This my task for Basic Data Structures & Algorithms"))
=======

# Test cases
print(filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))
print(count_character_frequency("This my task for Basic Data Structures & Algorithms"))
>>>>>>> 368e060317a66df300dcbef080e78f94263404f3
