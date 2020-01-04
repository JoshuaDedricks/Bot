from google.cloud import translate_v2 as translate

while_recurse_key = 0
BOT_HANDLE = '@joshuadedricks'

def strip_handle(text):
    text = text.replace(BOT_HANDLE, "")
    return text
# --- End of Method

def strip_hashtag(text, language):
    global while_recurse_key
    lowerCase = text.lower()
    strippedText = []
    l = 0
    t = 0
    pos = 0
    t = lowerCase.find('#', while_recurse_key, len(text))
    pos = t
    t = t + 1
    while_recurse_key = t

    try:
        while(lowerCase[t] and language[l]):
            if lowerCase[t] == language[l]:
                l = l + 1
                t = t + 1
            else:
                strip_hashtag(text, language)
    except IndexError:
        while_recurse_key = 0

    endOfHashtagPos = pos + len(language) + 1
    i = 0
    try:
        while i < len(text):
            if i not in range(pos, endOfHashtagPos):
                strippedText.append(text[i])
            i = i + 1
    except IndexError:
        print ('')
    return (''.join(strippedText))
# --- End of method

def stripper(text, language):
    strippedHashtag = strip_hashtag(text, language)
    strippedHandle = strip_handle(strippedHashtag)

    stripText = strippedHandle.strip()
    return stripText
# --- End of Method

def googleTranslate(text, target):
    translateClient = translate.Client()
    result = translateClient.translate(text, target_language = target)
    result = result['translatedText']
    return result

# --- End of Method

def packageMention(author, text):
    tweet = "@"+author+" "+text
    return tweet
