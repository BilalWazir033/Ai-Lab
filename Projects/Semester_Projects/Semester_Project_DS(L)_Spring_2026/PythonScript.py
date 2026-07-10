# %% [markdown]
# # SMS Spam Detection using Machine Learning
# 
# ## Introduction
# Spam messages are unwanted messages that often contain advertisements, scams, or phishing links. This project builds a machine learning model to automatically classify SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP).
# 
# ## Objectives
# - Clean and preprocess SMS text data.
# - Perform Exploratory Data Analysis (EDA).
# - Convert text into numerical features using TF-IDF.
# - Train different Naive Bayes classifiers.
# - Evaluate the models and select the best-performing one.
# - Deploy the trained model as a web application using Streamlit.

# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("spam.csv", encoding="latin-1")
df.head()

# %%
df.sample(5)

# %%
df.shape

# %%
# 1. Data cleaning
# 2. EDA
# 3. Text Preprocessing
# 4. Model building
# 5. Evaluation
# 6. Improvement
# 7. Website
# 8. Deploy

# %% [markdown]
# # 1. Data Cleaning
# 
# The dataset was cleaned before training the model.
# 
# Steps performed:
# - Removed unnecessary columns.
# - Renamed the columns for better readability.
# - Encoded the target labels (Spam = 1, Ham = 0).
# - Checked for missing values.
# - Removed duplicate records.

# %%
df.info()

# %%
# drop last 3 cols as much of it are null
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)

# %%
df.sample(5)

# %%
# renaming the cols
df.rename(columns={'v1':'target','v2':'text'},inplace=True)
df.sample(5)

# %%
# encode the target column
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# %%
# spam=1, ham=0
df['target'] = encoder.fit_transform(df['target'])

# %%
df.head()

# %%
# missing values
df.isnull().sum()

# %%
# check for duplicate values
df.duplicated().sum()

# %%
# remove duplicates
df = df.drop_duplicates(keep='first')

# %%
df.duplicated().sum()

# %%
df.shape

# %% [markdown]
# # 2. Exploratory Data Analysis (EDA)
# 
# EDA was performed to understand the dataset.
# 
# The following analyses were carried out:
# - Distribution of Spam and Ham messages.
# - Number of characters.
# - Number of words.
# - Number of sentences.
# - Histograms for message length.
# - Pair plot of numerical features.
# - Correlation heatmap.

# %%
df.head()

# %%
df['target'].value_counts()

# %%
import matplotlib.pyplot as plt
plt.pie(df['target'].value_counts(), labels=['ham','spam'],autopct="%0.2f")
plt.show()

# %%
# Data is imbalanced

# %%
import nltk # natural language tool kit

# %%
# !pip install nltk

# %%
nltk.download('punkt')
nltk.download('punkt_tab')

# %%
df['num_characters'] = df['text'].apply(len)

# %%
df.head()

# %%
# num of words
df['num_words'] = df['text'].apply(lambda x:len(nltk.word_tokenize(x)))

# %%
df.head()

# %%
df['num_sentences'] = df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))

# %%
df.head()

# %%
df[['num_characters','num_words','num_sentences']].describe()

# %%
# ham
df[df['target'] == 0][['num_characters','num_words','num_sentences']].describe()

# %%
#spam
df[df['target'] == 1][['num_characters','num_words','num_sentences']].describe()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%
plt.figure(figsize=(10,6))

sns.histplot(df[df['target'] == 0]['num_characters'],label='Ham')

sns.histplot(df[df['target'] == 1]['num_characters'],color='red',label='Spam')

plt.xlabel('Number of Characters')
plt.ylabel('Count')
plt.title('Distribution of Number of Characters')


plt.legend(loc='upper right')

plt.show()

# %%
plt.figure(figsize=(12,6))
sns.histplot(df[df['target'] == 0]['num_words'])
sns.histplot(df[df['target'] == 1]['num_words'],color='red')

# %%
sns.pairplot(df,hue='target')

# %%
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

# %% [markdown]
# # 3. Text Preprocessing
# 
# The SMS messages were cleaned using Natural Language Processing (NLP).
# 
# The preprocessing steps include:
# - Convert text to lowercase.
# - Tokenization.
# - Remove special characters.
# - Remove stop words.
# - Remove punctuation.
# - Apply Porter Stemming.

# %%
def transform_text(text):
    text = text.lower() # all text to lower case
    text = nltk.word_tokenize(text) # sentence into words, separate words
    
    y = []
    for i in text:
        if i.isalnum(): # is alpha numeric to remove special characters such as %% etc
            y.append(i)
    
    # to remove stopwords: play role in sentence formation not meaning , and puntuations:?!
    text = y[:] # cloning to copy the text
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)

# %%
import nltk

nltk.download('stopwords')

# %%
# stopwords
from nltk.corpus import stopwords
stopwords.words('english')

# %%
# punctuations
import string
string.punctuation

# %%
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

print(ps.stem("Loving"))
print(ps.stem("Loved"))
print(ps.stem("Playing"))

# %%
transform_text("I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today.")

# %%
df['text'][10]

# %%
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
ps.stem('loving')

# %%
df['transformed_text'] = df['text'].apply(transform_text)

# %% [markdown]
# # 5. Feature Extraction
# 
# The cleaned text was converted into numerical form using the TF-IDF Vectorizer.
# 
# TF-IDF assigns higher importance to informative words while reducing the impact of commonly occurring words.

# %%
df.head()

# %%
# make the most repitative words bold
from wordcloud import WordCloud
wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')

# %%
spam_wc = wc.generate(df[df['target'] == 1]['transformed_text'].str.cat(sep=" "))

