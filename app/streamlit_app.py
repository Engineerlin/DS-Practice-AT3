import streamlit as st
import pandas as pd
import altair as alt
from data import Dataset



def get_df(file):
    # get extension and read file
    global df
    extension = file.name.split('.')[1]
    if extension.upper() == 'CSV':
        df = pd.read_csv(file)

def exploredata(file):
    st.header('1.Overall Information')
    dat=data(name=file.name, df=pd.read_csv(file))
    st.subheader('Name of Table:')+st.text(dat.name)
    st.subheader('Number of Rows: ')+st.text(dat.get_n_rows())
    st.subheader('Number of Columns: ')+st.text(dat.get_n_cols())


def main():
    st.title('Data Explorer Tool')
    st.write('Choose a CSV file')
    file = st.file_uploader("Upload file", type=['csv'])
    if not file:
        st.write("Upload a .csv to get started")
        return
    get_df(file)
    exploredata(file)

main()
