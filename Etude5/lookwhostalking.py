# The following program is designed to take a sentence/input from stdin and output
# the Māori translation.
# First it takes a sentence and confirms its formatting
# Then it translates the checked sentence with respect to the pronoun,
# people present, tense, and verb.
# @Yashna Shetty
# @Remin Reji Mathew

import sys
import re

# function called if pronoun used is "i"


def pronoun_i(verbs_for_am, verbs_for_will, verbs_without_tenses, pronoun, tense, word, whoPeople):
    if whoPeople == None:
        if tense == "am":
            if word in verbs_for_am:
                return True
        elif tense == "will":
            if word in verbs_for_will:
                return True
        elif tense == pronoun:
            if word in verbs_without_tenses:
                return True
        return "wrong tense"
    return "please do not specify who is speaking for this pronoun"

# function called if pronoun used is "they"


def pronoun_they(verbs_for_am, verbs_for_will, verbs_without_tenses, pronoun, tense, word, whoPeople):
    if whoPeople == "excl":
        if tense == "are":
            if word in verbs_for_am:
                return True
        if tense == "will":
            if word in verbs_for_will:
                return True
        if tense == pronoun:
            if word in verbs_without_tenses:
                return True
        return "wrong tense"
    return "please specify who is speaking - you also cannot include the listener for this pronoun"

# function called if pronoun used is "you"


def pronoun_you(verbs_for_am, verbs_for_will, verbs_without_tenses, pronoun, tense, word, whoPeople):
    if whoPeople == None or whoPeople == "incl":
        if tense == "are":
            if word in verbs_for_am:
                return True
        if tense == "will":
            if word in verbs_for_will:
                return True
        if tense == pronoun:
            if word in verbs_without_tenses:
                return True
        return "wrong tense"
    return "you cannot exclude the listener with this pronoun"

# function called if pronoun used is "we"


def pronoun_we(verbs_for_am, verbs_for_will, verbs_without_tenses, pronoun, tense, word, whoPeople):
    if whoPeople == "incl" or whoPeople == "excl":
        if tense == "are":
            if word in verbs_for_am:
                return True
        if tense == "will":
            if word in verbs_for_will:
                return True
        if tense == pronoun:
            if word in verbs_without_tenses:
                return True
        return "wrong tense"
    return "please specify who's talking"

# function called if pronoun used is "she" or "he"


def pronoun_she_he(verbs_for_am, verbs_for_will,
                   special_case_curr_verbs, special_case_past_verbs, pronoun, tense, word, whoPeople):
    if whoPeople == None:
        if tense == "is":
            if word in verbs_for_am:
                return True
        if tense == "will":
            if word in verbs_for_will:
                return True
        if tense == pronoun:
            if word in special_case_curr_verbs:
                return True
            elif word in special_case_past_verbs:
                return True
        return "wrong tense"
    return "please do not specify who is speaking"

# function checks that the english sentence is in the correct format


def check_sentence(pronoun, tense, word, numPeople, whoPeople):
    verbs_for_will = ["go", "make", "see",
                      "want", "call", "ask", "read", "learn"]
    verbs_for_am = ["going", "making", "seeing", "wanting",
                    "calling", "asking", "reading", "learning"]
    verbs_without_tenses = ["go", "went", "make", "made", "see", "saw", "want",
                            "wanted", "call", "called", "ask", "asked", "read", "learn", "learned", "learnt"]
    special_case_curr_verbs = ["goes", "makes", "sees",
                               "wants", "calls", "asks", "reads", "learns"]
    special_case_past_verbs = [
        "went", "made", "saw", "wanted", "called", "asked", "read", "learned", "learnt"]

    if whoPeople != None:
        if numPeople == 0:
            return "you have specified who is speaking, please specify how many"
    if not isinstance(numPeople, int):
        return "bad number!"
    if word not in verbs_for_will and word not in verbs_for_am and word not in verbs_without_tenses and word not in special_case_curr_verbs and word not in special_case_past_verbs:
        return "wrong verb!"

    if pronoun == "i":
        return pronoun_i(verbs_for_am, verbs_for_will, verbs_without_tenses,
                         pronoun, tense, word, whoPeople)
    if pronoun == "you":
        return pronoun_you(verbs_for_am, verbs_for_will,
                           verbs_without_tenses, pronoun, tense, word, whoPeople)
    if pronoun == "she" or pronoun == "he":
        return pronoun_she_he(verbs_for_am, verbs_for_will,
                              special_case_curr_verbs, special_case_past_verbs, pronoun, tense, word, whoPeople)
    if pronoun == "we":
        return pronoun_we(verbs_for_am, verbs_for_will,
                          verbs_without_tenses, pronoun, tense, word, whoPeople)
    if pronoun == "they":
        return pronoun_they(verbs_for_am, verbs_for_will,
                            verbs_without_tenses, pronoun, tense, word, whoPeople)
    else:
        return "wrong pronoun"

# function called to translate the checked pronoun


