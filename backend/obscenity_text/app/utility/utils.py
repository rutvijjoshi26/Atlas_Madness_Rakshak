import string 
from cleantext import clean
import re
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
import nltk
from nltk.stem import WordNetLemmatizer





def remove_punctuations(x):
  x=x.translate(str.maketrans("","",string.punctuation))
  x.lower()
  return x

def final_preprocess_text(x):
  return clean(x,no_emoji=True,replace_with_url="<URL>",replace_with_email="<EMAIL>",fix_unicode=True, no_line_breaks=True)


def remove_numbers(text):
    return re.sub(r'\d+', '', text)


def remstopwwords(text):
    result = []
    for token in simple_preprocess(text):
        if token not in STOPWORDS and len(token) > 3:
            result.append(token)
    return " ".join(result)


def rem_spec_chars(x):
  x = x.replace('\r', ' ').replace(" 's",' ').replace('user',' ')
  return x


def lemma(text):
  tokens = nltk.word_tokenize(text)
  lemmatizer = WordNetLemmatizer()

  lemmatized_tokens = []
  for token in tokens:
    pos = nltk.pos_tag([token])[0][1][0].lower() # get the POS tag and convert to simplified format used by WordNet lemmatizer
    if pos in ['n', 'v', 'a', 'r']: # check if the POS tag is a noun, verb, adjective or adverb
        lemma = lemmatizer.lemmatize(token, pos=pos) # lemmatize the token with the appropriate POS tag
        lemmatized_tokens.append(lemma)
    else:
        lemmatized_tokens.append(token)

  return " ".join(lemmatized_tokens)


def preprocess_test(text_line):
   text_line=remove_punctuations(text_line)
   text_line=final_preprocess_text(text_line)
   text_line=remove_numbers(text_line)
   text_line=remstopwwords(text_line)
   text_line=lemma(text_line)

   return text_line