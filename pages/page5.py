import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.markdown("# page 5 ")

st.sidebar.markdown("# {level} VS {num_reviews} ")

st.markdown("## {level} VS {num_reviews} ")


udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')

udemyDS.groupby('level')['num_reviews'].mean().plot(kind='pie',autopct="%1.2f%%")

st.set_option('deprecation.showPyplotGlobalUse', False)

if st.button('show pie chart'):
  st.pyplot()

else:
    st.write('Press Button to show pie chart')
