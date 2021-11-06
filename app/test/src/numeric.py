import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt
import numpy as np




@dataclass
class NumericColumn:
    col_name: str
    serie: pd.Series


    def get_name(self):
        """
        Return name of selected column
        """
        return self.col_name

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        return self.serie.nunique()

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        return self.serie.isna().sum()

    def get_zeros(self):
        """
        Return number of occurrence of 0 value for selected column
        """
        return self.serie.isin([0]).sum()

    def get_negatives(self):
        """
        Return number of negative values for selected column
        """
        return (self.serie < 0).sum()

    def get_mean(self):
        """
        Return the average value for selected column
        """
        return self.serie.mean()

    def get_std(self):
        """
        Return the standard deviation value for selected column
        """
        return self.serie.std()

    def get_min(self):
        """
        Return the minimum value for selected column
        """
        return self.serie.min()

    def get_max(self):
        """
        Return the maximum value for selected column
        """
        return self.serie.max()

    def get_median(self):
        """
        Return the median value for selected column
        """
        return self.serie.median()

    def get_histogram(self, column):
        """
        Return the generated histogram for selected column
        """

        df_histogram = pd.DataFrame(self.serie)
        #histogramcol = alt.Chart(df_histogram).mark_bar().encode(alt.X(column, bin=True), y='count()')
        histogramcol = alt.Chart(df_histogram).mark_bar().encode(alt.X(column, bin=alt.Bin(maxbins=50)),y='count()')
        return histogramcol

    def get_frequent(self,column):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """

        data = pd.DataFrame(self.serie[column])
        top20 = data.groupby([column]).size().reset_index(name = 'Occurrence').sort_values(by='Occurrence', ascending=False)
        top20.index = np.arange(1, len(top20) + 1)
        top20['Percentage'] = top20['Occurrence']/sum(top20['Occurrence'])
        return top20.head(20)