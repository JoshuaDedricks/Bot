import tweepy
from translate import googleTranslate, stripper, strip_handle, strip_hashtag, packageMention


CONSUMER_KEY = 'R1PrxYTZ95iysyEbIdIWLPEZt'
CONSUMER_SECRET = '6N4fUwtdZcNPLX1tzqVarKEGfjFwqac1LBxVqFM1AvU9WJMlmC '
ACCESS_KEY = '1213366426557304834-iZEEbda4mMcn8UDNx6I0gxtflmxbdN'
ACCESS_SECRET = 'n93PNFB099yW5a3XOjqbZNe8y77jjWgTwbCECTZME6yGS'



## TODO:
# Remove Bot Handle
# Remove Language hashtag
# --Help for Help
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

def main():
    last_id = 0;
    break_id = 0;
    COUNTER = 0
    languages = {
        'ab': 'Abkhaz',
        'aa': 'Afar',
        'af': 'Afrikaans',
        'ak': 'Akan',
        'sq': 'Albanian',
        'am': 'Amharic',
        'ar': 'Arabic',
        'an': 'Aragonese',
        'hy': 'Armenian',
        'as': 'Assamese',
        'av': 'Avaric',
        'ae': 'Avestan',
        'ay': 'Aymara',
        'az': 'Azerbaijani',
        'bm': 'Bambara',
        'ba': 'Bashkir',
        'eu': 'Basque',
        'be': 'Belarusian',
        'bn': 'Bengali',
        'bh': 'Bihari',
        'bi': 'Bislama',
        'bs': 'Bosnian',
        'br': 'Breton',
        'bg': 'Bulgarian',
        'my': 'Burmese',
        'ca': 'Catalan; Valencian',
        'ch': 'Chamorro',
        'ce': 'Chechen',
        'ny': 'Chichewa; Chewa; Nyanja',
        'zh': 'Chinese',
        'cv': 'Chuvash',
        'kw': 'Cornish',
        'co': 'Corsican',
        'cr': 'Cree',
        'hr': 'Croatian',
        'cs': 'Czech',
        'da': 'Danish',
        'dv': 'Divehi; Maldivian;',
        'nl': 'Dutch',
        'dz': 'Dzongkha',
        'en': 'English',
        'eo': 'Esperanto',
        'et': 'Estonian',
        'ee': 'Ewe',
        'fo': 'Faroese',
        'fj': 'Fijian',
        'fi': 'Finnish',
        'fr': 'French',
        'ff': 'Fula',
        'gl': 'Galician',
        'ka': 'Georgian',
        'de': 'German',
        'el': 'Greek: Modern',
        'gn': 'Guaraní',
        'gu': 'Gujarati',
        'ht': 'Haitian',
        'ha': 'Hausa',
        'he': 'Hebrew modern',
        'hz': 'Herero',
        'hi': 'Hindi',
        'ho': 'Hiri Motu',
        'hu': 'Hungarian',
        'ia': 'Interlingua',
        'id': 'Indonesian',
        'ie': 'Interlingue',
        'ga': 'Irish',
        'ig': 'Igbo',
        'ik': 'Inupiaq',
        'io': 'Ido',
        'is': 'Icelandic',
        'it': 'Italian',
        'iu': 'Inuktitut',
        'ja': 'Japanese',
        'jv': 'Javanese',
        'kl': 'Kalaallisut',
        'kn': 'Kannada',
        'kr': 'Kanuri',
        'ks': 'Kashmiri',
        'kk': 'Kazakh',
        'km': 'Khmer',
        'ki': 'Kikuyu: Gikuyu',
        'rw': 'Kinyarwanda',
        'ky': 'Kirghiz: Kyrgyz',
        'kv': 'Komi',
        'kg': 'Kongo',
        'ko': 'Korean',
        'ku': 'Kurdish',
        'kj': 'Kwanyama: Kuanyama',
        'la': 'Latin',
        'lb': 'Luxembourgish',
        'lg': 'Luganda',
        'li': 'Limburgish',
        'ln': 'Lingala',
        'lo': 'Lao',
        'lt': 'Lithuanian',
        'lu': 'Luba-Katanga',
        'lv': 'Latvian',
        'gv': 'Manx',
        'mk': 'Macedonian',
        'mg': 'Malagasy',
        'ms': 'Malay',
        'ml': 'Malayalam',
        'mt': 'Maltese',
        'mi': 'Māori',
        'mr': 'Marathi Marāṭhī',
        'mh': 'Marshallese',
        'mn': 'Mongolian',
        'na': 'Nauru',
        'nv': 'Navajo: Navaho',
        'nb': 'Norwegian Bokmål',
        'nd': 'North Ndebele',
        'ne': 'Nepali',
        'ng': 'Ndonga',
        'nn': 'Norwegian Nynorsk',
        'no': 'Norwegian',
        'ii': 'Nuosu',
        'nr': 'South Ndebele',
        'oc': 'Occitan',
        'oj': 'Ojibwe: Ojibwa',
        'cu': 'Old Church Slavonic',
        'om': 'Oromo',
        'or': 'Oriya',
        'os': 'Ossetian: Ossetic',
        'pa': 'Punjabi',
        'pi': 'Pāli',
        'fa': 'Persian',
        'pl': 'Polish',
        'ps': 'Pashto: Pushto',
        'pt': 'Portuguese',
        'qu': 'Quechua',
        'rm': 'Romansh',
        'rn': 'Kirundi',
        'ro': 'Romanian: Moldavan',
        'ru': 'Russian',
        'sa': 'Sanskrit Saṁskṛta',
        'sc': 'Sardinian',
        'sd': 'Sindhi',
        'se': 'Northern Sami',
        'sm': 'Samoan',
        'sg': 'Sango',
        'sr': 'Serbian',
        'gd': 'Scottish Gaelic',
        'sn': 'Shona',
        'si': 'Sinhala: Sinhalese',
        'sk': 'Slovak',
        'sl': 'Slovene',
        'so': 'Somali',
        'st': 'Southern Sotho',
        'es': 'Spanish',
        'su': 'Sundanese',
        'sw': 'Swahili',
        'ss': 'Swati',
        'sv': 'Swedish',
        'ta': 'Tamil',
        'te': 'Telugu',
        'tg': 'Tajik',
        'th': 'Thai',
        'ti': 'Tigrinya',
        'bo': 'Tibetan',
        'tk': 'Turkmen',
        'tl': 'Tagalog',
        'tn': 'Tswana',
        'to': 'Tonga',
        'tr': 'Turkish',
        'ts': 'Tsonga',
        'tt': 'Tatar',
        'tw': 'Twi',
        'ty': 'Tahitian',
        'ug': 'Uighur: Uyghur',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'uz': 'Uzbek',
        've': 'Venda',
        'vi': 'Vietnamese',
        'vo': 'Volapük',
        'wa': 'Walloon',
        'cy': 'Welsh',
        'wo': 'Wolof',
        'fy': 'Western Frisian',
        'xh': 'Xhosa',
        'yi': 'Yiddish',
        'yo': 'Yoruba',
        'za': 'Zhuang: Chuang',
        'zu': 'Zulu'
    }

    with open('last_id.txt', 'r') as read_write:
        last_id = int(read_write.read())
    #try:
    for friend in tweepy.Cursor(api.mentions_timeline).items():
        COUNTER = COUNTER + 1
        if COUNTER == 1:
            break_id = friend.id
            with open('last_id.txt', 'w') as in_write:
                in_write.write(str(break_id))
        if friend.id != last_id:
            print(friend)
            if(friend.text.find('#') != -1):
                for iso, language in languages.items():
                    tag_language = '#' + language
                    if friend.text.lower().find(tag_language.lower()) != -1 :
                        filteredText = stripper(friend.text, language.lower())
                        translatedText = googleTranslate(filteredText, iso)
                        authorHandle = friend.author.screen_name
                        print (authorHandle)
                        api.update_status(packageMention(authorHandle, translatedText), friend.id)
                        break;

        else:
            break
    #except tweepy.TweepError:
    #    byteMe = 0
    main()


main()  ####### First time run
