# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from itertools import product
import numpy as np

# Register matplotlib converters to properly handle datetime objects in plots
register_matplotlib_converters()
# Set the style for seaborn plots
sns.set(style="whitegrid")

class TradeAnalyser:
    """
    A class used to analyze a trading dataset

    ...

    Attributes
    ----------
    df : pandas.DataFrame
        the dataset to analyze
    numerical_columns : list
        the numerical columns in the dataset
    categorical_columns : list
        the categorical columns in the dataset
    time_column : str
        the time column in the dataset for time series analysis
    """

    def __init__(self, df, numerical_columns, categorical_columns, time_column):
        """
        Constructs all the necessary attributes for the AdvancedDatasetAnalyzer object.

        Parameters:
            df (pandas.DataFrame): The input dataframe.
            numerical_columns (list): The list of numerical columns in the dataframe.
            categorical_columns (list): The list of categorical columns in the dataframe.
            time_column (str): The datetime column in the dataframe for time series analysis.
        """
        self.df = df
        self.numerical_columns = numerical_columns
        self.categorical_columns = categorical_columns
        self.time_column = time_column

    def handle_missing_values(self, strategy='mean'):
        """
        Handles missing values in the dataset according to the specified strategy.
        """
        if self.df.isnull().sum().sum() == 0:
            print("No missing values found.")
        else:
            print(f"Missing values detected. Applying '{strategy}' strategy.")

            if strategy == 'drop':
                self.df.dropna(inplace=True)
            elif strategy == 'mean':
                self.df.fillna(self.df.mean(), inplace=True)
            elif strategy == 'median':
                self.df.fillna(self.df.median(), inplace=True)
            elif strategy == 'mode':
                self.df.fillna(self.df.mode().iloc[0], inplace=True)

            print("Missing values have been handled.")

    def handle_outliers(self, strategy='cap'):
        """
        Detects and handles outliers in the dataset according to the specified strategy.
        """
        Q1 = self.df[self.numerical_columns].quantile(0.25)
        Q3 = self.df[self.numerical_columns].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR

        is_outlier = ((self.df[self.numerical_columns] < lower_bound) | 
                      (self.df[self.numerical_columns] > upper_bound)).any(axis=1)

        if is_outlier.sum() == 0:
            print("No outliers detected.")
        else:
            print(f"Outliers detected. Applying '{strategy}' strategy.")

            if strategy == 'drop':
                self.df = self.df[~is_outlier]
            elif strategy == 'cap':
                for col in self.numerical_columns:
                    self.df[col] = self.df[col].clip(lower_bound[col], upper_bound[col])

            print("Outliers have been handled.")

    def balance_per_codeName(self, plot_type='box', color='blue'):
        """
        Shows the balance distribution for each CodeName.

        Parameters:
        plot_type (str, optional): The type of plot to display. Options are 'box', 'bar'. Default is 'box'.
        color (str, optional): The color of the plot. Default is 'blue'.

        Returns:
        None
        """
        plt.figure(figsize=(10, 5))
        if plot_type == 'box':
            sns.boxplot(x='CodeName', y='Balance', data=self.df, color=color)
        elif plot_type == 'bar':
            sns.barplot(x='CodeName', y='Balance', data=self.df, color=color)
        plt.title('Balance Distribution per CodeName')
        plt.show()

    def descriptive_statistics(self):
        """
        Generates descriptive statistics of the dataframe.

        Returns:
        pandas.DataFrame: The descriptive statistics of the dataframe.
        """
        return self.df.describe(include='all')

    def distribution_variables(self):
        """
        Plots the distribution of numerical variables in the dataframe.

        Returns:
        None
        """
        for col in self.numerical_columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.show()

    def correlation_analysis(self):
        """
        Plots the correlation matrix of numerical variables in the dataframe.

        Returns:
        None
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df[self.numerical_columns].corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

    def time_series_analysis(self):
        """
        Plots the time series of numerical variables in the dataframe.

        Returns:
        None
        """
        df_copy = self.df.copy()
        df_copy.set_index(self.time_column, inplace=True)
        df_copy[self.numerical_columns].plot(subplots=True, layout=(len(self.numerical_columns),1), figsize=(10, 6*len(self.numerical_columns)))
        plt.title('Time Series Analysis')
        plt.tight_layout()
        plt.show()

    def balance_cdf_per_codename(self):
        """
        Plots the CDF of balance per codename in the dataframe.

        Returns:
        None
        """
        plt.figure(figsize=(10, 5))
        for codename in self.df['CodeName'].unique():
            subset = self.df[self.df['CodeName'] == codename]
            subset['Balance'].hist(cumulative=True, density=1, bins=100, histtype='step', label=codename)

        plt.title('CDF of Balance per CodeName')
        plt.xlabel('Balance')
        plt.ylabel('Likelihood of occurrence')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def empirical_distribution_per_codename(self):
        """
        Plots the empirical distribution of balance per codename in the dataframe.

        Returns:
        None
        """
        plt.figure(figsize=(10, 5))
        for codename in self.df['CodeName'].unique():
            subset = self.df[self.df['CodeName'] == codename]
            sns.kdeplot(subset['Balance'], label=codename)

        plt.title('Empirical Distribution of Balance per CodeName')
        plt.xlabel('Balance')
        plt.ylabel('Density')
        plt.legend()
        plt.grid(True)
        plt.show()

    def codename_performance_analysis(self):
        """
        Analyzes and plots the performance of each codename in the dataframe.

        Returns:
        None
        """
        performance_stats = self.df.groupby('CodeName')['Balance'].agg(['mean', 'median', 'sum', 'count'])
        performance_stats.sort_values(by='sum', ascending=False, inplace=True)

        colors = plt.cm.viridis(np.linspace(0, 1, len(performance_stats)))

        fig, axes = plt.subplots(4, 1, figsize=(10, 20))

        axes[0].bar(performance_stats.index, performance_stats['mean'], color='b')
        axes[0].set_title('Mean Balance per CodeName')
        axes[0].set_ylabel('Mean Balance')

        axes[1].bar(performance_stats.index, performance_stats['median'], color='r')
        axes[1].set_title('Median Balance per CodeName')
        axes[1].set_ylabel('Median Balance')

        axes[2].bar(performance_stats.index, performance_stats['sum'], color=colors)
        axes[2].set_title('Total Balance per CodeName')
        axes[2].set_ylabel('Total Balance')

        axes[3].pie(performance_stats['count'], labels=performance_stats.index, colors=colors, autopct='%1.1f%%')
        axes[3].set_title('Count of Trades per CodeName')

        for ax in axes[:-1]:
            ax.set_xlabel('CodeName')
            ax.set_xticks(range(len(performance_stats)))
            ax.set_xticklabels(performance_stats.index, rotation=90)

        plt.tight_layout()
        plt.show()

    def empirical_distribution_per_codename_full(self):
        """
        Plots the empirical distribution of balance per codename in the dataframe, 
        once with all data and then separately for each month and year.

        Returns:
        None
        """
        # Convert 'OpenTradeDatetime' to datetime if it is not already
        if self.df[self.time_column].dtype != 'datetime64[ns]':
            self.df[self.time_column] = pd.to_datetime(self.df[self.time_column], format="%d/%m/%Y %H:%M:%S")

        # Create new columns for the year and month
        self.df['Year'] = self.df[self.time_column].dt.year
        self.df['Month'] = self.df[self.time_column].dt.month

        # Create a color palette
        codenames = self.df['CodeName'].unique()
        colors = plt.cm.viridis(np.linspace(0, 1, len(codenames)))
        color_dict = dict(zip(codenames, colors))

        # Get the unique years and months in ascending order
        years = sorted(self.df['Year'].unique())
        months = sorted(self.df['Month'].unique())

        # Create a figure with a subplot for each year, month, and each codename
        fig, axes = plt.subplots(len(years) * len(months) + 1, len(codenames), figsize=(5 * len(codenames), 5 * (len(years) * len(months) + 1)))

        for i, codename in enumerate(codenames):
            subset = self.df[self.df['CodeName'] == codename]
            balance_min = subset['Balance'].min()
            balance_max = subset['Balance'].max()

            # All data
            sns.kdeplot(subset['Balance'], ax=axes[0, i], color=color_dict[codename])
            axes[0, i].set_title(f'All Data ({codename}, n={len(subset)})')
            axes[0, i].set_xlabel('Balance')
            axes[0, i].set_ylabel('Density')
            axes[0, i].set_xlim(balance_min-100, balance_max+100)

            # Year by year, month by month
            for j, (year, month) in enumerate(product(years, months), start=1):
                year_month_subset = subset[(subset['Year'] == year) & (subset['Month'] == month)]
                if not year_month_subset.empty:
                    sns.kdeplot(year_month_subset['Balance'], ax=axes[j, i], color=color_dict[codename])
                    axes[j, i].set_title(f'{year}-{month:02d} ({codename}, n={len(year_month_subset)})')
                    axes[j, i].set_xlabel('Balance')
                    axes[j, i].set_ylabel('Density')
                    axes[j, i].set_xlim(balance_min-100, balance_max+100)

        plt.tight_layout()
        plt.show()

    def analyze(self, analyses_config=None, missing_values_strategy='mean', outliers_strategy='cap'):
        """
        Performs a comprehensive analysis of the dataset based on the specified configuration.
        """
        if analyses_config is None:
            analyses_config = {
                "handle_missing_values": True,
                "handle_outliers": True,
                "descriptive_statistics": True,
                "distribution_variables": True,
                "correlation_analysis": True,
                "time_series_analysis": True,
                "categorical_analysis": True,
                "balance_per_codeName": True,
                "codename_performance_analysis": True,
                "empirical_distribution_per_codename": True,
                "empirical_distribution_per_codename_full":True
            }

        if analyses_config.get("handle_missing_values", False):
            print("\nHandling Missing Values:")
            self.handle_missing_values(missing_values_strategy)

        if analyses_config.get("handle_outliers", False):
            print("\nHandling Outliers:")
            self.handle_outliers(outliers_strategy)

        if analyses_config.get("descriptive_statistics", False):
            print("\nDescriptive Statistics:")
            print(self.descriptive_statistics())

        if analyses_config.get("distribution_variables", False):
            print("\nDistribution of Variables:")
            self.distribution_variables()

        if analyses_config.get("correlation_analysis", False):
            print("\nCorrelation Analysis:")
            self.correlation_analysis()

        if analyses_config.get("time_series_analysis", False):
            print("\nTime Series Analysis:")
            self.time_series_analysis()

        if analyses_config.get("balance_per_codeName", False):
            print("\nBalance Distribution per CodeName:")
            self.balance_per_codeName()
        
        if analyses_config.get("balance_cdf_per_codename", False):
            print("\nCDF of Balance per CodeName:\n")
            self.balance_cdf_per_codename()
        
        if analyses_config.get("empirical_distribution_per_codename", False):
            print("\nEmpirical Distribution of Balance per CodeName:\n")
            self.empirical_distribution_per_codename()
        
        if analyses_config.get("codename_performance_analysis", False):
            print("\nPerformance Analysis of each CodeName:\n")
            self.codename_performance_analysis()
        
        if analyses_config.get("empirical_distribution_per_codename_full", False):
            print("\nEmpirical Distribution of Balance per CodeName and Month:\n")
            self.empirical_distribution_per_codename_full()