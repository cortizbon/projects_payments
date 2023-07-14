import streamlit as st
import boto3
from botocore.exceptions import ClientError
import pandas as pd
from utils import client, return_df

st.title("Payment info download")



var_name = st.text_input("Write the nickname in your email. If your mail is pepo90@lmail.com, write 'pepo90', no spaces.")

if not var_name:
  st.warning('Write your nickname.')
  st.stop()

try:

    client(var_name)
    csv1, csv2 = return_df(var_name)

    col1, col2 = st.columns(2)

    with col1:
        st.download_button("Download detailed projects info here.",
                            csv1,
                            f"{var_name}_projects.csv")

    with col2:
        st.download_button("Download grouped info here.",
                            csv2,
                            f"{var_name}_grouped.csv")
        
except:
    st.error("Your name is not correct. Try again.")



    
