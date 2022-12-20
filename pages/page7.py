import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# page 7 ")

st.sidebar.markdown("# {num_lectures} VS {level} ")

st.markdown("## {num_lectures} VS {level} ")

udemyDS = pd.read_csv('3.1-data-sheet-udemy-courses-business-courses.csv')
udemyDS.drop(udemyDS.index[-1], inplace=True)
st.title('udemyDS Application')

fig, axes = plt.subplots()

axes.stem(udemyDS['num_lectures'],udemyDS['level'], use_line_collection=True, basefmt=' ')
axes.set_ylim(0)

plt.title('num of lectures for each level')
plt.xlabel('num_lectures')
plt.ylabel('level')
plt.xticks(udemyDS.num_lectures)
fig.set_figwidth(25)
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
