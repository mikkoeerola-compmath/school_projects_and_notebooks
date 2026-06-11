import pandas as pd
import numpy as np

def init():
    # The columns are user_id, item_id, rating, timestamp
    ratings = pd.read_csv(
        filepath_or_buffer="./ml-100k/u.data",
        sep="\t",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )

    movies = pd.read_csv(
        "./ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        names=[
            "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
            "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
            "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
            "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
        ],
        usecols=range(24)
    )

    user_movie_matrix = ratings.pivot_table(index="user_id", columns="movie_id", values="rating")

    user_similarity = user_movie_matrix.transpose().corr(method='pearson').fillna(0)

    return ratings, movies, user_movie_matrix, user_similarity

ratings, movies, user_movie_matrix, user_similarity = init()
'''
print("Rating dataset first rows:")
print(ratings.head())
print("\n")
print(f"Number of ratings (rows) in the data: {ratings.shape[0]}.")
print("\n")
print("Movies dataset first rows:")
print(movies.head())
print()

print(user_movie_matrix)
print()

print("User similarity matrix")
print(user_similarity)
print()'''

def movie_id_to_title(movie_id):
    return movies.loc[movies['movie_id'] == movie_id, 'title'].values[0]

# Let's predict a list of movies that user: user_id
# might like using the prediction function, ratings given by other users and the calculated
# similarities between the users.
def recommend_movies(user_id, user_similarity, user_movie_matrix):

    target_user = user_id
    recommend_users = user_similarity[target_user].sort_values(ascending=False)

    #let's drop the target user themselve
    recommend_users = recommend_users.drop(target_user)

    # Also let's drop users with not so many common ratings:
    target_user_ratings = user_movie_matrix.loc[target_user]
    for user in recommend_users.index:
        if len(target_user_ratings.dropna().index.intersection(user_movie_matrix.loc[user].dropna().index)) < 5:
            recommend_users.drop(user)

    # find the movies the target user hasn't rated
    unrated_movies = target_user_ratings[target_user_ratings.isna()].index

    # predict the rating for the target user in a dict
    avg_target_rating = target_user_ratings.mean()
    predicted_ratings = {}

    for movie in unrated_movies:
        movie_ratings = user_movie_matrix[movie]
        users_who_rated = movie_ratings[movie_ratings.notna()].index

        # let's consider top-100 closest neighbours
        common_index = recommend_users[users_who_rated].index \
            .intersection(recommend_users.index)
        sims = recommend_users[common_index][0:99]

        # if there are more than one users who have rated the movie, calculate the prediction
        if len(sims) > 1:
            users = sims.index

            # Vector of user average ratings
            user_avgs = user_movie_matrix.loc[users].mean(axis=1)

            # Vector of users’ ratings for this movie
            user_movie_vals = movie_ratings.loc[users]

            # Compute numerator and denominator
            numerators = sims.values * (user_movie_vals.values - user_avgs.values)
            denominator = np.abs(sims.values).sum()
            if denominator == 0:
                continue
            predicted_ratings[movie] = avg_target_rating + numerators.sum()/denominator
        else:
            predicted_ratings[movie] = 0

    predicted_ratings_series = pd.Series(predicted_ratings)
    predicted_ratings_series.index = predicted_ratings_series.index.map(movie_id_to_title)

    return predicted_ratings_series.sort_values(ascending=False)
'''
# Let's take top 5 most recommended movies
recommended_movies = recommend_movies(1, user_similarity, user_movie_matrix)[0:4]
print("recommended movies for target_user and their predicted rating:")
print(recommended_movies.apply(lambda x: min(5, max(1, x))))
print()
'''
"""
# Let's improve the similarity function accoring to Fethi Fkih, 2022
# (https://doi.org/10.1016/j.jksuci.2021.09.014)
def ipwr(x: pd.Series, y: pd.Series):
    \"""
    Calculate the improved Pearson correlation coefficient between two arrays
    and balance it with standard deviation for each users (user preference)
    \"""
    # Empirically found balance
    a = 0.3
    
    # Drop NaN values to only consider overlapping items
    common = x.dropna().index.intersection(y.dropna().index)
    if len(common) == 0:
        return np.nan

    x_common = x.loc[common]
    y_common = y.loc[common]

    # Means and stds
    mean_x, mean_y = x_common.mean(), y_common.mean()
    std_x, std_y = x_common.std(ddof=0), y_common.std(ddof=0)

    # Regular Pearson correlation
    num = np.sum((x_common - mean_x) * (y_common - mean_y))
    den = np.sqrt(np.sum((x_common - mean_x)**2) * np.sum((y_common - mean_y)**2))
    if den == 0:
        return np.nan
    pearson = num / den

    # Rating preference behavior (RPB)
    rpb = np.cos(np.abs(mean_x - mean_y) * np.abs(std_x - std_y))

    # Combine
    b = 1 - a
    return a * rpb + b * pearson

# let's take a look if the neighbours change
user_similarity = user_movie_matrix.transpose().corr(method=ipwr)
user_similarity = user_similarity.fillna(0)

recommend_users2 = user_similarity[target_user].sort_values(ascending=False)

#let's drop the target user themselves
recommend_users2 = recommend_users2.drop(target_user)

# Also let's drop users with not so many common ratings:
target_user_ratings = user_movie_matrix.loc[target_user]
for user in recommend_users2.index:
    if len(target_user_ratings.dropna().index.intersection(user_movie_matrix.loc[user].dropna().index)) < 5:
        recommend_users2.drop(user)

print("most similar users for target_user:")
print(recommend_users2.head())
print()
"""

# group recommendations function
def group_recommendations(user_ids: list):
    all_recommendations = {}

    for user in user_ids:
        recs = (recommend_movies(user, user_similarity, user_movie_matrix))
        recs = recs[~recs.index.duplicated(keep='first')]
        all_recommendations[user] = recs
    return pd.DataFrame(all_recommendations).dropna()
'''
# Group recommendations, let the group be user_ids 1-5
group_df = group_recommendations([1,2,3,4,5])
print("group recommendation list")
print(group_df)
print()

# average aggregation
group_recommendation_avg = group_df.transpose().agg('mean')
# Top-5 recommended movies for the group
print("top 5 movies for the group using average aggregation")
print(group_recommendation_avg.sort_values(ascending=False).head(5))
print()

# least misery aggregation
group_recommendation_lm = group_df.transpose().agg('min')
# Top-5 recommended movies for the group
print("top 5 movies for the group using least misery aggregation")
print(group_recommendation_lm.sort_values(ascending=False).head(5))
'''