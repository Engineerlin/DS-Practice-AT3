import unittest
import pandas as pd
from src.numeric import NumericColumn

file_url = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
df_pd = pd.read_csv(file_url, nrows=1000, parse_dates=['Date/Time'])
ds_pd = df_pd.iloc[:, 1]
numeric = NumericColumn(col_name='Lat', serie=ds_pd)


class TestGetName(unittest.TestCase):
    def test_get_name(self):
        expected = 'Lat'
        result = numeric.get_name()
        self.assertEqual(result, expected)


class TestGetUnique(unittest.TestCase):
    def test_get_unique(self):
        expected = 634
        result = numeric.get_unique()
        self.assertEqual(result, expected)


class TestGetMissing(unittest.TestCase):
    def test_get_missing(self):
        expected = 0
        result = numeric.get_missing()
        self.assertEqual(result, expected)


class TestGetZeros(unittest.TestCase):
    def test_get_zeros(self):
        expected = 0
        result = numeric.get_zeros()
        self.assertEqual(result, expected)


class TestGetNegative(unittest.TestCase):
    def test_get_negatives(self):
        expected = 0
        result = numeric.get_negatives()
        self.assertEqual(result, expected)


class TestGetMean(unittest.TestCase):
    def test_get_mean(self):
        expected = 40.7383235
        result = numeric.get_mean()
        self.assertEqual(result, expected)


class TestGetStd(unittest.TestCase):
    def test_get_std(self):
        expected = 0.04994672013858984
        result = numeric.get_std()
        self.assertEqual(result, expected)


class TestGetMin(unittest.TestCase):
    def test_get_min(self):
        expected = 40.2201
        result = numeric.get_min()
        self.assertEqual(result, expected)


class TestGetMax(unittest.TestCase):
    def test_get_max(self):
        expected = 41.0628
        result = numeric.get_max()
        self.assertEqual(result, expected)


class TestGetMedian(unittest.TestCase):
    def test_get_median(self):
        expected = 40.7447
        result = numeric.get_median()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()