import streamlit as st
import pandas as pd
import numpy as np
import random
st.write("Nitya Shah's Website")
databar=pd.DataFrame(np.random.random((20,3)),columns=['a','b','c'])
st.bar_chart(databar)
st.line_chart(databar)
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)
if picture:
    st.image(picture)
st.caption("Never open random links my man this could have been phishing")