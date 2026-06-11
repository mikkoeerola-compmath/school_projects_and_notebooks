import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import random
import sys
sys.path.append('./')
from projectpart1 import init, group_recommendations, aggregate_group_mean, movie_id_to_title

print("initializing...")

ratings, movies, user_movie_matrix, user_similarity = init()

print("working on group recommendations...")
print()

# let's use group with 5 random users
group = nums = [random.randint(1, 943) for _ in range(5)]
group_rec = group_recommendations(group, user_movie_matrix)
# group_recs_top = pd.DataFrame({})
# group_recs_top_index = []

group_rec_mean = aggregate_group_mean(group_rec)

print(group_rec_mean)

# Explanations:
"""group_interactions_numpy = [user_movie_matrix[user] \
                      .dropna().index \
                      #.map(movie_id_to_title) \
                      .to_numpy() for user in group]

group_interactions_DF = pd.DataFrame({
    idx: pd.Series(vals)
    for idx, vals in zip(group, group_interactions_numpy)
})"""
#print(group_interactions_DF)

top_pred = group_rec_mean.index.to_list()

# metrics to aggregate and sort the group_interactions_DF
def score(row):
    return row['mean'] * row['rec']

def greedygrow(target: int, um_matrix: pd.DataFrame, group: list[int]):
    um_matrix_group = um_matrix.loc[group]
    um_matrix_group = um_matrix_group.transpose()
    um_matrix_group = um_matrix_group.dropna(how='all', subset=group)
    um_matrix_group['mean'] = um_matrix_group[group].mean(axis=1)
    um_matrix_group['count'] = um_matrix_group[group].count(axis=1)
    um_matrix_group['rec'] = um_matrix_group['count'] / len(group)
    um_matrix_group['score'] = um_matrix_group.apply(score, axis=1)
    um_matrix_group = um_matrix_group.sort_values('score', ascending=False)

    # print(um_matrix_group)

    expl_canditates = um_matrix_group.index.to_list()
    expl = []

    pred_ls = top_pred[0:5]

    while target in pred_ls:
        # for testing
        print(expl)
        print(pred_ls)

        drop = expl_canditates.pop(0)
        expl.append(drop)
        # new_um_matrix_group = um_matrix_group.drop(index=drop)
        new_um_matrix = um_matrix.drop(expl, axis=1)

        new_group_recs = group_recommendations(group, new_um_matrix)
        new_group_recs_mean = aggregate_group_mean(new_group_recs)
        
        pred_ls = new_group_recs_mean.index.to_list()[0:5]

        """ # fairness rebuild:
        if target in pred_ls:
            expl = fairness_rebuild(expl)

            new_um_matrix = um_matrix.drop(expl, axis=1)

            new_group_recs = group_recommendations(group, new_um_matrix)
            new_group_recs_mean = aggregate_group_mean(new_group_recs)

            pred_ls = new_group_recs_mean.index.to_list()[0:10]
        else:
            return expl"""

    return expl, um_matrix_group


# pick items so that everyone has interacted with an item in expl atleast once.
def diversity_cluster_rebuild(group_df, expls):
    """
    group_df = ratings of the group with aggregated scores
    expl = list of movie IDs in the counterfactual explanation
    k = desired explanation size
    """
    k = max(1, int(round(np.log(len(expls)))))
    k = min(k, len(expls))

    # Subset to explanation items
    sub = group_df.loc[expls, group]
    sub_full = group_df.loc[expls].copy()

    #test
    print(sub)
    print(sub_full)

    # Cluster
    kmeans = KMeans(n_clusters=k, random_state=42).fit(sub)

    sub_full["cluster"] = kmeans.labels_

    # Pick best representative per cluster
    representatives = []

    for cl in sorted(sub_full["cluster"].unique()):
        cluster_items = sub_full[sub_full["cluster"] == cl]
        rep = cluster_items['score'].idxmax()
        representatives.append(rep)

    return representatives


print("working on explanations...")
target = top_pred[0]
expl_list, group_mtx = greedygrow(target, user_movie_matrix, group)
expl_list = diversity_cluster_rebuild(group_mtx.fillna(0), expl_list)
print(expl_list)

print(f"Explanations for {target} are: {[movie_id_to_title(movie) for movie in expl_list]}")

new_um_matrix = user_movie_matrix.drop(expl_list, axis=1)

new_group_recs = group_recommendations(group, new_um_matrix)
new_group_recs_mean = aggregate_group_mean(new_group_recs)

pred_ls = new_group_recs_mean.index.to_list()[0:5]
print(pred_ls)
print(f"{[movie_id_to_title(movie) for movie in pred_ls]}")

