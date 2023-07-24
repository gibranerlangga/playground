# a simulation to demonstrate the problem of p-value when sample size is large.
# The result shows that as the sample size n increases, the p-value decreases.
# This is because the t-statistic increases as the sample size increases. 
#
# The t-statistic is the ratio of the difference between the sample mean and the 
# null hypothesis mean, and the standard error of the difference between the sample 
# mean and the null hypothesis mean. As the sample size increases, the difference 
# between the sample mean and the null hypothesis mean becomes larger, and the standard
# error of the difference between the sample mean and the null hypothesis mean
# becomes smaller. Therefore, the t-statistic increases as the sample size increases.

import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# set the seed
np.random.seed(123)

# generate mean and std of 2 artificial groups
group1_mean, group2_mean = 1, 1.4
group1_std, group2_std = 1, 1

# p-value placeholder
p_values = []

# array to store sample sizes
sample_sizes = np.arange(10, 1000, 10)

for n in sample_sizes:
    group1 = np.random.normal(group1_mean, group1_std, n)
    group2 = np.random.normal(group2_mean, group2_std, n)

    t_stat, p_value = ttest_ind(group1, group2)

    p_values.append(p_value)

# plot the p-values as a function of sample size
plt.plot(sample_sizes, p_values)
plt.xlabel('sample size')
plt.ylabel('p-value')
plt.title('p-value as a function of sample size')
plt.show()
