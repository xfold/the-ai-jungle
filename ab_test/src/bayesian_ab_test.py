import numpyro
from numpyro import handlers
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.power import tt_ind_solve_power
import copy


class BayesianABTest:
    """
    This class performs Bayesian A/B testing using MCMC (Markov chain Monte Carlo) simulation.
    
    Attributes:
        data_A (numpy array): Array of data from group A.
        data_B (numpy array): Array of data from group B.
        priors (dict): Dictionary containing prior distributions for the model parameters.
        posterior_samples (dict): Dictionary containing samples drawn from the posterior distributions of the model parameters.
    """
    def __init__(self, data_A, data_B, priors):
        """
        Initializes the BayesianABTest object.
        
        Parameters:
            data_A (numpy array): Array of data from group A.
            data_B (numpy array): Array of data from group B.
            priors (dict): Dictionary containing prior distributions for the model parameters.
        """
        self.data_A = data_A
        self.data_B = data_B
        self.priors = copy.deepcopy(priors)
        self.posterior_samples = None

    def model(self, data_A, data_B):
        """
        Defines the model for the Bayesian A/B test.
        
        Parameters:
            data_A (numpy array): Array of data from group A.
            data_B (numpy array): Array of data from group B.
        """
        mu_A = numpyro.sample('mu_A', self.priors['mu_A'])
        mu_B = numpyro.sample('mu_B', self.priors['mu_B'])
        sigma_A = numpyro.sample('sigma_A', self.priors['sigma_A'])
        sigma_B = numpyro.sample('sigma_B', self.priors['sigma_B'])
        numpyro.sample('data_A_obs', dist.Normal(mu_A, sigma_A), obs=data_A)
        numpyro.sample('data_B_obs', dist.Normal(mu_B, sigma_B), obs=data_B)

    def plot_distributions(self, priors, title):
        """
        Plots the distributions of the provided priors.
        
        Parameters:
            priors (dict): Dictionary containing prior distributions to be plotted.
            title (str): The title of the plot.
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        for ax, (param, dist) in zip(axs.ravel(), priors.items()):
            rng_key = jax.random.PRNGKey(0)
            samples = dist.sample(rng_key, (10000,))
            sns.histplot(samples, ax=ax, kde=True)
            ax.set_title(f'{title} of {param}')

        plt.tight_layout()
        plt.show()

    def plot_posterior_samples(self):
        """
        Plots the posterior distributions of the model parameters.
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        for ax, (param, samples) in zip(axs.ravel(), self.posterior_samples.items()):
            sns.histplot(samples, ax=ax, kde=True)
            ax.set_title(f'Posterior distribution of {param}')
        plt.tight_layout()
        plt.show()

    def plot_posterior_samples_dens(self):
        """
        Plots the density of the posterior distributions of 'mu' and 'sigma' for both groups.
        """
        fig, axs = plt.subplots(2, figsize=(10, 8))

        sns.kdeplot(self.posterior_samples['mu_A'], ax=axs[0], fill=True, label="Store A", color='blue')
        sns.kdeplot(self.posterior_samples['mu_B'], ax=axs[0], fill=True, label="Store B", color='orange')
        axs[0].set_title('Posterior distributions of mu')
        axs[0].legend()

        sns.kdeplot(self.posterior_samples['sigma_A'], ax=axs[1], fill=True, label="Store A", color='blue')
        sns.kdeplot(self.posterior_samples['sigma_B'], ax=axs[1], fill=True, label="Store B", color='orange')
        axs[1].set_title('Posterior distributions of sigma')
        axs[1].legend()

        plt.tight_layout()
        plt.show()

    def run(self):
        """
        Runs the Bayesian A/B test, including plotting of prior distributions, MCMC simulation, plotting of posterior distributions, 
        and calculation of required sample size for a power of 0.95.
        """
        # Plot the prior distributions
        self.plot_distributions(self.priors, 'Prior distribution')

        # Run MCMC
        kernel = NUTS(self.model)
        mcmc = MCMC(kernel, num_warmup=500, num_samples=2000)
        mcmc.run(jax.random.PRNGKey(0), data_A=self.data_A, data_B=self.data_B)

        # Extract the posterior samples
        self.posterior_samples = mcmc.get_samples()

        # Plot the posterior distributions
        self.plot_posterior_samples()

        # Plot the density functions
        self.plot_posterior_samples_dens()

        # Calculate the required sample size for a power of 0.95
        effect_size = (self.posterior_samples['mu_B'].mean() - self.posterior_samples['mu_A'].mean()) / self.posterior_samples['sigma_A'].mean()
        sample_size = tt_ind_solve_power(effect_size=effect_size, alpha=0.05, power=0.95, ratio=1)
        print(f"Required sample size for 95% power: {sample_size:.2f} per group")

        print( mcmc.print_summary() )
