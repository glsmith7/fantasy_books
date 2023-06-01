"""Main module."""

import random

def sentence(words):
    """
    Return a randomly generated sentence of lorem ipsum text.
    The first word is capitalized, and the sentence ends in either a period or
    question mark. Commas are added at random.
    """

    # Determine the number of comma-separated sections and number of words in
    # each section for this sentence.
    sections = [
        " ".join(random.sample(words, random.randint(3, 12)))
        for i in range(random.randint(2, 5))
    ]
    s = ", ".join(sections)
    # Convert to sentence case and add end punctuation.
    return "%s%s%s" % (s[0].upper(), s[1:], random.choice("?."))


def paragraph(words):
    """
    Return a randomly generated paragraph of lorem ipsum text.
    The paragraph consists of between 2 to 4 sentences.
    """
    return " ".join(sentence(words) for i in range(random.randint(2, 4)))


def paragraphs(words,count=5):
    """
    Return a list of paragraphs as returned by paragraph(). the first
    paragraph will be the standard 'lorem ipsum' paragraph.
    """
    paras = []
    for i in range(count):
            paras.append(paragraph(words = words))
    return "\n".join(paras)


def words(words,count=5,limit=0):
    """
    Returns lorem ipsum words separated by a single space.
    Limit is not usually need, but for some things (e.g., Akkadian) it does wonky things if there are more 50 characters in the string.

    x = (lf.words(vocab_dictionary["Akkadian"],limit=50)) 
    """
    word_list = []
    c = len(word_list)
    if count > c:
        count -= c
        while count > 0:
            c = min(count, len(words))
