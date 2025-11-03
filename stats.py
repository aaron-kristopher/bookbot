from typing import Dict


def get_word_count(content: str) -> int:
    """Returns the number of words within the string"""
    return len(content.split())


def get_char_count(content: str):
    """Returns the number of appearances each alpha character has within the text"""
    char_count = {}

    # Iterate over file content
    for char in content:
        char = char.lower()  # Normalize characters to lowercase

        # Increments value by 1.
        # Starts at 0 if not initalized within dictionary
        char_count[char] = char_count.get(char, 0) + 1

    return sort_chars(char_count)


def sort_chars(char_count: Dict[str, int]):
    """
    Sorts each character count entry into their own dictionary
    Stores all character dict within an array and sorts in descending order
    """
    char_list = []

    for k, v in char_count.items():
        char_list.append({"char": k, "count": v})

    return sorted(char_list, key=lambda x: x["count"], reverse=True)
