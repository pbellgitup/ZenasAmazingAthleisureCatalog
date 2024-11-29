# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Welcome to Zena's Amazing Athleisure Catalog Site
    """
)


#name_on_order = st.text_input("Name on Smoothie:")
#st.write("The name on your Smoothie will be: ", name_on_order)


session = get_active_session()
my_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").select(col('color_or_style'), col('price'), col('size_list'), col('upsell_product_desc'), col('file_url'))
#st.dataframe(data=my_dataframe, use_container_width=True)


selected_color = st.selectbox(
    'Pick a sweatsuit color or style'
    , my_dataframe
)

st.write(selected_color)
st.write(price)
st.stop()

