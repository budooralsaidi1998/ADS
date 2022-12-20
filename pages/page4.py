import streamlit as st
st.markdown("# page 4 ")

st.sidebar.markdown("# {num_subscribers} VS {num_reviews} ")

st.markdown("## {num_subscribers} VS {num_reviews} ")

import pandas as pd
import altair as alt
udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')
udemyDSname = st.select_slider("Select your level",udemyDS['level'].unique())
st.write(udemyDSname)

options = st.multiselect(
    'choose a chart',
    ['scatter', 'point', 'bar', 'line', 'area'])


if 'scatter' in options:
  pl = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_circle().encode(
    x='num_subscribers', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
    ).interactive()
  st.altair_chart(pl)

if 'point' in options:
  pl1 = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_point().encode(
    x='num_subscribers', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
    ).interactive()
  st.altair_chart(pl1)

if 'bar' in options:
  pl2 = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_bar().encode(
    x='num_subscribers', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
    ).interactive()
  st.altair_chart(pl2)

if 'line' in options:
  pl2 = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_line().encode(
    x='num_subscribers', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
    ).interactive()
  st.altair_chart(pl2)

if 'area' in options:
  pl3 = alt.Chart(udemyDS[udemyDS['level']==udemyDSname]).mark_area().encode(
    x='num_subscribers', y='num_reviews',tooltip=['course_id','num_subscribers','num_reviews','Rating','price']
    ).interactive()
  st.altair_chart(pl3)
