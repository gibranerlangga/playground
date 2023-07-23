# source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4867863/

# The d-value is a measure of the separation between two groups of observations.
# It is the area under the ROC curve (AUC) when the observations are separated 
# into two groups and the ROC curve is plotted of sensitivity (true positive rate) 
# versus 1-specificity (false positive rate).

# Below is the implementation of the d-value in Python.

import numpy as np
from sklearn.metrics import roc_auc_score


# set the seed
np.random.seed(123)

## generate an artificial dataset
group1 = np.random.normal(0, 1, 1000)
group2 = np.random.normal(0.5, 1, 1000)

## calculate the d-value
# Create the labels (0 for group1 and 1 for group2)
labels = np.concatenate([np.zeros_like(group1), np.ones_like(group2)])

# Concatenate the observations
observations = np.concatenate([group1, group2])

# Compute the d-value, i.e. ROC AUC
d_value = roc_auc_score(labels, observations)

print(d_value)