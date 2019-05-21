import pandas as pd

# Demo of a simplified Recommender System
#
#
# First an introduction to some of the popular types of Recommender Systems:
#   Simple Recommender (based on item ratings only)
#       Recommends n top-rated movies to all users.
#       This approach requires only the movie ratings (item_id, rating).
#   Collaborative Filtering (also based on item ratings)
#       This approach requires only the triplets dataset
#       consisting of user_id, item_id, rating.
#           Similar Users
#               User A: likes movies M1, M2 and M3
#               User B: likes movies M1, M2 and M3
#               In this case, users A and B can be called similar,
#               and later when User B likes movie M4,
#               it will be recommended to User A.
#           Similar Items
#               User A: likes movies M1 and M2
#               User B: likes movies M1 and M2
#               User C: likes movies M1 and M2
#               In this case, items M1 and M2 can be called similar,
#               and later when user D likes movie M2,
#               movie M1 will be recommended to user D.
#   Content-based Filtering (based on item meta-data)
#       This approach requires a vector for each user
#       consisting of the user's profile (user_id, genres liked, artists likes, directors liked, etc),
#       as well as a vector for each movie
#       consisting of the movie's meta-data (movie_id, directors, producers, artists, genres, etc).
#       We can use Cosine Similarity, Pearson's Correlation, TF-IDF, or a combination of these between
#       user's profile vector and movies' meta-data vectors.
#   Hybrid Systems
#       This approach produce the best recommendations,
#       however, they are the most complex to implement
#       as not only do they combine Collaborative and Content based filtering methods,
#       they also require more data for each user such as demographic information, pages visited,
#       interactions on social platforms, etc.
#       Hence, a hybrid recommender system needs to account for and meaningfully process all this
#       extra information to be able to provide truly personalized and useful recommendations.
#
# We shall build a rather simplistic item-item similarity
# collaborative filtering method based on Pearson's correlation scores.
#

df = pd.read_csv('ml-latest-small/ratings.csv')
movie_titles = pd.read_csv('ml-latest-small/movies.csv')
df = pd.merge(df, movie_titles, on='movieId')

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

m1_user_rating = movie_matrix['Toy Story (1995)']
m2_user_rating = movie_matrix['Jumanji (1995)']

movies_similar_to_m1 = movie_matrix.corrwith(m1_user_rating)
movies_similar_to_m2 = movie_matrix.corrwith(m2_user_rating)

corr_m1 = pd.DataFrame(movies_similar_to_m1, columns=['correlation'])
corr_m1.dropna(inplace=True)
print('Movies similar to Toy Story (1995): ')
print(corr_m1.head())

corr_m2 = pd.DataFrame(movies_similar_to_m2, columns=['correlation'])
corr_m2.dropna(inplace=True)
print('Movies similar to Jumanji (1995): ')
print(corr_m2.head())

corr_m1 = corr_m1.join(ratings['number_of_ratings'])
print('Movies similar to Toy Story (1995): ')
print(corr_m1.head())

corr_m2 = corr_m2.join(ratings['number_of_ratings'])
print('Movies similar to Jumanji (1995): ')
print(corr_m2.head())

corr_m1 = corr_m1[corr_m1['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False)
print('Movies similar to Toy Story (1995): ')
print(corr_m1.head())

corr_m2 = corr_m2[corr_m2['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False)
print('Movies similar to Jumanji (1995): ')
print(corr_m2.head())
