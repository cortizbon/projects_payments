import streamlit as st
import boto3
import pandas as pd

st.title("Payment info download")

st.write("Write the nickname in your email. If your mail is pepo90@lmail.com, write 'pepo90', no spaces.")

var_name = st.text_input("Write the nickname in your email. If your mail is pepo90@lmail.com, write 'pepo90', no spaces.")

s3 = boto3.client('s3', 
                  region_name='us-east-1')

bucket_name = 'bucket-csv-files'

response = s3.list_objects_v2(Bucket=bucket_name)

s3.download_file(Bucket=bucket_name,
    Key=f"pay_info/{var_name}/grouped.csv",
    Filename=f"{var_name}_grouped.csv")

s3.download_file(Bucket=bucket_name,
    Key=f"pay_info/{var_name}/projects.csv",
    Filename=f"{var_name}_projects.csv")

col1, col2 = st.columns(2)

df1 = pd.read_csv(f"{var_name}_projects.csv")
df2 = pd.read_csv(f"{var_name}_grouped.csv")

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv1 = convert_df(df1)
csv2 = convert_df(df2)

with col1:
    st.download_button("Download detailed projects info here.",
                       csv1,
                       f"{var_name}_projects.csv")

with col2:
    st.download_button("Download grouped info here.",
                       csv2,
                       f"{var_name}_grouped.csv")
