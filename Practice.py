import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2022, 2030)
y = np.exp(np.arange(len(x)))

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.title('Forecast of # of companies adopting Generative AI')
plt.plot(x, y)
plt.ylabel('# of Firms')
plt.xlabel('Year')
st.pyplot()
