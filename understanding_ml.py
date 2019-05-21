import pandas as pd
from sklearn.linear_model import LogisticRegression


######################################
# Problem Statement
######################################


# Detect if a string is a numerical value or not using ML
#   Example Input   : 'The clients are going to visit again in 2 days!'
#   Expected Output : not a number
#   Example Input   : '3.141592654'
#   Expected Output : is a number


######################################
# Objective
######################################


# Understand ML at the foundation level.
#   Understand what ML really does, what it can do and cannot do.
#   Understand the importance of data in ML and how the quality of data impacts the degree of learning.


######################################
# Data for training
######################################


positive_samples_set1 = ['1', '2', '3', '4', '10', '11.12']
negative_samples_set1 = ['a', 'b', 'cd', 'ef', 'abc', 'namoraga'] # lol NAMO forever <3 !!!

positive_samples_set2 = ['1', '12', '4294967296', '123.45', '12345.6789', '.33333333333333']
negative_samples_set2 = ['the', ',', '!#@$', 'how are you', '3idiots', '1.2.3.4.5.6.']


######################################
# Data for prediction (testing)
######################################


#prediction_raw_data = ['23', '2000', '12345678', '1.1', '3.141592654',
 #                      '123.45.67', '192.168.0.97', 'KA03L9291', 'madam july',
  #                     'we made 300 in 12 minutes']

prediction_raw_data = ['23', '2000', '12345678', '1.1']

######################################
# Approach to solution
######################################

# A token is a running sequence of digits or letters, split at any symbols or space
# The splitting character is also treated as a separate token -> meaning a space or a comma is also treated as a token

# Generate feature vectors for training data
# 2 features for each token: pairs of (type, length) -> types defined below
#   
# 
                        # type codes: 
                        # 0 -> digits or '.', 
                        # 1 -> letters, 
                        # 2 -> symbols (except '.') or mixed

# Examples: 'input' : type, length

#   '1'           : 0, 1
#   '12'          : 0, 2
#   '123.45'      : 0, 3, 0, 1, 0, 2
#   'the'         : 1, 3
#   'how are you' : 1, 3, 2, 1, 1, 3, 2, 1, 1, 3
#   '3idiots'     : 2, 7


######################################
# Function definitions
######################################


def get_type(token):
    is_number = True
    is_alpha = True
    for char in token:
        char_code = ord(char.lower()) # ord is used to find ascii code. storing the code in char_code.
        if (char_code != 46) and (char_code < 48 or char_code > 57): # if not a dot AND not a number then set is_number to false.
            is_number = False
        if char_code < 97 or char_code > 122: # if not a small alphabet then set is_alpha to false.
            is_alpha = False
    if is_number:
        return 0            #number mapped to 0;
    if is_alpha:
        return 1                # alphabet mapped to 1;
    return 2                    # everything else mapped to 2;


def tokenize(input_string):
    tokens = []
    token = ''
    for char in input_string:
        char_code = ord(char.lower()) #deals with capital letters as well
        if (char_code > 96 and char_code < 123) or (char_code > 47 and char_code < 58):
            token = token + char  # creating a token 
        else:
            tokens.append(token)
            tokens.append([char])
            token = ''
    tokens.append(token)
    tokens = list(filter(None, tokens))  # filtering blank values and retunring the tokens.
    return tokens


def featurize(input_string):
    tokens = tokenize(input_string)
    token_features = []
    for token in tokens:
        token_features.append(get_type(token))
        token_features.append(len(token))
    token_count = len(tokens)
    for i in range(20 - token_count):
        token_features.append(-1)
        token_features.append(-1)
    return token_features


def build_data(raw_data, training, label=0):
    x = []
    y = []
    for data in raw_data:
        x.append(featurize(data))
        if training:
            y.append(label)
    if training:
        return x, y
    else:
        return x


######################################
# Build datasets that we can feed to our models for training
######################################


x1p, y1p = build_data(raw_data=positive_samples_set1, training=True, label=1)
x1n, y1n = build_data(raw_data=negative_samples_set1, training=True, label=0)
x2p, y2p = build_data(raw_data=positive_samples_set2, training=True, label=1)
x2n, y2n = build_data(raw_data=negative_samples_set2, training=True, label=0)

X1 = pd.DataFrame(x1p + x1n)
Y1 = y1p + y1n
X2 = pd.DataFrame(x2p + x2n)
Y2 = y2p + y2n


######################################
# Train models
######################################


clf_lgrg1 = LogisticRegression(random_state=10, solver='liblinear')
clf_lgrg1.fit(X1, Y1)

clf_lgrg2 = LogisticRegression(random_state=10, solver='liblinear')
clf_lgrg2.fit(X2, Y2)


######################################
# Build prediction dataset and run predictions using the models we have built
######################################


new_X = pd.DataFrame(build_data(raw_data=prediction_raw_data, training=False))

prediction_clf_lgrg1 = clf_lgrg1.predict(new_X)
prediction_clf_lgrg2 = clf_lgrg2.predict(new_X)


######################################
# Display the results from the models
######################################


print('\n\n{:>60}\t{:>25}\t{:>25}'.format('String', 'Model1: Number?', 'Model2: Number?'))
i = 0
for s in prediction_raw_data:
    print('{:>60}\t{:>25}\t{:>25}'.format(s,
                                          'Yes' if prediction_clf_lgrg1[i] else 'No',
                                          'Yes' if prediction_clf_lgrg2[i] else 'No'))
    i += 1

