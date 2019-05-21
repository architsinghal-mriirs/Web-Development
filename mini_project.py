from os import listdir #returns list of entries in the directory of the path ( listdr(path))
from os.path import isfile # isfile(path) returns true if the file exists
from os.path import join # join(path, *path) - concatenates path with *path ( check )

import string  #string manipulation

from nltk.tokenize import word_tokenize # for creating tokens
from nltk.corpus import stopwords  # for removing stop words

import spacy  # because nltk is not enough. also doesn't require pos tagging.


pos_files_path = 'C:/Users/Archit/aclImdb/train/pos/'  # path of the positive file training set
pos_files_list = [f for f in listdir(pos_files_path) if isfile(join(pos_files_path, f))] # creating a list of files

neg_files_path = 'C:/Users/Archit/aclImdb/train/neg/'
neg_files_list = [f for f in listdir(neg_files_path) if isfile(join(neg_files_path, f))]

#print(pos_files_list)
 #print(neg_files_list)

positive_reviews = []
negative_reviews = []

for file_name in pos_files_list:
    with open(pos_files_path+file_name, 'r') as file:
        positive_reviews.append(file.read().replace('\n', ''))

for file_name in neg_files_list:
    with open(neg_files_path+file_name, 'r') as file:
        negative_reviews.append(file.read().replace('\n', ''))

# print(positive_reviews[:2])
# print(negative_reviews[:2])


# Tokenization, Stop-words Removal and Lemmatization

stop_words = stopwords.words('english') + list(string.punctuation)

pos_tokens = []
for doc in positive_reviews:
    pos_tokens.append(word_tokenize(doc))

neg_tokens = []
for doc in negative_reviews:
    neg_tokens.append(word_tokenize(doc))

for ti in range(len(pos_tokens)):
    pos_tokens[ti] = [i for i in pos_tokens[ti] if i.lower() not in stop_words]

for ti in range(len(neg_tokens)):
    neg_tokens[ti] = [i for i in neg_tokens[ti] if i.lower() not in stop_words]

spacyProcessor = spacy.load('en', disable=['parser', 'ner'])

pos_lemmatized_tokens = []
for doc_tokens in pos_tokens:
    sp_doc = spacyProcessor(" ".join([token for token in doc_tokens]))
    pos_lemmatized_tokens.append([token.lemma_ for token in sp_doc])

neg_lemmatized_tokens = []
for doc_tokens in neg_tokens:
    sp_doc = spacyProcessor(" ".join([token for token in doc_tokens]))
    neg_lemmatized_tokens.append([token.lemma_ for token in sp_doc])

preprocessed_positive_reviews = []
for doc_tokens in pos_lemmatized_tokens:
    preprocessed_positive_reviews.append(" ".join([tokens for tokens in doc_tokens]))

preprocessed_negative_reviews = []
for doc_tokens in neg_lemmatized_tokens:
    preprocessed_negative_reviews.append(" ".join([tokens for tokens in doc_tokens]))

print(preprocessed_positive_reviews[:2])
print(preprocessed_negative_reviews[:2])