import boto3
import pandas as pd
import streamlit as st

def client(var_name):
    s3 = boto3.client('s3', 
                        region_name='us-east-1', 
                        aws_access_key_id=st.secrets['one'], 
                        aws_secret_access_key=st.secrets['two'])

    bucket_name = 'bucket-csv-files'

    s3.download_file(Bucket=bucket_name,
            Key=f"pay_info/{var_name}/grouped.csv",
            Filename=f"{var_name}_grouped.csv")

    s3.download_file(Bucket=bucket_name,
            Key=f"pay_info/{var_name}/projects.csv",
            Filename=f"{var_name}_projects.csv")
    
    df1 = pd.read_csv(f"{var_name}_projects.csv")
    df2 = pd.read_csv(f"{var_name}_grouped.csv")

def return_df(var_name):
    df1 = pd.read_csv(f"{var_name}_projects.csv")
    df2 = pd.read_csv(f"{var_name}_grouped.csv")
    csv1 = df1.to_csv(df1, index=False).enconde('utf-8')
    csv2 = df2.to_csv(df1, index=False).enconde('utf-8') 
    return csv1, csv2