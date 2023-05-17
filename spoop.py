import streamlit as st
import pandas as pd
import numpy as np
import functions


DATA_URL = './assets/data.csv';
core = functions.AppFunctions(DATA_URL);

st.title('Приложуха');

st.subheader('Вывести пасажиров с указанным возрастом:');

p_by_age = st.slider('Возраст', 30, 60, value=(30, 60));
filtered_data = core.find_men_by_age(p_by_age[0], p_by_age[1]);
st.dataframe(filtered_data);


st.subheader('Имена пасажиров, стоймость билета которых выше:');

ticket_cost = st.number_input('Стоимость билета:');
filtered_data = core.get_names_by_fare(ticket_cost);
st.dataframe(filtered_data);


st.subheader('Класс, имя и возраст спасенных, имя которых начинается с:');

p_name = st.text_input('Имя:');
filtered_data = core.find_passengers_by_name_start(p_name);
st.dataframe(filtered_data);



