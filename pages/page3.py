import streamlit as st
st.markdown("# Page 3 ")

st.sidebar.markdown("# {num_subscribers} VS {price} ")

st.markdown("## {num_subscribers} VS {price} ")

import pandas as pd
import altair as alt
udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')
udemyDSname = st.selectbox("Select your level",udemyDS['level'].unique())
st.write(udemyDSname)
plot_type=st.radio("select the plot type",['scatter','line','point','bar','area'])
if plot_type == 'scatter':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_circle().encode(
    x='num_subscribers', y='price',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
elif plot_type == 'point':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_point().encode(
    x='num_subscribers', y='price',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
elif plot_type == 'bar':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_bar().encode(
    x='num_subscribers', y='price',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
elif plot_type == 'line':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_line().encode(
    x='num_subscribers', y='price',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
else:
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_area().encode(
    x='num_subscribers', y='price',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
st.altair_chart(pl)
