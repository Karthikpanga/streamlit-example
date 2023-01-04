import streamlit as st
import plotly.express as px
import tableauserverclient as TSC

import snowflake.connector

import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar:
    choose = option_menu("App Gallery", ['Tableau', 'ml'])
    if choose == 'Tableau':
        if 'cur' not in st.session_state:
            
                def check_password():
                    """Returns `True` if the user had a correct password."""

                    def password_entered():
                        """Checks whether a password entered by the user is correct."""
                        if (
                            st.session_state["username"] in st.secrets["passwords"]
                            and st.session_state["password"]
                            == st.secrets["passwords"][st.session_state["username"]]
                        ):
                            st.session_state["password_correct"] = True
                            del st.session_state["password"]  # don't store username + password
                            #del st.session_state["username"]
                        else:
                            st.session_state["password_correct"] = False

                    if "password_correct" not in st.session_state:
                        # First run, show inputs for username + password.
                        st.text_input("Username", on_change=password_entered, key="username")
                        st.text_input(
                            "Password", type="password", on_change=password_entered, key="password"
                        )
                        return False
                    elif not st.session_state["password_correct"]:
                        # Password not correct, show input + error.
                        st.text_input("Username", on_change=password_entered, key="username")
                        st.text_input(
                            "Password", type="password", on_change=password_entered, key="password"
                        )

                        st.error("😕 User not known or password incorrect")
                        return False
                    else:
                        # Password correct.
                        return True

if check_password():
  with st.expander('Tableau'):
    
    if st.session_state["username"] == 'streamlit1':
       st.markdown ("#### Dashboard")
       server_url = 'https://prod-useast-a.online.tableau.com'
       user = 'amulya.s.nidhi@kipi.bi'
       password = 'Kipithon@123'
       site = 'Site21'

       tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
       server = TSC.Server(server_url, use_server_version=True)

       # Fetch the dashboards/charts
       @st.experimental_memo(ttl=1200)
       def run_query(view_name):
         with server.auth.sign_in(tableau_auth):
           workbooks, pagination_item = server.workbooks.get()
           for w in workbooks:
             if w.name == 'ourworkbook':
               our_workbook = w
               break
       # Get views for trydashboard workbook.
           server.workbooks.populate_views(our_workbook)
           for v in our_workbook.views:
             if view_name == v.name:
               our_view = v
               break
       #Get an image for the view.
           server.views.populate_image(our_view)
           view_image = our_view.image
           return view_image

       view_image = run_query('MyDash')
       st.image(view_image, width=800)
    else:
        st.write("bye!")
                    
        
 # set_page_config needs to be the first Streamlit command in your script
#st.set_page_config(layout="wide")
#st.title("FOREX Forecasting Models Monitoring")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
       
                

    
