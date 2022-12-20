import streamlit as st
st.markdown("# Page 2 ")

st.sidebar.markdown("# {Rating} VS {num_reviews} ")

st.markdown("## {Rating} VS {num_reviews} ")

import pandas as pd
import altair as alt
udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')
udemyDSname = st.selectbox("Select your level",udemyDS['level'].unique())
st.write(udemyDSname)
plot_type=st.radio("select the plot type",['scatter','line','point','bar'])
color = st.color_picker('Pick A Color', '#00f900')
if plot_type == 'scatter':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_circle(color=color).encode(
    x='Rating', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
elif plot_type == 'point':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_point(color=color).encode(
    x='Rating', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
elif plot_type == 'bar':
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_bar(color=color).encode(
    x='Rating', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
else:
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_line(color=color).encode(
    x='Rating', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
).interactive()
st.altair_chart(pl)
