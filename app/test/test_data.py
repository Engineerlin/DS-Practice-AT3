import unittest
from src.data import Dataset

file_url = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
df_pd = pd.read_csv(file_url, nrows=1000, parse_dates=['Date/Time'])
data=Dataset(name='filename',df=df_pd)

class TestGetName(unittest.TestCase):
    def test(self):
       expected = 'filename'
       result = data.get_name()
       self.assertEqual(result, expected) 


if __name__ == '__main__':
    unittest.main()