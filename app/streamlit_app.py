import streamlit as st
import pandas as pd
import altair as alt

from test.src.data import Dataset

def get_df(file):
    global dff
    extension = file.name.split('.')[1]
    if extension.upper() == 'CSV':
        dff = pd.read_csv(file)


def exploredata(file):
    st.header('1.Overall Information')
    dat=Dataset(name=file.name, df=pd.read_csv(file))
    filename = dat.get_name()
    st.markdown("__Name of Table:__ "+filename)
    st.markdown("__Number of Rows:__ "+str(dat.get_n_rows()))
    st.markdown("__Number of Columns:__ "+str(dat.get_n_cols()))
    st.markdown("__Number of Duplicated Rows:__ "+str(dat.get_n_duplicates()))
    st.markdown("__Number of Rows with Missing Values:__ "+str(dat.get_n_missing()))
    st.subheader('List of Columns')
    col_list=dat.get_cols_list()
    st.write(col_list)
    col_type_df=pd.DataFrame.from_dict(dat.get_cols_dtype(),orient='Index',columns=['type'])
    st.dataframe(col_type_df)
    n_row_disp=st.slider('Select the number of rows to be displayed',min_value=5, max_value=50)
    st.subheader('Top Rows of Table')
    st.dataframe(dat.get_head(n_row_disp))
    st.subheader('Bottom Rows of Table')
    st.dataframe(dat.get_tail(n_row_disp))
    sel_box=st.multiselect('Which columns do you want to convert to dates',col_list)
    for i in sel_box:
        dat.df[i]=dat.df[i].astype('datetime64[ns]')

def main():
    st.title('Data Explorer Tool')
    st.write('Choose a CSV file')
    file = st.file_uploader("Upload file", type=['csv'])
    if not file:
        st.write("Upload a .csv to get started")
        return

    exploredata(file)

main()
