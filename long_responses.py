import random

R_FAT = "I neither have mass nor weight because I am a bot. \n " \
        "Maybe don't try to project your insecurities on others. :p"

def unknown():
    response = ['Could you please rephrase that?', "...",
                "Sounds about right", "What does that mean?",
                "Incomprehensible statement"][random.randrange(5)]
    return response