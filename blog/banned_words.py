BANNED_WORDS = [
    'asshole',
    'bitch',
    'chink',
    'cunt',
    'dick',
    'dyke',
    'fag',
    'faggot',
    'fuck',
    'kill yourself',
    'nigga',
    'nigger',
    'raped',
    'shit',
]


def contains_banned_words(input):
    input = input.lower()
    return any(word in input for word in BANNED_WORDS)
