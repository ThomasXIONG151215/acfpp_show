import streamlit as st
from show_canopy import show_canopy
from show_forecast import show_forecast
from show_optimize import show_optimize
from show_plan import show_plan
from show_context import show_context
import plotly.express as px 

st.title('7-11月工作')

with st.sidebar:
    page = st.radio('选择模块',options = ['研究目标','作物长势','温度分布预测','空调流场预测规划','后续计划'])

if page == '研究目标':
    show_context()

elif page == '作物长势':
    show_canopy()

elif page == '温度分布预测':
    show_forecast()
    
elif page == '空调流场预测规划':
    show_optimize()
     
elif page == '后续计划':
    show_plan()
