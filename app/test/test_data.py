import unittest
import pandas as pd
from src.data import Dataset


file_url = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
df_pd = pd.read_csv(file_url, nrows=1000, parse_dates=['Date/Time'])
df_pd.columns =['datetime', 'lat', 'lon', 'base']
data=Dataset(name='filename',df=df_pd)

class TestGetName(unittest.TestCase):
    def test(self):
       expected = 'filename'
       result = data.get_name()
       self.assertEqual(result, expected) 

class TestGet_n_Rows(unittest.TestCase):
    def test(self):
       expected = 1000
       result = data.get_n_rows()
       self.assertEqual(result, expected) 

class TestGet_n_Cols(unittest.TestCase):
    def test(self):
       expected = 4
       result = data.get_n_cols()
       self.assertEqual(result, expected) 

class TestColList(unittest.TestCase):
    def test(self):
       expected = ['datetime', 'lat', 'lon', 'base']
       result = data.get_cols_list()
       self.assertEqual(result, expected) 

if __name__ == '__main__':
    unittest.main()