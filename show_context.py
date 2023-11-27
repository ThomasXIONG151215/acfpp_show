import streamlit as st 


def show_context():
    st.markdown('# 目标')
    st.markdown('在考虑植物生长情况的条件下快速预测出植物工厂的温度分布，然后借助这个优势生成能耗最优的空调运行算法')
    st.markdown('# 研究路线')
    st.markdown('1. 测试不同种植密度对植物生长的影响，并从中选出既能保证产量又能对流场不产生太大影响的种植密度')
    st.markdown('2. 已验证CFD模拟可靠性的情况下，训练流场代理模型来实现植物工厂的快速温度分布预测')
    st.markdown('3. 借助流场代理模型，利用三轮迭代算法生成电费-能耗-温度分布-换气次数最优的空调运行方案')
    