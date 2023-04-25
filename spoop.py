import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = 'assets/data.csv'

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

st.title('Uber pickups in NYC')

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')

st.subheader('Вывести пасажиров с указанным возрастом:')

p_by_age = st.slider('Возраст', 30, 60,0)
filtered_data = #
st.map(filtered_data)


st.subheader('Имена пасажиров, стоймость билета которых выше:')

ticket_cost = st.number_input('Стоимость билета:')
filtered_data = #
st.map(filtered_data)


st.subheader('Класс, имя и возраст спасенных, имя которых начинается с:')

p_name = st.text_input('Имя:')
filtered_data = #
st.map(filtered_data)



