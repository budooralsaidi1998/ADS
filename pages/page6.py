import streamlit as st
import pandas as pd
import altair as alt

st.markdown("# page 6 ")

st.sidebar.markdown("# {course_id} VS {price} ")

st.markdown("## {course_id} VS {price} ")

udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')

chartfoot = alt.Chart(udemyDS).mark_circle().encode(
x = 'course_id',
y = 'price' ,
    size='num_reviews',
    color='level',
tooltip=['course_id','num_reviews','Rating','price']).interactive()
st.altair_chart(chartfoot)
