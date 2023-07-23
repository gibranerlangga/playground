# comparison between frequentist, bayesian and empirical bayesian approaches to the same problem

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# set mean and std
true_mean = 10
true_std = 2

# set the seed
np.random.seed(0)

sample_size = 1000
sample = np.random.normal(true_mean, true_std, sample_size)

sample_mean = np.mean(sample)
sample_std = np.std(sample)


# frequentist approach
confidence_level = 0.95
z = stats.norm.ppf((1 + confidence_level) / 2)
lower = sample_mean - z * sample_std / np.sqrt(sample_size)
upper = sample_mean + z * sample_std / np.sqrt(sample_size)
confidence_interval = (lower, upper)

# bayesian approach
prior_mean = 0
prior_std = 1
posterior_mean = ((prior_mean / prior_std**2) + (sample_size * sample_mean / sample_std**2)) / ((1 / prior_std**2) + (sample_size / sample_std**2))
posterior_std_dev = np.sqrt(1 / ((1 / prior_std**2) + (sample_size / sample_std**2)))

# Empirical Bayesian Approach
emp_posterior_mean = sample_mean
emp_posterior_std = sample_std
emp_posterior = stats.norm(emp_posterior_mean, emp_posterior_std)

print('frequentist:', confidence_interval)
print('bayesian:', posterior_mean, posterior_std_dev)
print('empirical bayes:', emp_posterior.mean(), emp_posterior.std())