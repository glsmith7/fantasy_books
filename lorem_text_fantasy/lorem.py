"""Main module."""

import random
global WORDS

WORDS = ()

def import_language(lang):
    dictionary_languages = {
        "Latin" : "latin.txt",
        "Greek" : "greek.txt",
        "Akkadian": "akkadian.txt",
        "Ancient" : "akkadian.txt",
        "Runes" : "runes.txt",
        "Dwarven" : "runes.txt",
        "Dwarf" : "runes.txt",
        "Elvish" : "sindarin.txt",
        "Elf" : "sindarin.txt",
        "Sindarin": "sindarin.txt",
    }

    # with open('latin.txt') as f:
    #     latin_words = f.readlines

    latin_words = (
    "exercitationem",
    "perferendis",
    "perspiciatis",
    "laborum",
    "eveniet",
    "sunt",
    "iure",
    "nam",
    "nobis",
    "eum",
    "cum",
    "officiis",
    "excepturi",
    "odio",
    "consectetur",
    "quasi",
    "aut",
    "quisquam",
    "vel",
    "eligendi",
    "itaque",
    "non",
    "odit",
    "tempore",
    "quaerat",
    "dignissimos",
    "facilis",
    "neque",
    "nihil",
    "expedita",
    "vitae",
    "vero",
    "ipsum",
    "nisi",
    "animi",
    "cumque",
    "pariatur",
    "velit",
    "modi",
    "natus",
    "iusto",
    "eaque",
    "sequi",
    "illo",
    "sed",
    "ex",
    "et",
    "voluptatibus",
    "tempora",
    "veritatis",
    "ratione",
    "assumenda",
    "incidunt",
    "nostrum",
    "placeat",
    "aliquid",
    "fuga",
    "provident",
    "praesentium",
    "rem",
    "necessitatibus",
    "suscipit",
    "adipisci",
    "quidem",
    "possimus",
    "voluptas",
    "debitis",
    "sint",
    "accusantium",
    "unde",
    "sapiente",
    "voluptate",
    "qui",
    "aspernatur",
    "laudantium",
    "soluta",
    "amet",
    "quo",
    "aliquam",
    "saepe",
    "culpa",
    "libero",
    "ipsa",
    "dicta",
    "reiciendis",
    "nesciunt",
    "doloribus",
    "autem",
    "impedit",
    "minima",
    "maiores",
    "repudiandae",
    "ipsam",
    "obcaecati",
    "ullam",
    "enim",
    "totam",
    "delectus",
    "ducimus",
    "quis",
    "voluptates",
    "dolores",
    "molestiae",
    "harum",
    "dolorem",
    "quia",
    "voluptatem",
    "molestias",
    "magni",
    "distinctio",
    "omnis",
    "illum",
    "dolorum",
    "voluptatum",
    "ea",
    "quas",
    "quam",
    "corporis",
    "quae",
    "blanditiis",
    "atque",
    "deserunt",
    "laboriosam",
    "earum",
    "consequuntur",
    "hic",
    "cupiditate",
    "quibusdam",
    "accusamus",
    "ut",
    "rerum",
    "error",
    "minus",
    "eius",
    "ab",
    "ad",
    "nemo",
    "fugit",
    "officia",
    "at",
    "in",
    "id",
    "quos",
    "reprehenderit",
    "numquam",
    "iste",
    "fugiat",
    "sit",
    "inventore",
    "beatae",
    "repellendus",
    "magnam",
    "recusandae",
    "quod",
    "explicabo",
    "doloremque",
    "aperiam",
    "consequatur",
    "asperiores",
    "commodi",
    "optio",
    "dolor",
    "labore",
    "temporibus",
    "repellat",
    "veniam",
    "architecto",
    "est",
    "esse",
    "mollitia",
    "nulla",
    "a",
    "similique",
    "eos",
    "alias",
    "dolore",
    "tenetur",
    "deleniti",
    "porro",
    "facere",
    "maxime",
    "corrupti",
)
    print (latin_words)
    
    return latin_words

def sentence(lang="Latin"):
    """
    Return a randomly generated sentence of lorem ipsum text.
    The first word is capitalized, and the sentence ends in either a period or
    question mark. Commas are added at random.
    """

    WORDS = import_language(lang)

    # Determine the number of comma-separated sections and number of words in
    # each section for this sentence.
    sections = [
        " ".join(random.sample(WORDS, random.randint(3, 12)))
        for i in range(random.randint(2, 5))
    ]
    s = ", ".join(sections)
    # Convert to sentence case and add end punctuation.
    return "%s%s%s" % (s[0].upper(), s[1:], random.choice("?."))


def paragraph(lang="Latin"):
    """
    Return a randomly generated paragraph of lorem ipsum text.
    The paragraph consists of between 2 to 4 sentences.
    """
    return " ".join(sentence(lang=lang) for i in range(random.randint(2, 4)))


def paragraphs(count=5, lang="Latin"):
    """
    Return a list of paragraphs as returned by paragraph(). the first
    paragraph will be the standard 'lorem ipsum' paragraph.
    """
    paras = []
    for i in range(count):
            paras.append(paragraph(lang=lang))
    return "\n".join(paras)


def words(count=5,lang="Latin"):
    """
    Returns lorem ipsum words separated by a single space.
    """
    WORDS = import_language(lang)

    word_list = []
    c = len(word_list)
    if count > c:
        count -= c
        while count > 0:
            c = min(count, len(WORDS))
            count -= c
            word_list += random.sample(WORDS, c)
    else:
        word_list = word_list[:count]

    return " ".join(word_list)
