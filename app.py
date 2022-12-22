import streamlit as st
from pytableau import TableauAuth, Server, Site, Workbook
import pandas as pd
# Set Tableau server URL, username, and password
server_url = "https://prod-useast-a.online.tableau.com"
username = "user@example.com"
password = "password"
# Authenticate with Tableau server
auth = TableauAuth(username, password)
# Connect to Tableau server
server = Server(server_url)
# Get information about the Tableau site
site = Site(server, "Site21")
# Get the desired workbook
workbook = Workbook(server, site, "Workbook Name")
# Get the data from the workbook as a Pandas DataFrame
df = workbook.fetch_data()
# Display the data in a line chart
st.line_chart(df)
