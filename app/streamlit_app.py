import streamlit as st
import pandas as pd
import altair as alt
from test.src.data import Dataset
from test.src.numeric import NumericColumn


def explore_data(file):
    global dff
    dff = pd.read_csv(file)
    st.header('1.Overall Information')
    dat = Dataset(name=file.name, df=dff)
    filename = dat.get_name()
    st.markdown("__Name of Table:__ " + filename)
    st.markdown("__Number of Rows:__ " + str(dat.get_n_rows()))
    st.markdown("__Number of Columns:__ " + str(dat.get_n_cols()))
    st.markdown("__Number of Duplicated Rows:__ " + str(dat.get_n_duplicates()))
    st.markdown("__Number of Rows with Missing Values:__ " + str(dat.get_n_missing()))
    st.subheader('List of Columns')
    col_list = dat.get_cols_list()
    col_list2 = str(dat.get_cols_list())
    st.write(col_list2)
    col_type_df = pd.DataFrame.from_dict(dat.get_cols_dtype(), orient='Index', columns=['type'])
    st.dataframe(col_type_df)
    n_row_disp = st.slider('Select the number of rows to be displayed', min_value=5, max_value=50)
    st.subheader('Top Rows of Table')
    st.dataframe(dat.get_head(n_row_disp))
    st.subheader('Bottom Rows of Table')
    st.dataframe(dat.get_tail(n_row_disp))
    st.subheader('Random Sample Rows of Table')
    st.dataframe(dat.get_sample(n_row_disp))
    sel_box = st.multiselect('Which columns do you want to convert to dates', col_list)

    for i in sel_box:
        dat.df[i] = dat.df[i].astype('datetime64[ns]')


def explore_numeric(dff):
    st.header('2. Numeric Column Information')
    num_cols = dff.select_dtypes(include='number').columns
    num_cols_df = dff.select_dtypes(include='number')
    name = num_cols
    numeric = NumericColumn(name, num_cols_df)
    col_index = 0

    for col in range(len(num_cols)):
        col_names = numeric.get_name()[col]
        st.subheader(f'2.{col_index} Field Name: **_{col_names}_**')
        col_index = col_index + 1
        unique = numeric.get_unique().iloc[col]
        missing = numeric.get_missing().iloc[col]
        zero = numeric.get_zeros().iloc[col]
        negative = numeric.get_negatives().iloc[col]
        average = numeric.get_mean().iloc[col]
        st_dev = numeric.get_std().iloc[col]
        min_val = numeric.get_min().iloc[col]
        max_val = numeric.get_max().iloc[col]
        med_val = numeric.get_median().iloc[col]
        d = {' ': ["Number of Unique Values:",
                   "Number of rows with missing values:",
                   "Number of rows with 0:", "Number of rows with Negative values:",
                   "Average value:",
                   "Standard Deviation value:",
                   "Minimum Value:",
                   "Maximum Value:",
                   "Median Value:"],
             'Value': [unique, missing, zero, negative, average, st_dev, min_val, max_val, med_val]}
        df_field = pd.DataFrame(d)
        df_field2 = df_field.assign(hack='').set_index('hack')
        st.dataframe(data=df_field2, width=500)
        st.subheader('**Histogram**')
        st.write(numeric.get_histogram(col_names))
        frequent = numeric.get_frequent(col_names)
        st.subheader('**Most Frequent Values**')
        st.dataframe(frequent)


def main():
    st.title('Data Explorer Tool')
    st.write('Choose a CSV file')
    file = st.file_uploader("Upload file", type=['csv'])
    if not file:
        st.write("EDA will start when a CSV file is uploaded")
        return
    explore_data(file)
    explore_numeric(dff)


main()
