# importing libraries

import gspread
import pandas as pd
import streamlit as st
from google.oauth2 import service_account

# defining function to get the data from the google spreadsheet


def get_data(sheet_name):

    # Authenticate and open the Google Sheet
    credentials_dict = st.secrets['gcp_service_account']
    credentials = service_account.Credentials.from_service_account_info(credentials_dict, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])

    gc = gspread.Client(auth=credentials)
    wks = gc.open(sheet_name).sheet1

    # Get all the values from the Google Sheet
    data = wks.get_all_values()

    # Specify column names (assuming the first row of the Google Sheet contains column headers)
    column_names = data[0]

    # Create a Pandas DataFrame from the data, skipping the first row (header row)
    df = pd.DataFrame(data[1:], columns=column_names)

    # Convert columns to appropriate data types
#    df['Date'] = pd.to_datetime(df['Date'])
#    df['Temperature'] = pd.to_numeric(
#        df['Temperature'].str.replace(',', '.'), errors='coerce')
#    df['Temperature feels like'] = pd.to_numeric(
#        df['Temperature feels like'].str.replace(',', '.'), errors='coerce')
#    df['Temperature Min'] = pd.to_numeric(
#        df['Temperature Min'].str.replace(',', '.'), errors='coerce')
#    df['Temperature Max'] = pd.to_numeric(
#        df['Temperature Max'].str.replace(',', '.'), errors='coerce')
#    df['Humidity'] = pd.to_numeric(
#        df['Humidity'], errors='coerce').astype('Int8')
#    df['Wind Speed'] = pd.to_numeric(
#        df['Wind Speed'].str.replace(',', '.'), errors='coerce')

    return df


data = get_data('weathering heights')


# Streamlit app
st.set_page_config(page_title='Weather app - Home', layout='centered')

# Adding a title and description
st.title('Weather in Berlin')
st.title(':sun_small_cloud: :barely_sunny: :partly_sunny_rain: :rain_cloud: :snow_cloud:')

st.divider()

st.header(':book:  Description:')
st.write("Welcome to the 3 day weather forecaster")

st.divider()

st.header(':gear:  How to Use It:')
st.write('Navigate to the data you want using the sidebar on the left:')
st.markdown(
    ":gray[1.]  **Home:** U R here.")
st.markdown(":gray[2.]  **Raw Data:** Raw, unfiltered data. Probably not why you're here.")
st.markdown(":gray[3.]  **Data Visualization:** Weather forecast with a few parameters. Woohoo.")

st.divider()

st.header(':crystal_ball:  Forecast Updates:')
st.write("This updates daily with a 5 day forecast. Prepare to have your mind blown I guess")

# Applying session_state[] to the data  transfer the dataframe (data) across the pages
st.session_state['data'] = data

# streamlit run streamlit_app.py
