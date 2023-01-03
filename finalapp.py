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
        placeholder = st.empty()
        if 'cur' not in st.session_state:
            with placeholder.form("login-form", clear_on_submit=True):
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
                        if  st.session_state["username"] == 'streamlit1':
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
                        elif st.session_state["username"] == 'streamlit2':

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

                            view_image = run_query('newdash')
                            st.image(view_image, width=800)
                        else:
                            st.write("bye!")
        
 # set_page_config needs to be the first Streamlit command in your script
#st.set_page_config(layout="wide")
#st.title("FOREX Forecasting Models Monitoring")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
    elif choose == 'ml':
        if 'cur' not in st.session_state:
            with placeholder.form("login-form", clear_on_submit=True):
                @st.experimental_singleton
                def init_connection():
                    return snowflake.connector.connect(
                        **st.secrets["snowflake"], client_session_keep_alive=True
                    )

                conn = init_connection()

                def load_data():
                   #rows = run_query("SELECT * from mytable;")
                   cur = conn.cursor().execute("select CURRENT_ACCOUNT();")
                  # cur = conn.cursor().execute(query)
                   return cur.fetch_pandas_all()

                @st.experimental_memo(ttl=600)
                def run_query(query):
                    with conn.cursor() as cur:
                        cur.execute(query)
                        return cur.fetchall()

                #rows = run_query("select * from ML;")


                actual=run_query("select ACTUAL from ACTVSPREC limit 5;")
                prediction=run_query("select PREDICTIONS from ACTVSPREC limit 5;")
                date=run_query("select DDATE from ACTVSPREC limit 5 ;")


                # Create DataFrame from multiple lists


                df2=pd.DataFrame(list(zip(date,actual,prediction)),columns=['date','actual','prediction'])
                st.write(df2)

                #chart_data = pd.DataFrame(
                 #   np.random.randn(20, 3),
                 #   columns=['a', 'b', 'c'])

                #st.line_chart(rows)
                line_fig = px.line(
                   df2,
                   x="date",
                   y=["actual", "prediction"],
                   title="Actual Values vs Forecasted values",

                )
                #legend_names = {"sales": "Actual Sales", "sales_forecast": "Forecasted Sales"}
                line_fig.update_layout(
                   xaxis=dict(showgrid=False),
                   legend=dict(
                       yanchor="top",
                       y=0.99,
                       xanchor="right",
                       x=0.99
                   ),
                   title_x=0.5,
                   height=600
                )

                # passing in the Plotly graph object to Streamlit
                #st.plotly_chart(line_fig, use_container_width=True)


                df = pd.DataFrame({
                  'date': ['12/28/2022','12/29/2022','12/30/2022','12/31/2022','01/1/2023','01/2/2023', '01/3/2023', '01/4/2023','01/5/2023','01/6/2023'],
                  'Actual': [ 46.53, 46.53,  46.54, 46.64,46.645,46.62,46.665,46.63,46.7,46.68],
                    'Prediction':[ 46.52, 46.530, 46.52, 46.54,46.66,46.643,46.624,46.666,46.619,46.721]
                })






                # Print results.


                st.line_chart(df, x="date",
                   y=["Actual", "Prediction"])

    
