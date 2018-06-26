import random

def generate_compliment():

    #part1 of the sentence---noun/subject
    part1 = [
        "you",
    ]

    #part2 of the sentence--the verb/action
    part2 = [
        "are",
    ]

    #part3 of the sentence--the ending(noun)
    part3 = [
        "extremely intuitive",
        "a searcher of hidden meanings",
        "sensitive and perceptive",
        "gifted at reading others",
        "a holder of strong convictions and beliefs",
        "a person who will not compromise their ideals",
        "genuinely warm and affirming by nature",
        "capable of trusting your own instincts (and with good reason)",
        "usually right and you usually know it",
        "typically gentle and caring",
        "usually have good communication skills",
        "a gifted writer",
        "committed and you take commitment seriously",
        "the reason why I admire you deeply",
        "a seeker of lifelong relationships",
        "a good listener",
        "deep, complex and intense",
        "artistic and creative",
        "a inspirator, a motivator, an achiever",
        "extremely insightful about people and situations",
        "a Perfectionist",
        "natural nurturer",
        "devoted to and protective of those they care about",
        "the rarest of all types",
        "an independent worker",
        "in some ways, be easy-going",
        "everything I want to be",
        "very important to me",
        "not a failure",
        "special and idiosyncratic (heh, in a good way)",
        "beautiful, not just outside, but deep inside as well",
        "the person I want to risk myself for because God risk Himself on me",
        "perfection, even the sun is jealous of the way you shine",
        "so kind to others",
        "a believer that there is good in this world",
        "constantly racing through my mind",
        "the next Victoria Secret Model",
        "loved always",
        "pretty, witty, and gracious",
        "important",
        "geniune and sincere",
        "one I went to spend my time with, even the future",
        "hotter than donut grease",
        "a snack",

    ]

    # this will shuffle the lists
    random.shuffle(part1)
    random.shuffle(part2)
    random.shuffle(part3)

    n = 1
    # concatinate the parts of the sentences
    list_of_sentences = []
    for word in range(n):
            try:
                    list_of_sentences = part1[word] + ' ' + part2[word] + ' ' + part3[word]
                    list_of_sentences += '.'
            except IndexError:
                    break
    return list_of_sentences
