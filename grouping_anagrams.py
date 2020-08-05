def grouping_anagrams(arr, sort=False):
    """Group a list a words together if they're anagrams of each other.

    Args:
        arr (List[str]): List of words to be grouped.
        sort (boolean): A flag indicating if the final result should be sorted.

    Returns:
        List[List[str]]: List of grouped words.
    """
    grouped = {}

    for word in arr:
        # Calculate the anagram the word belongs to by rearranging it 
        # in alphabetically ascending order
        anagram = ''.join(sorted(word)) 
        if anagram in grouped:
            grouped[anagram].append(word)
        else:
            grouped[anagram] = [word]

    if sort:
        # If specified, sort the groups and the list of words 
        # in alphabetically ascending order
        sorted_anagrams = sorted(grouped.keys())
        result = [sorted(grouped[anagram]) for anagram in sorted_anagrams]
    else:
        result = [words for words in grouped.values()]
    
    return result


if __name__ == '__main__':
    words = ["roma", "paso", "frase", "mora", "sapo", "prisa", "amor", "fresa", "paris", "pagar", "cesar", "praga"]
    sort = False
    result = grouping_anagrams(words, sort)
    
    print(result)