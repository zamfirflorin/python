results = []

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "is", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

while True:
    user_input = input("Say something : ")
    if user_input == '\end':
        break
    else: 
        results.append(sentence_maker(user_input))

print(" ".join(results))