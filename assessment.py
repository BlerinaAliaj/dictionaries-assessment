"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    my_dict = {}

    for word in phrase.split():
        my_dict[word] = my_dict.get(word, 0) + 1

    return my_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_dict = {"Watermelon": 2.95,
                  "Cantaloupe": 2.50,
                  "Musk": 3.25,
                  "Christmas": 14.25}

    if melon_name in melon_dict:
        return melon_dict[melon_name]
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    my_dict = {}

    for word in words:
        word_len = len(word)

        if word_len not in my_dict:
            my_dict[word_len] = [word]
        else:
            my_dict[word_len].append(word)
            my_dict[word_len].sort()

        my_list = sorted(my_dict.items())

    return my_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Can Save the above output to another file and read it in to create
    # dictionary

    english_to_pirate = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be"}

    phrase_list = phrase.split()
    pirate_talk = []

    for word in phrase_list:

        if word in english_to_pirate:
            pirate_talk += [english_to_pirate[word]]
        else:
            pirate_talk += [word]

    pirate_string = ' '.join(pirate_talk)

    return pirate_string


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # This block is to create dictionary of every last letter in the names
    # list and give values of empty list

    letter_dictionary = {}
    for name in names:
        letter = name[-1]
        letter_dictionary[letter] = []

    # This pops the first value of the names list and assigns it to the
    # word_chains list

    word_chains = [names.pop(0)]

    # This will itterate over the new names list and add all the words to
    # the value list for each last letter of the word

    for name in names:
        my_key = name[0]
        if my_key in letter_dictionary:
            # append name to the value list of my_key
            letter_dictionary[my_key].append(name)

    last_letter = word_chains[0][-1]

    # This loop will look for last letter in dictionary, pull the first word
    # from the list, append it to the word_chains list, and remove it from the
    # value list in the dictionary. When Exception is raised, the function will
    # return the word_chains list.

    while last_letter in letter_dictionary:
        try:
            next_word = letter_dictionary[last_letter].pop(0)
            word_chains.append(next_word)
            last_letter = next_word[-1]

        except Exception:
            return word_chains


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
