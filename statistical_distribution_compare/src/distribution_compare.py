import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def compare_distributions(data1, data2):
    """
    Compare two distributions using histograms and the Kolmogorov-Smirnov test.
    The shaded region represents the point of maximum difference (K-S statistic) between the two CDFs.
    
    Parameters:
    - data1, data2: Input arrays or lists representing the two distributions to be compared.
    
    This function performs the following steps:
    1. Plots the histograms of the two distributions.
    2. Applies the Kolmogorov-Smirnov test to compare the distributions.
    3. Prints the K-S statistic and p-value, and makes a decision about the null hypothesis.
    4. Plots the cumulative distribution functions of the two distributions, highlighting the K-S statistic.
    """

    def ecdf(data):
        """Compute ECDF for a one-dimensional array of measurements."""
        n = len(data)
        x = np.sort(data)
        y = np.arange(1, n+1) / n
        return x, y

    # Step 1: Draw the distributions
    plt.figure(figsize=(14, 7))

    plt.subplot(1, 2, 1)
    plt.hist(data1, bins=30, density=True, color='b', alpha=0.6)
    plt.title('Distribution 1')

    plt.subplot(1, 2, 2)
    plt.hist(data2, bins=30, density=True, color='r', alpha=0.6)
    plt.title('Distribution 2')

    plt.show()
    
    # Step 2: Apply whatever effects are necessary to make these distributions comparable
    # Note: The Kolmogorov-Smirnov test is nonparametric and does not assume a specific distribution. 
    # So, there's no need to apply any transformations to the data in order to make them comparable.
    
    # Step 3: Compare the distributions using the Kolmogorov-Smirnov test
    ks_stat, ks_p_value = stats.ks_2samp(data1, data2)
    print(f'K-S statistic: {ks_stat}')
    print(f'p-value: {ks_p_value}')

    if ks_p_value < 0.05:
        print("We reject the null hypothesis that the two samples were drawn from the same distribution.")
    else:
        print("We cannot reject the null hypothesis that the two samples were drawn from the same distribution.")
    
    # Step 4: Create a figure of the K-S statistic
    # Compute ECDF for each data set
    x1, y1 = ecdf(data1)
    x2, y2 = ecdf(data2)

    # Compute the differences in y-values (CDFs)
    diff = np.abs(y1 - y2)

    # Find the x where the difference is maximum (K-S statistic)
    max_diff_index = np.argmax(diff)

    # Generate plot
    plt.figure(figsize=(12, 7))
    plt.plot(x1, y1, label='Distribution 1')
    plt.plot(x2, y2, label='Distribution 2')
    plt.fill_betweenx([y1[max_diff_index], y1[max_diff_index+1]], [x1[max_diff_index], x1[max_diff_index+1]], color='gray', alpha=0.5)
    plt.title('Cumulative Distribution Functions with K-S Statistic')
    plt.ylabel('Cumulative Probability')
    plt.xlabel('Value')
    plt.legend()
    plt.show()