def translate_checked_pronoun(pronoun, numPeople, whoPeople):
    if pronoun == "i":
        sentence_ender = "au"
    elif pronoun == "we":
        if numPeople == 1:
            return "wrong pronoun"
        elif numPeople == 2:
            if whoPeople == "incl":
                sentence_ender = "tāua"
            elif whoPeople == "excl":
                sentence_ender = "māua"
        elif numPeople >= 3:
            if whoPeople == "incl":
                sentence_ender = "tātou"
            elif whoPeople == "excl":
                sentence_ender = "mātou"
    elif pronoun == "you":
        if numPeople == 0 or numPeople == 1:
            sentence_ender = "koe"
        elif numPeople == 2:
            sentence_ender = "kōrua"
        elif numPeople >= 3:
            sentence_ender = "koutou"
    elif pronoun == "they":
        if numPeople == 1:
            return "wrong pronoun"
        elif numPeople == 2:
            sentence_ender = "rāua"
        elif numPeople >= 3:
            sentence_ender = "rātou"
    elif pronoun == "he" or pronoun == "she":
        sentence_ender = "ia"
    else:
        return "wrong pronoun"
    return sentence_ender

# function called to translate the checked tense


def translate_checked_tense(tense, verb, pronoun):
    past_tense_verbs = ["went", "made", "saw", "wanted",
                        "called", "asked", "learnt", "learned"]
    if verb in past_tense_verbs:
        sentence_starter = "I"
    elif tense == "will":
        sentence_starter = "Ka"
    elif tense == pronoun:
        if verb == "read":
            sentence_starter = "I"
        else:
            sentence_starter = "Kei te"
    elif tense == "am" or tense == "are" or tense == "is":
        sentence_starter = "Kei te"
    else:
        return "wrong tense"
    return sentence_starter

# function called to translate the checked verb


def translate_checked_verb(verb):
    if verb == "go" or verb == "going" or verb == "goes" or verb == "went":
        sentence_mid = "haere"
    elif verb == "make" or verb == "made" or verb == "making" or verb == "makes":
        sentence_mid = "hanga"
    elif verb == "see" or verb == "saw" or verb == "seeing" or verb == "sees":
        sentence_mid = "kite"
    elif verb == "wanted" or verb == "want" or verb == "wanting" or verb == "wants":
        sentence_mid = "hiahia"
    elif verb == "call" or verb == "called" or verb == "calling" or verb == "calls":
        sentence_mid = "karanga"
    elif verb == "ask" or verb == "asked" or verb == "asking" or verb == "asks":
        sentence_mid = "pātai"
    elif verb == "read" or verb == "reading" or verb == "reads":
        sentence_mid = "pānui"
    elif verb == "learn" or verb == "learning" or verb == "learnt" or verb == "learned" or verb == "learns":
        sentence_mid = "ako"
    else:
        return "wrong verb"
    return sentence_mid

# main function that prints the introductory message to the user


def main():
    print("Welcome! This program takes a simple sentence and translates it into Māori.\n")
    print(
        "Please follow the following syntax: [Pronoun] [(no. of people being referred to \"incl\" or \"excl\")] [tense] [verb]\n")
    print("To quit the program, please type \"quit\"")
    main2()

# second main function that takes input from stdin and calls
# the appropriate functions to check and translate
# the given input.


def main2():
    for line in sys.stdin:
        line = line.strip().lower()
        numIndex = line.find("(")
        numIndex2 = line.find(")")
        numPeople = 0
        whoPeople = None
        if numIndex != -1 and numIndex2 != -1:
            specPeople = line[numIndex+1:numIndex2]
            for s in specPeople.split():
                if s.isdigit():
                    numPeople = s
                else:
                    whoPeople = s
            try:
                numPeople = int(numPeople)
            except ValueError:
                numPeople = numPeople
            numIndex2 = line.find(")")
            newSentence = line[0:numIndex] + " " + line[numIndex2+1:]
            whoPeople = line[numIndex2-4:numIndex2]

            wordlist = re.split("[\s\\n]", newSentence)
        else:
            wordlist = re.split("[\s\\n]", line)
        finList = []
        for word in wordlist:
            if word.strip():
                finList.append(word)
        for txt in finList:
            if len(finList) == 1:
                if txt == "quit":
                    quit()
                else:
                    print(
                        "This isn't a recognisable sentence. Please try a new sentence")
                    main2()

        if check_sentence(finList[0], finList[-2], finList[-1], numPeople, whoPeople) == True:
            if translate_checked_pronoun(finList[0], numPeople, whoPeople) != "wrong pronoun":
                if translate_checked_tense(finList[-2], finList[-1], finList[0]) != "wrong tense":
                    if translate_checked_verb(finList[-1]) != "wrong verb":
                        print(translate_checked_tense(finList[-2], finList[-1], finList[0]) + " " +
                              translate_checked_verb(finList[-1]) + " " + translate_checked_pronoun(finList[0], numPeople, whoPeople))
                    else:
                        print(translate_checked_verb(finList[-1]))
                else:
                    print(translate_checked_tense(
                        finList[-2], finList[-1], finList[0]))
            else:
                print(translate_checked_pronoun(
                    finList[0], numPeople, whoPeople))
        else:
            print(check_sentence(finList[0], finList[-2],
                                 finList[-1], numPeople, whoPeople))


main()
