def get_num_words(book_text):
    return len(book_text.split())


def get_unique_characters(book_text):
    unique_chars = {}
    for ltr in book_text:
        lltr = ltr.lower()
        if lltr not in unique_chars:
            unique_chars[lltr] = 0
        unique_chars[lltr] += 1
    return unique_chars


def sort_on(dict):
    return dict["count"]


def get_sorted_counts(character_counts):
    result = []
    for k in character_counts:
        result.append({"letter": k, "count": character_counts[k]})
    result.sort(reverse=True, key=sort_on)
    return result
