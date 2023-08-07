import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("click button")

if st.button("Button"):
    st.write("why hello there")
else:
    st.write("Goodbye")

st.header("st.write")

st.write("hello world : sunglass")

st.write(1234)

df=pd.DataFrame({'first column':[1,2,3,4,5],
                'second column':[6,7,8,9,10]})
st.write(df)

st.write("below data ",df,"above data")

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b',size='c',color='c', tooltip=['a', 'b','c'])
st.write(c)


