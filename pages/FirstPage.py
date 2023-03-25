import streamlit as st
import pandas as pd
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import requests

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
import os
import tempfile
from pathlib import PurePath

sharepoint_email = "andres.moreno@ingeo-data.com"
sharepoint_password = "*Urapanes09*"
sharepoint_url_site = "https://ingeodata.sharepoint.com/sites/Developersteam"
sharepoint_site_name = "Developersteam"
sharepoint_doc_library = "Documentos compartidos"
folder_name = "General"
file_name = "file_test.csv"

# sharepoint_email = st.secrets["sharepoint_email"]
# sharepoint_password = st.secrets["sharepoint_password"]
# sharepoint_url_site = st.secrets["sharepoint_url_site"]
# sharepoint_site_name = st.secrets["sharepoint_site_name"]
# sharepoint_doc_library = st.secrets["sharepoint_doc_library"]
# folder_name = st.secrets["folder_name"]
# file_name = st.secrets["file_name"]


pc_path = "./pages/Download"
conn = ClientContext(sharepoint_url_site).with_credentials(UserCredential(sharepoint_email, sharepoint_password))
file_url = f"/sites/{sharepoint_site_name}/{sharepoint_doc_library}/{folder_name}/{file_name}"
#download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
#with open(download_path, "wb") as local_file:
#    file = conn.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
    #file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
#print("[Ok] file has been downloaded into: {0}".format(download_path))
#file_content = file.content
#print(file_content)



final_path = PurePath(pc_path, file_name)
file = File.open_binary(conn, file_url)
file_content = file.content
with open(final_path, 'wb') as f:
    f.write(file_content)
print(file.content)
df = pd.read_csv(final_path)
print(df)

# SharePoint credentials option 2



# # SharePoint credentials option 1
# sharepoint_url = "https://ingeodata-my.sharepoint.com" #URL de entrada
# username = "andres.moreno@ingeo-data.com"
# password = "*Urapanes09*"
# sharepoint_url_site = "https://ingeodata.sharepoint.com/sites/Developersteam/"
# authcookie = Office365(sharepoint_url, username=username, password=password).GetCookies()
# site = Site(sharepoint_url_site, version=Version.v365, authcookie=authcookie)

# folder = site.Folder('Documentos compartidos')
# data = folder.get_file = ('file_test')




st.title("Stability Window RT for Client")
st.text('This is a test to show a RT stability Window')
st.markdown('## test in markdown')
st.sidebar.title('Side bar creation')
uploaded_file = st.file_uploader('Ubload a file:')
st.sidebar.button('Run')
text = st.text_input('text here')
st.text(text)
st.header('Raw Data')
#st.write(file)
st.write(df)

# if uploaded_file:
#     st.header('Raw Data')
#     df = pd.read_csv(uploaded_file)
#     st.write(df)
#     st.header('Data stadistics')
#     st.write(df.describe())