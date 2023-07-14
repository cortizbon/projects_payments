import streamlit as st
import boto3
import pandas as pd
from utils import client, return_df

st.title("Payment info download")

st.write("Write the nickname in your email. If your mail is pepo90@lmail.com, write 'pepo90', no spaces.")

var_name = st.text_input("Write the nickname in your email. If your mail is pepo90@lmail.com, write 'pepo90', no spaces.")

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
    st.warning("Either your nickname is not correct or you have not written any name.")
