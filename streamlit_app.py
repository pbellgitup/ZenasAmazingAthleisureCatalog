# Import python packages
import streamlit as st
import requests
import pandas as pd


# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Welcome to Zena's Amazing Athleisure Catalog Site
    """
)

#  Establish connection for Streamlit
cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").select(col('color_or_style'), col('price'), col('size_list'), col('upsell_product_desc'), col('file_url'))

# Convert the Snowpark Dataframe to a Pandas Dataframe so we can use the LOC function
pd_df = my_dataframe.to_pandas()


st.dataframe(data=my_dataframe, use_container_width=True)

st.stop()


selected_color = st.selectbox(
    'Pick a sweatsuit color or style'
    , my_dataframe
)

st.write(selected_color)
st.write(price)
st.stop()

