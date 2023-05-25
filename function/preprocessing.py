import pandas as pd
import numpy as np

def mentor_mentee_table(data):
    data = pd.DataFrame(data)
    mentee_interest = data.loc[data['role_id'] == 3,['id', 'name', 'gender_id', 'is_path_android', 'is_path_be', 
                                                     'is_path_devops', 'is_path_flutter', 'is_path_gcp','is_path_ios',
                                                     'is_path_ml', 'is_path_react', 'is_path_web', 'is_path_fe']] 
    mentor_interest = data.loc[data['role_id'] == 2, ['id', 'name', 'gender_id', 'is_path_android', 'is_path_be', 
                                                     'is_path_devops', 'is_path_flutter', 'is_path_gcp','is_path_ios',
                                                     'is_path_ml', 'is_path_react', 'is_path_web', 'is_path_fe']] 
    mentee_day_availability = data.loc[data['role_id'] == 3, ['id', 'name', 'gender_id', 'is_monday_available', 
                                                              'is_tuesday_available', 'is_wednesday_available',
                                                              'is_thursday_available', 'is_friday_available',
                                                              'is_saturday_available', 'is_sunday_available']]
    mentor_day_availability = data.loc[data['role_id'] == 2, ['id', 'name', 'gender_id', 'is_monday_available', 
                                                              'is_tuesday_available', 'is_wednesday_available',
                                                              'is_thursday_available', 'is_friday_available',
                                                              'is_saturday_available', 'is_sunday_available']]
    
    return mentee_interest, mentor_interest, mentee_day_availability, mentor_day_availability

def cosine_similarity(mentee, mentor):
    vec1 = mentee
    vec2 = mentor
    cosine = np.dot(vec1,vec2)/((np.dot(vec1,vec1)*np.dot(vec2,vec2))**0.5) 
    return cosine

