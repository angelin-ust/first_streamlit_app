import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError

streamlit.title('My Moms New Healthy Dine')

streamlit.header('Breakfast Favourite')

streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new session
streamlit.header('345')
#create the repeatable code block (called a function)
def get_fruitvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized



# new session
streamlit.header('123')
streamlit.header('fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    back_from_function=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()




#import requests

#streamlit.text(fruityvice_response.json())
 #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# take the json version of the respond and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)

# streamlit.stop()

#import snowflake.connector

#some function
streamlit.header('789')

#allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      fruit_values = jackfruit + " " + papaya + " " + guava + " " + kiwi  # Concatenate the fruit values with a space delimiter
      my_cur.execute("insert into fruit_load_list values('" + fruit_values + "')")
      return "Thank for adding" + new_fruit


#Add a button to load the furit
#-----------------------
if streamlit.button('Getfruit list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows= get_fruit_load_list(fruit_values)
   my_cnx.close()
   streamlit.dataframe(my_data_rows)
#-----------------------
# add_my_fruit = streamlit.text_input('What fruit would you add?')
# if streamlit.button('Add a fruit to the list'):
#    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#    back_from_function=insert_row_snowflake(add_my_fruit)
#    streamlit.text(back_from_function)
   
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)

# add_my_fruit = streamlit.text_input('What fruit would you add?','jackfruit')
# streamlit.write('The user entered ', add_my_fruit)
# "jackfruit"+"papaya"+"guava"+"kiwi"
# my_cur.execute("insert into fruit_load_list values('from streamlit')")
