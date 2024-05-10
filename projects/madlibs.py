import random

sentences = [
    "The [adjective] cat [verb] over the [adjective] moon.",
    "[Exclamation]! I [verb] in my [noun]!",
    "The [adjective] [noun] [verb] [adverb] through the [adjective] forest.",
    "The [adjective] [noun] [verb] [adverb] over the [adjective] [noun].",
    "[Name] [verb] to the top of the [noun] and shouted, '[Exclamation]!'",
    "[Name] was so [adjective] that they [verb] their [noun] on the [noun].",
    "The [adjective] [noun] [verb] [adverb] down the [adjective] road.",
    "[Exclamation]! Look at that [adjective] [noun]!"
]

def fill_in(sentence):
    placeholders = ["[adjective]", "[verb]", "[noun]", "[adverb]", "[Exclamation]", "[Name]",]
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder[1:-1]}: ")
        sentence = sentence.replace(placeholder, user_input)
    return sentence

random_sentence = random.choice(sentences)

filled_sentence = fill_in(random_sentence)
print(filled_sentence)
