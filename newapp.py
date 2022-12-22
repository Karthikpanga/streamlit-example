import streamlit as st
import tableauserverclient as TSC
# Establish the connection

st.markdown ("#### Dashboard Il")
server_url = 'https://prod-useast-a.online.tableau.com'
user = 'amulya.s.nidhi@kipi.bi'
password = 'Kipithon@123'
site = 'Site21'

tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
server = TSC.Server(server_url, use_server_version=True)

# Fetch the dashboards/charts
@st.experimental_memo(ttl=1200)
def run_query():
  with server.auth.sign_in(tableau_auth):
    workbooks, pagination_item = server.workbooks.get()
    for w in workbooks:
      if w.name == 'trydashboard':
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
st.image(view_image, width=800)
      
