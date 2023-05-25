from function.preprocessing import *
import pandas as pd
import numpy as np
from collections import OrderedDict

def rank_sim(data):
    mentee_interest, mentor_interest, mentee_day_availability, mentor_day_availability = mentor_mentee_table(data)
    similarity_rank = {}
    cos_per_mentor = {}
    mentee_id = list(mentee_interest['id'].unique())
    mentor_id = list(mentor_interest['id'].unique())
    interests = ['android', 'be', 'devops', 'flutter', 'gcp', 'ios', 'ml', 'react', 'web', 'fe']
    interest_vars = [f"is_path_{i}" for i in interests]
    for mentee in mentee_id:
        interest_vec_mentee = mentee_interest.loc[mentee_interest['id']==mentee, interest_vars].values.reshape(-1,1)
        interest_vec_mentee = np.squeeze(np.asarray(interest_vec_mentee))
        for mentor in mentor_id:
            interest_vec_mentor = mentor_interest.loc[mentor_interest['id']==mentor, interest_vars].values.reshape(-1,1)
            interest_vec_mentor = np.squeeze(np.asarray(interest_vec_mentor))
            sim = cosine_similarity(interest_vec_mentee, interest_vec_mentor)
            if np.isnan(sim):
                sim = 1
            cos_per_mentor[int(mentor)] = sim

        similarity_rank[int(mentee)] = cos_per_mentor
        cos_per_mentor = {}

    # sorted similarity dictionary
    ranked_similarity_rank = {}
    for dict_keys, dict_vals in similarity_rank.items():
        ranked_dict_vals = {k: v for k, v in sorted(dict_vals.items(), key=lambda item: item[1], reverse=True)}
        ranked_similarity_rank[dict_keys] = ranked_dict_vals

    # output similarity dictionary
    ranked_sim_rank = {}
    for dict_keys, dict_vals in ranked_similarity_rank.items():
        list_mentors = list(dict_vals.keys())
        ranked_sim_rank[dict_keys] = list_mentors

    return ranked_sim_rank
    # return similarity_rank_hash