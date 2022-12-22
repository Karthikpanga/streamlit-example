import tableauserverclient as TSC

server_url = 'https://prod-useast-a.online.tableau.com'
user = 'amulya.s.nidhi@kipi.bi'
password = 'Kipithon@123'
site = 'Site21'

tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
server = TSC.Server(server_url, use_server_version=True)

with server.auth.sign_in(tableau_auth):
    print('[Logged in successfully to {}]'.format(server_url))
