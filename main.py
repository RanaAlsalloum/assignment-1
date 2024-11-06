import numpy as np
import pandas as pd
import streamlit as st

st.title("Hi everyone")
st.write("All of you are vary nice people")

data=pd.DataFrame({"C1":['A','B','C','B','E'],
                   "C2":[100,200,300,400,500]
})

st.write("Below are your Marks")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=['P','Q','R','T']
)

st.line_chart(chart_data)
