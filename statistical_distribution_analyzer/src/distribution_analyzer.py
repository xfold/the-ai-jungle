import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from IPython.display import Image
from IPython.display import SVG


class DistributionAnalyzer:
    """Perform distribution analysis on a given dataset.

    The class provides methods to analyze if the data follows one of the
    following distributions: Normal, Binomial, Uniform, Poisson, Exponential,
    and Beta.

    Attributes:
        data: The input data as a list or a numpy array.
        n: The number of data points.
        mean: The mean of the data.
        std_dev: The standard deviation of the data.

    """

    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.mean = np.mean(data)
        self.std_dev = np.std(data)

    def analyze(self):
        """Analyze the distribution of the data.

        The function checks the goodness of fit for various distributions and
        plots the data if it matches any known distribution.

        """
        dists = ["Normal", 
                 "Binomial", 
                 "Uniform", 
                 #"Poisson", 
                 "Exponential", 
                 "Beta"]
        dist_checks = [self.is_normal(), 
                       self.is_binomial(), 
                       self.is_uniform(), 
                       #self.is_poisson(), 
                       self.is_exponential(), 
                       self.is_beta()]

        dist_true = [d for d, check in zip(dists, dist_checks) if check]

        for dist in dist_true:
            print(f"Data seems to be drawn from a {dist} distribution.")
            self.plot(dist)
        
        if not dist_true:
            print("Data does not seem to fit Normal, Binomial, Uniform, Poisson, Exponential or Beta distributions.")

    def is_normal(self):
        k2, p = stats.kstest(self.data, 'norm')
        return p > 0.05  # Null hypothesis: data comes from a Normal distribution

    def is_binomial(self):
        def ecdf(data):
            # Compute ECDF for a one-dimensional array of measurements.
            n = len(data)  # Number of data points
            x = np.sort(data)  # x-data for the ECDF
            y = np.arange(1, n+1) / n  # y-data for the ECDF
            return x, y

        def theorical_cdf(n, p):
            # Compute theorical CDF for Binomial distribution
            x = np.arange(n+1)
            y = stats.binom.cdf(x, n, p)
            return x, y

        p = self.mean / self.n
        x, y = ecdf(self.data)
        x_theo, y_theo = theorical_cdf(self.n, p)
        return stats.ks_2samp(y, y_theo).pvalue > 0.05


    def is_uniform(self):
        k2, p = stats.kstest(self.data, 'uniform')
        return p > 0.05

    #def is_poisson(self):
    #    unique, counts = np.unique(self.data, return_counts=True)
    #    # Calculate probabilities based on a Poisson distribution
    #    expected_probabilities = stats.poisson.pmf(unique, self.mean)
    #    # Multiply by total number of observations to get expected counts
    #    expected_counts = expected_probabilities * self.n
    #    # Check if all expected counts are zero
    #    if np.all(expected_counts == 0):
    #        return False
    #    # Normalize expected counts so their sum equals the sum of observed counts
    #    expected_counts *= np.sum(counts) / np.sum(expected_counts)
    #    # Compare observed and expected counts using a chi-squared test
    #    chi2, p = stats.chisquare(counts, expected_counts)
    #    return p > 0.05


    def is_exponential(self):
        k2, p = stats.kstest(self.data, 'expon')
        return p > 0.05

    def is_beta(self):
        k2, p = stats.kstest(self.data, 'beta', args=(2, 2))
        return p > 0.05

    def plot(self, distribution_type):
        plt.hist(self.data, bins='auto', density=True)
        plt.title(f"{distribution_type} Distribution")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        if distribution_type == 'Normal':
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = stats.norm.pdf(x, self.mean, self.std_dev)
            plt.plot(x, p, 'k', linewidth=2)
        plt.show()

    def get_info(self):
        print(f"Number of data points: {self.n}")
        print(f"Mean: {self.mean}")
        print(f"Standard deviation: {self.std_dev}")
