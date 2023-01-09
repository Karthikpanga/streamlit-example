import streamlit as st
import tableauserverclient as TSC
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import snowflake.connector

import pandas as pd
import numpy as np


# Using "with" notation
with st.sidebar:
    choose = option_menu("TRADERS CENTRAL", ['HOME','ML','TABLEAU'])
if choose =='HOME':
    new_title = '<p style="font-family:sans-serif; color:#ADD8E6; font-size: 41px;">WELCOME TO TRADERS CENTRAL</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    image = Image.open('imagest.PNG')
    st.image(image)
elif choose == 'ML':
    # set_page_config needs to be the first Streamlit command in your script
    st.title("FOREX Forecasting Models Monitoring")
    add_selectbox = st.selectbox(
    "Choose your Currency Pair",
    ('INR-USD','EURO-USD','USD-CAD')
    )
    new_title1 = '<p style="font-family:sans-serif; color:#FFFFFF; font-size: 25px;"><b>The prediction for the next 5 days:</b></p>'
    st.markdown(new_title1, unsafe_allow_html=True)
    #st.write('The prediction for the next 5 days:')
    if add_selectbox=='INR-USD':

        # Initialize connection.
        # Uses st.experimental_singleton to only run once.
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


        #actual=run_query("select ACTUAL from ACTVSPREC limit 5;")
        prediction=run_query("select PREDICTIONS from ACTVSPREC limit 5;")
        date=run_query("select DDATE from ACTVSPREC limit 5 ;")


        # Create DataFrame from multiple lists


        df2=pd.DataFrame(list(zip(date,prediction)),columns=['date','prediction'])
        st.write(df2)

        #chart_data = pd.DataFrame(
         #   np.random.randn(20, 3),
         #   columns=['a', 'b', 'c'])

       

        # passing in the Plotly graph object to Streamlit
        #st.plotly_chart(line_fig, use_container_width=True)


        df5 = pd.DataFrame({
          'date': ['12/23/2022','12/26/2022','12/27/2022','12/28/2022','12/29/2022','12/30/2022', '01/2/2023', '01/3/2023','01/4/2023','01/5/2023'],
           'Actual': [  82.79, 82.55, 82.73, 82.74,82.83,82.75,82.73,82.71,82.51,82.81],
                'Prediction':[ 82.78, 82.65, 82.83, 82.736,82.758,82.717,82.745,82.774,82.641,82.765]
            })






            # Print results.


        st.line_chart(df5, x="date",
           y=["Actual", "Prediction"])

    elif add_selectbox=='EURO-USD':
    # Initialize connection.
        # Uses st.experimental_singleton to only run once.
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


        #actual=run_query("select ACTUAL from ACTVSPREC limit 5;")
        prediction=run_query("select PREDICTION from ACTVSPRECEURO limit 5;")
        date=run_query("select DDATE from ACTVSPRECEURO limit 5 ;")


        # Create DataFrame from multiple lists


        df3=pd.DataFrame(list(zip(date,prediction)),columns=['date','prediction'])
        st.write(df3)

        #chart_data = pd.DataFrame(
         #   np.random.randn(20, 3),
         #   columns=['a', 'b', 'c'])

        

        # passing in the Plotly graph object to Streamlit
        #st.plotly_chart(line_fig, use_container_width=True)


        df6 = pd.DataFrame({
          'date': ['12/23/2022','12/26/2022','12/27/2022','12/28/2022','12/29/2022','12/30/2022', '01/2/2023', '01/3/2023','01/4/2023','01/5/2023'],
           'Actual': [ 1.0714, 1.1035, 1.0728, 1.1008,1.0761,1.0802,1.0702,1.0436,1.0609,1.1203],
                'Prediction':[ 1.0614, 1.0635, 1.0638, 1.0608,1.0661,1.0702,1.0662,1.0546,1.0599,1.0603]
            })






            # Print results.


        st.line_chart(df6, x="date",
           y=["Actual", "Prediction"])
    else:
         # Initialize connection.
        # Uses st.experimental_singleton to only run once.
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


        #actual=run_query("select ACTUAL from ACTVSPREC limit 5;")
        prediction=run_query("select PREDICTION from ACTVSPRECAD limit 5;")
        date=run_query("select DDATE from ACTVSPRECAD limit 5 ;")


        # Create DataFrame from multiple lists


        df4=pd.DataFrame(list(zip(date,prediction)),columns=['date','prediction'])
        st.write(df4)

        #chart_data = pd.DataFrame(
         #   np.random.randn(20, 3),
         #   columns=['a', 'b', 'c'])

        

        # passing in the Plotly graph object to Streamlit
        #st.plotly_chart(line_fig, use_container_width=True)


        df7 = pd.DataFrame({
          'date': ['12/23/2022','12/26/2022','12/27/2022','12/28/2022','12/29/2022','12/30/2022', '01/2/2023', '01/3/2023','01/4/2023','01/5/2023'],
           'Actual': [ 1.3603, 1.3571, 1.3631, 1.3591,1.2946,1.3000,1.4072,1.3700,1.3482,1.3601],
                'Prediction':[ 1.3598, 1.3583, 1.3522, 1.3608,1.3546,1.3549,1.3572,1.3669,1.3476,1.3503]
            })






            # Print results.


        st.line_chart(df7, x="date",
           y=["Actual", "Prediction"])
elif choose == 'TABLEAU':
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
        if st.session_state["username"] == 'Craig':
            server_url = 'https://prod-apnortheast-a.online.tableau.com/'
            user = 'panga.r.karthik@kipi.bi'
            password = 'Kipithon@123'
            site = 'Site22'
            tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
            server = TSC.Server(server_url, use_server_version=True)

            # Get various data.
            # Explore the tableauserverclient library for more options.
            # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
            @st.experimental_memo(ttl=1200)
            def run_query(view_name):
                with server.auth.sign_in(tableau_auth):
                    workbooks, pagination_item = server.workbooks.get()
                    for w in workbooks:
                        if w.name == 'myworkbook4':
                            our_workbook = w
                            break
            # Get views for BHARAT_REFINERY_DASHBOARD_FINAL workbook.
                    server.workbooks.populate_views(our_workbook)
                    for v in our_workbook.views:
                        if view_name == v.name:
                            our_view = v
                            break

                #Get an image for the view.
                    server.views.populate_image(our_view)
                    view_image = our_view.image
                    return view_image
            view_image = run_query('CDH')
            st.image(view_image, width=800)
        elif st.session_state["username"] == 'Jhony':
            server_url = 'https://prod-apnortheast-a.online.tableau.com/'
            user = 'panga.r.karthik@kipi.bi'
            password = 'Kipithon@123'
            site = 'Site22'
            tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
            server = TSC.Server(server_url, use_server_version=True)

            # Get various data.
            # Explore the tableauserverclient library for more options.
            # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
            @st.experimental_memo(ttl=1200)
            def run_query(view_name):
                with server.auth.sign_in(tableau_auth):
                    workbooks, pagination_item = server.workbooks.get()
                    for w in workbooks:
                        if w.name == 'myworkbook4':
                            our_workbook = w
                            break
            # Get views for BHARAT_REFINERY_DASHBOARD_FINAL workbook.
                    server.workbooks.populate_views(our_workbook)
                    for v in our_workbook.views:
                        if view_name == v.name:
                            our_view = v
                            break

                #Get an image for the view.
                    server.views.populate_image(our_view)
                    view_image = our_view.image
                    return view_image
            view_image = run_query('JDH')
            st.image(view_image, width=800)
        else:
            st.print("Bye!")