# %%
plt.figure(figsize=(15,6))
plt.imshow(spam_wc)

# %%
ham_wc = wc.generate(df[df['target'] == 0]['transformed_text'].str.cat(sep=" "))

# %%
plt.figure(figsize=(15,6))
plt.imshow(ham_wc)

# %%
df.head()

# %%
spam_corpus = []
for msg in df[df['target'] == 1]['transformed_text'].tolist():
    for word in msg.split():
        spam_corpus.append(word)
        

# %%
len(spam_corpus)

# %%
# from collections import Counter
# sns.barplot(pd.DataFrame(Counter(spam_corpus).most_common(30))[0],pd.DataFrame(Counter(spam_corpus).most_common(30))[1])
# plt.xticks(rotation='vertical')
# plt.show()

from collections import Counter

word_counts = pd.DataFrame(Counter(spam_corpus).most_common(30))

plt.figure(figsize=(12,6))
sns.barplot(
    x=word_counts[0],
    y=word_counts[1],
    hue=word_counts[0],      # Different color for each bar
    palette='husl',
    legend=False
)

plt.xticks(rotation='vertical')
plt.show()

# %%
ham_corpus = []
for msg in df[df['target'] == 0]['transformed_text'].tolist():
    for word in msg.split():
        ham_corpus.append(word)

# %%
len(ham_corpus)

# %%
# from collections import Counter
# sns.barplot(pd.DataFrame(Counter(ham_corpus).most_common(30))[0],pd.DataFrame(Counter(ham_corpus).most_common(30))[1])
# plt.xticks(rotation='vertical')
# plt.show()


ham_df = pd.DataFrame(Counter(ham_corpus).most_common(30), columns=['Word', 'Count'])

plt.figure(figsize=(12,6))

sns.barplot(
    x='Word',
    y='Count',
    data=ham_df,
    hue='Word',          # Gives each bar a different color
    palette='husl',
    legend=False
)

plt.xticks(rotation='vertical')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 30 Most Frequent Words in Ham Messages")

plt.show()

# %%
# Text Vectorization
# using Bag of Words
df.head()

# %% [markdown]
# # 5. Model Building
# 
# Three Naive Bayes classifiers were trained:
# 
# - Gaussian Naive Bayes
# - Multinomial Naive Bayes
# - Bernoulli Naive Bayes
# 
# The dataset was divided into:
# - 80% Training Data
# - 20% Testing Data## 4. Model Building

# %%
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = CountVectorizer()
tfidf = TfidfVectorizer(max_features=3000)

# %%
X = tfidf.fit_transform(df['transformed_text']).toarray()

# %%
X.shape

# %%
y = df['target'].values

# %%
from sklearn.model_selection import train_test_split

# %%
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

# %% [markdown]
# # 6. Model Evaluation
# 
# The models were evaluated using:
# 
# - Accuracy Score
# - Precision Score
# - Confusion Matrix
# 
# Among all models, Multinomial Naive Bayes achieved the best overall performance and was selected as the final model.

# %%
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score

# %%
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

# %%
gnb.fit(X_train,y_train)
y_pred1 = gnb.predict(X_test)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
print(precision_score(y_test,y_pred1))

# %%
mnb.fit(X_train,y_train)
y_pred2 = mnb.predict(X_test)
print(accuracy_score(y_test,y_pred2))
print(confusion_matrix(y_test,y_pred2))
print(precision_score(y_test,y_pred2))

# %%
bnb.fit(X_train,y_train)
y_pred3 = bnb.predict(X_test)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
print(precision_score(y_test,y_pred3))

# %%
# tfidf --> MNB

# %%
# model improve
# 1. Change the max_features parameter of TfIdf

# %% [markdown]
# # 7. Advanced Model Development
# 
# To improve the performance of the spam detection system, two advanced machine learning algorithms were implemented and compared.
# 
# The models used are:
# - Random Forest (RF)
# - Support Vector Machine (SVM)
# 
# Both models were trained using the TF-IDF feature vectors and evaluated on the test dataset using Accuracy and Precision.

# %%
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# %%
svc = SVC(kernel='sigmoid', gamma=1.0)
rfc = RandomForestClassifier(n_estimators=50, random_state=2)

# %%
clfs = {
    'SVC' : svc,
    'RF': rfc, 
}

# %%
def train_classifier(clf,X_train,y_train,X_test,y_test):
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    precision = precision_score(y_test,y_pred)
    
    return accuracy,precision

# %%
train_classifier(svc,X_train,y_train,X_test,y_test)

# %%
accuracy_scores = []
precision_scores = []

for name,clf in clfs.items():
    
    current_accuracy,current_precision = train_classifier(clf, X_train,y_train,X_test,y_test)
    
    print("For ",name)
    print("Accuracy - ",current_accuracy)
    print("Precision - ",current_precision)
    
    accuracy_scores.append(current_accuracy)
    precision_scores.append(current_precision)

# %%
performance_df = pd.DataFrame({'Algorithm':clfs.keys(),'Accuracy':accuracy_scores,'Precision':precision_scores}).sort_values('Precision',ascending=False)

# %%
performance_df

# %% [markdown]
# # Saving the Model
# 
# The trained TF-IDF vectorizer and Multinomial Naive Bayes model were saved using Pickle.
# 
# Saved Files:
# - model.pkl
# - vectorizer.pkl

# %%
import pickle
pickle.dump(tfidf,open('vectorizer.pkl','wb'))
pickle.dump(mnb,open('model.pkl','wb'))

# %% [markdown]
# # Deployment
# 
# The final model was deployed as a Streamlit web application, allowing users to enter SMS messages and instantly predict whether they are Spam or Ham.

# %%



