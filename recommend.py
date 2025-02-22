
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import argparse


class MovieSearch: 
    def __init__(self, dataset):
        '''
        Read the dataset and initialize TF-IDF
        '''
        self.vectorizer = TfidfVectorizer()
        self.df = pd.read_csv(dataset)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['Overview'])

    def search(self, query, top_n=5):
        '''
        Transform the query into a TF-IDF vector, return top matches by cosine similarity   
        '''
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        self.df['similarity'] = cosine_similarities
        df_sorted = self.df.sort_values(by='similarity', ascending=False)
        titles = df_sorted[:top_n]
        titles = titles.assign(info=titles[['Series_Title', 'Released_Year']].agg(' - '.join, axis=1))
        return titles['info']

        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Description to select movies")
    parser.add_argument("--results", help="number of results to return", action="store")
    args = parser.parse_args()
    
    m = MovieSearch("./imdb_top_1000.csv")

    result = m.search(f"{args.query}")
    if args.results:
        result = m.search(f"{args.query}", int(args.results))

    for idx, title in enumerate(result):
        print(f"{idx+1}. {title}")


if __name__ == "__main__":
    main()