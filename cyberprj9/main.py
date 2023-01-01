import pandas as pd
import string
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

emails = [[0, 'Hello, how are you!'], 
            [1, 'Win epic prices today, win from home.'], 
            [0, 'Call me now. I need to speak with you'], 
            [0, 'Can we have a meeting at your place tomorrow?']]

df = pd.DataFrame(np.array(emails), columns=['tag', 'mail_message'])

print(df.head())

x_train, x_test, y_train, y_test = train_test_split(df['mail_message'], df['tag'], random_state=1)

print('Number of rows in the total set: {}'.format(df.shape[0]))
print('Number of rows in the training set: {}'.format(x_train.shape[0]))
print('Number of rows in the test set: {}'.format(x_test.shape[0]))

count_vector = CountVectorizer()

trainiing_data = count_vector.fit_transform(x_train)
print(trainiing_data)
print(count_vector.get_feature_names_out())

testing_data = count_vector.transform(x_test)

naive_bayes = MultinomialNB()
naive_bayes.fit(trainiing_data, y_train)

predictions = naive_bayes.predict(testing_data)

print('the prediction was: ', predictions)
print('Accuracy score: ', format(accuracy_score(y_test, predictions)))