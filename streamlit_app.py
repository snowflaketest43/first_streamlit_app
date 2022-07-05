import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('My title')

streamlit.header('Breakfast Menu')
streamlit.text('Oemga 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Create a smoothie!')



streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
