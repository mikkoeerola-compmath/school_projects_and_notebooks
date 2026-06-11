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
    top_predicted = group_recs[user].sort_values(ascending=False)[0:9]
    for movie in top_predicted.index:
        group_recs_top_index.append(movie)

unique = []
for x in group_recs_top_index:
    if x not in unique:
        unique.append(x)
group_recs_top_index = unique

group_recs_top = group_recs.loc[group_recs_top_index]

print(group_recs_top)

def satisfaction(items, user):
    # User satisfaction with items
    ratings = group_recs_top[user]
    return np.sum(ratings.loc[items]) / np.sum(
        ratings.sort_values(ascending=False).head(len(items)))

print(f"user 1 satisfaction test: {satisfaction(['Babyfever (1994)'], 1)}")

def group_disagreenment_avg(items):
    # Group average disagreenment on items
    sats = []
    for u in group:
        sat = satisfaction(items, u)
        sats.append(sat)
    max_sat = np.max(sats)
    return np.sum([max_sat - satisfaction(items, user) for user in group])/len(group)

print(f"group disagreenment test: {group_disagreenment_avg(['Babyfever (1994)'])}")

def seq_group_rec(group, candidate_items, selected, alpha=0.7, beta=0.3):
    # Build the list of sequential recommendations with eager algorithm
    # that balances satisfaction and disagreenment

    scores = {}
    for item in candidate_items:
        # simulate adding the item
        trial_items = selected + [item]

        # compute metrics
        user_sats = [satisfaction(trial_items, user) for user in group]
        group_sat = np.mean(user_sats)
        disagreement = group_disagreenment_avg(trial_items)

        # combined objective: maximize satisfaction, minimize disagreement
        scores[item] = alpha * group_sat - beta * disagreement

    # pick the best next item
    best_item = max(scores, key=scores.get)
    selected.append(best_item)
    candidate_items.remove(best_item)
    
    if len(selected) == 5:
        return selected
    else:
        if group_disagreenment_avg(selected) > 0.5:
            return seq_group_rec(group, candidate_items.copy(), selected.copy(), alpha=0.3, beta=0.7)
        else:
            return seq_group_rec(group, candidate_items.copy(), selected.copy())

seq_recs_index = seq_group_rec(group, group_recs_top_index, [])
seq_recs = []
for movie in seq_recs_index:
    seq_recs.append((movie), group_recs_top.loc[movie].agg('mean'))

print("Sequential group recommendations for 5 rounds with average rating:")
print(seq_recs)