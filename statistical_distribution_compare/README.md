# Compare Statistical Distributions using Kolmogorov-Smirnov (K-S) test

> **Note**<br/>
**You can find the jupyter notebook to compare two distributions manually [here](statistical_distribution_compare.ipynb), , and the statistical library to compare them [here](src/distribution_compare.py)**


The Kolmogorov-Smirnov (K-S) test is a nonparametric test that makes no assumption about the distribution of data. This property makes it suitable for comparing two samples, regardless of the distribution they follow.

However, there are a few things to keep in mind:

1. The K-S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. So, it can detect differences in median, variability, skewness, and kurtosis. 

2. The K-S test compares the entire distribution of data, not just a single statistic (like mean or median). Therefore, two distributions could have the same mean and standard deviation, but the K-S test could still indicate that they come from different distributions.

3. The power of the K-S test (i.e., its ability to correctly reject the null hypothesis when it is false) can be lower than other tests when the differences between the distributions are not in the center of the distributions.

4. The samples being compared should be continuous distributions. The K-S test is not suitable for discrete distributions because it is based on the cumulative distribution function, which isn't stepwise for a discrete distribution.

5. The two samples should be independent of each other.

It's also worth noting that there are other statistical tests for comparing distributions, such as the Anderson-Darling test, the Cramér-von Mises criterion, and the Wasserstein distance. The choice of test depends on the specific data and research question at hand.

**How to interpret the test**

The Kolmogorov-Smirnov test quantifies the distance between the empirical distribution functions of two samples. If the K-S statistic is small or the p-value is high, then we cannot reject the hypothesis that the distributions of the two samples are the same. Conversely, a large K-S statistic or small p-value suggests that the distributions are different.

*example:*
Suppose the result of the Kolmogorov-Smirnov test gives us a statistic of 0.524 and a very small p-value (approximately \(9.13 \times 10^{-126}\)).

The K-S statistic of 0.524 represents the maximum difference between the cumulative distribution functions of the two samples. The extremely small p-value suggests that we can confidently reject the null hypothesis that the two samples were drawn from the same distribution.

In other words, these results indicate that the two distributions are significantly different, which aligns with our initial setup where we drew one sample from a Normal distribution and the other from an Exponential distribution.