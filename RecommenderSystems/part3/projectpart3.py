import pandas as pd
import numpy as np
import sys
sys.path.append('./')
from projectpart1 import init, group_recommendations

ratings, movies, user_movie_matrix, user_similarity = init()

print("working on group recommendations")
print()

# let's use group with user_ids 1-5
group = [1,2,3,4,5]
group_recs = group_recommendations(group)
group_recs_top = pd.DataFrame({})
group_recs_top_index = []

print(group_recs)

for user in group:
    top_predicted = group_recs[user].sort_values(ascending=False)[0:49]
    for movie in top_predicted.index:
        group_recs_top_index.append(movie)

unique = []
for x in group_recs_top_index:
    if x not in unique:
        unique.append(x)
group_recs_top_index = unique

group_recs_top = group_recs.loc[group_recs_top_index]

print(group_recs_top)

def movie_title_to_genre_vector(title):
    row = movies.loc[movies['title'] == title]
    row_numpy = row.to_numpy()[0]
    return row_numpy[-19:]

def sim_items(mv1, mv2):
    # invert the titles to genre vectors
    mg1 = movie_title_to_genre_vector(mv1)
    mg2 = movie_title_to_genre_vector(mv2)

    # cosine between movie genre vectors
    na = np.linalg.norm(mg1)
    nb = np.linalg.norm(mg2)

    if na == 0 or nb == 0:
        return 0.0
    return np.dot(mg1, mg2) / (na * nb)

def similarity(movie, movies):
    # calculates the average pairwise similarity
    sims = [sim_items(movie, mv) for mv in movies]
    return np.mean(sims)

def diversness(mvs):
    # calculating the average pairwise dissimilariy
    k = len(mvs)
    if k <= 1:
        return 0.0
    dsims = []
    for i in range(k):
        for j in range(1+i, k):
            dsims.append(1-sim_items(mvs[i], mvs[j]))
    div = 2/(k*(k-1)) * np.sum(dsims)
    return div

def f_score(movie, movies, l=0.5):
    k = len(movies)
    return (k-1)*(1-l)*similarity(movie, movies)+2*l*diversness(movies)

def motley_w_fscore(candidate: list[str], result: list[str], q: str, theta=0.3) -> list[str]:
    result.append(q)
    candidate.remove(q)
    candidate = sorted(candidate, key=lambda x: sim_items(x, q), reverse=True)
    while len(result) < 10 or len(candidate) == 0:
        m = candidate.pop(0)
        if f_score(q, result + [m]) >= theta:
            result.append(m)
    return result

# test prints
print(f"movie to genre vector: {movie_title_to_genre_vector('GoldenEye (1995)')}")
print(f"similarity two movies: {sim_items('GoldenEye (1995)', 'You So Crazy (1994)')}")
print(f"similarity(q, R): {similarity('GoldenEye (1995)', ['Babyfever (1994)', '187 (1997)', 'Hard Eight (1996)'])}")
print(f"diversity(R): {diversness(['Babyfever (1994)', '187 (1997)', 'Hard Eight (1996)'])}")
print(f"F-score test: {f_score('GoldenEye (1995)', ['Babyfever (1994)', '187 (1997)', 'Hard Eight (1996)'], l=0.2)}")
print()

group_recommendation_avg = group_recs.transpose() \
    .agg('mean') \
    .sort_values(ascending=False)

top_prediction = group_recommendation_avg \
    .head(1) \
    .index[0]

motleyF_index = motley_w_fscore(group_recs_top_index, [], top_prediction)
motleyF_recs = []
for movie in motleyF_index:
    motleyF_recs.append((movie, group_recs_top.loc[movie].agg('mean').round(2)))

print("Sequential diverse group recommendations with motleyF for 10 rounds with average ratings:")
for i in range(len(motleyF_recs)):
    print(f"{i+1}: {motleyF_recs[i]}")
print(f"motleyF F-score: {f_score(top_prediction, motleyF_index)}")
print()

# for comparison
comparison_set_avg = group_recommendation_avg \
    .head(10) \
    .index
print(f"Using just average aggregation:\n{group_recommendation_avg.head(10)}")
print(f"avg agg F-score: {f_score(top_prediction, comparison_set_avg)}")