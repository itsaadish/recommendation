import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from config import CSV_FILE_PATH_CLEANED

df = None
article_database = defaultdict(dict)
article_contents = []
article_urls = []
dataframe  = None
cosine_sim = None

def load_data():
    global dataframe,df, article_database, article_contents, article_urls, cosine_sim
    
    # Load the CSV data
    df = pd.read_csv(CSV_FILE_PATH_CLEANED)
    dataframe = df
    print(len(df))
    # Initialize TF-IDF vectorizer
    # tfidf = TfidfVectorizer(stop_words='english')

    # Create article database and compute TF-IDF matrix
    for _, row in df.iterrows():
        article_url = row['latest_article_read']
        if article_url not in article_database:
            article_database[article_url] = {
                'sport': row['latest_sport_read'],
                'entity': row['latest_entity_read'],
            }


def get_user_data(user_id):
    global df
    return df[df['user_dim_nk'] == user_id].iloc[0]

def get_article_database():
    global article_database
    return article_database

def get_article_urls():
    global article_urls
    return article_urls

def get_cosine_sim():
    global cosine_sim
    return cosine_sim

    
    #since there is no article content access i can't do similarity score checking so cannot convert articles data to tfidf

    # tfidf_matrix = tfidf.fit_transform(article_contents)
    # cosine_sim = cosine_similarity(tfidf_matrix)