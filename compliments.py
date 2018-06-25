import random

def generate_compliment():

    #part1 of the sentence---noun/subject
    part1 = [
        "You",
    ]

    #part2 of the sentence--the verb/action
    part2 = [
        "are",
    ]

    #part3 of the sentence--the ending(noun)
    part3 = [
        "Extremely intuitive",
        "A searcher of hidden meanings",
        "Sensitive and perceptive",
        "Gifted at reading others",
        "A holder of strong convictions and beliefs",
        "A person who will not compromise their ideals",
        "Genuinely warm and affirming by nature",
        "Capable of trusting your own instincts (and with good reason)",
        "Usually right and you usually know it",
        "Typically gentle and caring",
        "Usually have good communication skills",
        "A gifted writer",
        "Committed and you take commitment seriously",
        "The reason why I admire you deeply",
        "A seeker of lifelong relationships",
        "A good listener",
        "Deep, complex and intense",
        "Artistic and creative",
        "A inspirator, a motivator, an achiever",
        "Extremely insightful about people and situations",
        "a Perfectionist",
        "Natural nurturer",
        "Devoted to and protective of those they care about",
        "The rarest of all types",
        "An independent worker",
        "In some ways, be easy-going",
        "Everything I want to be",
        "Very important to me",
        "Not a failure",
        "Special and idiosyncratic (heh, in a good way)",
        "Beautiful, not just outside, but deep inside as well",
        "The person I want to risk myself for because God risk Himself on me",
        "Perfection, even the sun is jealous of the way you shine",
        "So kind to others",
        "A believer that there is good in this world",
        "Constantly racing through my mind",
        "The next Victoria Secret Model",
        "Loved always",
        "Pretty, witty, and gracious",
        "Important",
        "Geniune and sincere",
        "One I went to spend my time with, even the future",
        "Hotter than donut grease",

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
                    list_of_sentences = list_of_sentences.capitalize() + '. '
            except IndexError:
                    break
    return list_of_sentences
