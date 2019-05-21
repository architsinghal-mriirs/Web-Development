from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import string

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.corpus import wordnet     # constants wordnet.NOUN, wordnet.VERB

from nltk import pos_tag

from nltk import PorterStemmer
from nltk import SnowballStemmer

from nltk.stem.wordnet import WordNetLemmatizer

import spacy


# Document Corpus

dc = ['The quick brown fox jumped over the lazy dog!',
      'I hope you are enjoying this class!',
      'An apple fell on Rishabh\'s head.',
      'This is quite an enjoyable course, hopefully it is also useful.',
      'The striped bats are hanging on their feet for best and ate best fishes.',
      'Following mice attacks, caring farmers were marching to Delhi for better living conditions.']


# Tokenization

tokens = []

for doc in dc:
    tokens.append(word_tokenize(doc))

tokens_all = tokens.copy()


# Stop-words removal

stop_words = stopwords.words('english') + list(string.punctuation)
for ti in range(len(tokens)):
    tokens[ti] = [i for i in tokens[ti] if i.lower() not in stop_words]


# Stemming, POS and Lemmatization

porterStemmer = PorterStemmer()
sbStemmer = SnowballStemmer('english')
wnLemmatizer = WordNetLemmatizer()
spacyProcessor = spacy.load('en', disable=['parser', 'ner'])

porter_stemmed_tokens = []
sb_stemmed_tokens = []
wn_lemmatized_tokens = []
sp_lemmatized_tokens = []
tokens_pos = []
row = 0

tag_dict = {
    "J": wordnet.ADJ,
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "R": wordnet.ADV
}

for doc_tokens in tokens:

    ps = []
    ss = []
    wl = []

    tokens_pos.append(pos_tag(doc_tokens))

    sp_doc = spacyProcessor(" ".join([token for token in doc_tokens]))
    sp_lemmatized_tokens.append([token.lemma_ for token in sp_doc])

    for i in range(len(doc_tokens)):

        ps.append(porterStemmer.stem(doc_tokens[i]))
        ss.append(sbStemmer.stem(doc_tokens[i]))

        wl.append(wnLemmatizer.lemmatize(doc_tokens[i], tag_dict.get(tokens_pos[row][i][1][0], wordnet.NOUN)))

    porter_stemmed_tokens.append(ps)
    sb_stemmed_tokens.append(ss)

    wn_lemmatized_tokens.append(wl)

    row = row + 1

# print(tokens_pos)

print('\nAll tokens:\n\t', tokens_all)
print('Stopwords removed tokens:\n\t', tokens)
print('\nPorter Stemmed tokens:\n\t', porter_stemmed_tokens)
print('Snowball Stemmed tokens:\n\t', sb_stemmed_tokens)
print('\nWordnet Lemmatized tokens:\n\t', wn_lemmatized_tokens)
print('Spacy Lemmatized tokens:\n\t', sp_lemmatized_tokens)


# Create a new document corpus with the filtered and stemmed / lemmatized tokens
# We'll select Spacy's lemmatized tokens as it seems to be better

ndc = []
for doc_tokens in sp_lemmatized_tokens:
    ndc.append(" ".join([tokens for tokens in doc_tokens]))

# Text Vectorization (Featurization) using Counts and TF-IDF

count_vectorizer = CountVectorizer()
tfidf_vectorizer = TfidfVectorizer()

count_vectorizer.fit(ndc)
tfidf_vectorizer.fit(ndc)

# print(count_vectorizer.vocabulary_)
# print(tfidf_vectorizer.vocabulary_)
# print(tfidf_vectorizer.idf_)

count_vector = count_vectorizer.transform(ndc)
tfidf_vector = tfidf_vectorizer.transform(ndc)

# print(count_vector.shape)
# print(count_vector.toarray())
# print(tfidf_vector.shape)
# print(tfidf_vector.toarray())


# Create a truth vector for classification training

doc_class = {
    'nursery': 0,
    'junior': 1,
    'senior': 2
}

# Add more labels to dc_truth if you add more documents to the corpus (dc)
dc_truth = ['nursery', 'junior', 'junior', 'junior', 'senior', 'senior']

Y_train = [doc_class.get(i) for i in dc_truth]


# Training

X_train_cv = count_vector
X_train_tv = tfidf_vector

nb_clf_model_cv = MultinomialNB().fit(X_train_cv, Y_train)
nb_clf_model_tv = MultinomialNB().fit(X_train_tv, Y_train)


# Evaluation

print('\n\nModel Evaluation:\n')

eval_dc = ['A lazy man is a crazy man!',
           'The course of our actions today make memories of yesterday.',
           'Attacking our farmers is like attacking our country.']

eval_dc_truth = ['nursery', 'junior', 'senior']
Y_test = [doc_class.get(i) for i in eval_dc_truth]

eval_tokens = []
for doc in eval_dc:
    eval_tokens.append(word_tokenize(doc))

for ti in range(len(eval_tokens)):
    eval_tokens[ti] = [i for i in eval_tokens[ti] if i.lower() not in stop_words]

eval_lemmatized_tokens = []
for doc_tokens in eval_tokens:
    sp_doc = spacyProcessor(" ".join([token for token in doc_tokens]))
    eval_lemmatized_tokens.append([token.lemma_ for token in sp_doc])

eval_ndc = []
for doc_tokens in eval_lemmatized_tokens:
    eval_ndc.append(" ".join([tokens for tokens in doc_tokens]))

print('\tPreprocessed tokens:\n\t\t', eval_ndc)

X_test_cv = count_vectorizer.transform(eval_ndc)
X_test_tv = tfidf_vectorizer.transform(eval_ndc)

Y_pred_cv = nb_clf_model_cv.predict(X_test_cv)
Y_pred_tv = nb_clf_model_tv.predict(X_test_tv)

nb_clf_model_cv_acc = accuracy_score(Y_test, Y_pred_cv)
nb_clf_model_tv_acc = accuracy_score(Y_test, Y_pred_tv)

print('\tAccuracy of classifier using CountVectorizer features: {:>2.2f}'.format(nb_clf_model_cv_acc))
print('\tAccuracy of classifier using TFIDFVectorizer features: {:>2.2f}'.format(nb_clf_model_tv_acc))
