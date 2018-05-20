
# coding: utf-8

# # Evaluate Kahoot performance during a course
# 
# ## Evaluate points
# 
# ### Read data from Excell files

# In[3]:

import os
import pandas

directory_name = "A:\\1docs\\aktualis\\2017-18-2 Oktatas\\Fusion devices\\kahoot"
sheet_name = "Final Scores"
list_of_all_files = os.listdir(directory_name)
list_of_all_files


# In[4]:

list_of_files = [elem for elem in list_of_all_files if len(elem) > 20]
list_of_files


# ### Players corrections

# In[5]:

import numpy as np
def convert_players(old_player):
    if old_player == "Niklas":
        return "TJBYX4"
    if old_player == "Vladislav M.":
        return "DHD5TF"
    if old_player == "Bori":
        return "KD9XVQ"
    if old_player == "Yossi":
        return "SW0S1F"
    if old_player == "Tobi":
        return "TH5Z6J"
    if old_player == "Buchtinator":
        return "F87N7B"
    if old_player == "Daniel Brunsch":
        return "MU3HCF"
    if old_player == "Vicky":
        return "WE2600"
    if old_player == "H.Adam":
        return "PJ257S"
    if old_player == "Mo":
        return "RYLBNG"
    old_player = str(old_player).upper()
    if old_player == "MUH3CF":
        return "MU3HCF"
    return old_player

conv_players=np.vectorize(convert_players)


# ### Read data from Excell files and perform transformations

# In[6]:

scores = pandas.DataFrame()
for file_name in list_of_files:
    scores_single = pandas.read_excel(directory_name+"\\"+file_name, sheetname=sheet_name, header=1, 
                                      skiprows=[1], skipfooter=1,
                                      converters={"Players":convert_players})
    scores = scores.append(scores_single)


# In[7]:

scores_single.head()


# In[8]:

scores.head()


# In[9]:

scores['Players'].value_counts()


# ### Aggregate results of individual Players

# In[10]:

scores_aggregate = scores.groupby('Players',as_index=False).agg({'Rank': ['mean', 'count'],
                                                                'Total Score (points)': 'sum',
                                                                'Correct Answers': 'sum',
                                                                'Incorrect Answers': 'sum'})


# In[11]:

scores.columns


# In[12]:

scores_aggregate.columns=[ 'Players', 'Rank', 'Count', 'Total Score (points)', 'Correct Answers', 'Incorrect Answers']


# In[13]:

scores_aggregate


# In[18]:

scores_aggregate['Total Score (Percentage)'] = 100.0 * scores_aggregate['Total Score (points)'] /                                                scores_aggregate['Total Score (points)'].max()


# In[19]:

scores_aggregate


# ### Print result

# In[21]:

writer = pandas.ExcelWriter(directory_name+"\\"+'kahoot_results.xlsx')
scores_aggregate.to_excel(writer,'Results')
writer.save()


# ## Evaluate question statistics
