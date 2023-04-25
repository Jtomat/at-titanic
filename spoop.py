import streamlit as st
import pandas as pd
import numpy as np
import functions

core = functions.AppFunctions()
DATA_URL = 'assets/data.csv'

st.title('Приложуха')

st.subheader('Вывести пасажиров с указанным возрастом:')

p_by_age = st.slider('Возраст', 30, 60)
filtered_data = core.find_men_by_age(p_by_age)
st.map(filtered_data)


# st.subheader('Имена пасажиров, стоймость билета которых выше:')
#
# ticket_cost = st.number_input('Стоимость билета:')
# filtered_data =
# st.map(filtered_data)


st.subheader('Класс, имя и возраст спасенных, имя которых начинается с:')

p_name = st.text_input('Имя:')
filtered_data = core.find_passengers_by_name_start(p_name)
st.map(filtered_data)



