import streamlit as st
import openai
import json
import numpy as np
import warnings
import matplotlib.pyplot as plt
import plotly.express as px
warnings.filterwarnings('ignore')
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from langchain.agents import Tool,Agent
from langchain.chat_models import ChatOpenAI 
import os,re,json
from langchain.document_loaders import UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
from streamlit_chat import message
from langchain.memory import ConversationBufferMemory
from rfp import *
from main import *
from database import get_sql_query


st.set_page_config(layout='wide')


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Source Sans Pro', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:tomato;padding:3px">
    <h2 style="color:white;text-align:center;padding:3px">Data Insights as Service</h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

def val_ls(values_input):
    try:
        input_values = values_input.split(',')
        input_values = [value.strip() for value in input_values]

        # Remove empty values from the list (if any)
        input_values = [value for value in input_values if value]
        return input_values
    except Exception as e:
         return e


with st.container():
    Name = st.selectbox(
    'Select Application Name:',
    ('pega','sf'))

url="http://172.19.137.8:8888/"+str(Name)
# st.write(url)

colp, colq = st.columns(2)

with colp.container():
    object_val = st.selectbox(
    'Select Object:',
    ('CLAIMS','CUSTOMER'))

with colq.container():
    InsightKey = st.selectbox(
    'Select Insight Key:',
    ('FRAUD_GE','TOP_N_FRAUD_IN_N_YEAR','FRAUD_GE_IN_N_YEAR','CUST_CLAIMS_N_YEAR','CUST_FRAUD_N_YEAR','CUST_FRAUD_PRCNT_N_YEAR'))

user_input=st.text_input("Enter Values:")
if user_input!="":
     col1, col2, col3 = st.columns(3)
     if col2.button("Get Insights"):
          user_input1=val_ls(user_input)
        #   st.write(Name,"**",object_val,"**",InsightKey,"**",user_input1)
          data = {
                "object": object_val,
                "reqkey": InsightKey,
                "user_input": user_input1
            }
          json_string = json.dumps(data)
          st.write(json_string)

else:
     col1, col2, col3 = st.columns(3)
     if col2.button("Get Insights"):
         st.write("please enter input")
     






# input_string = st.text_input("String:")
# if input_string:
#     with st.spinner("Please wait while we answer your question..."):
#         sql_query=get_sql_query(input_string)
#         st.success(sql_query) 