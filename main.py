# Core Pkgs
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


import utils as utl
from views import ebay, ebayvendido, options, configuration, inicio


st.set_page_config(layout="wide", page_title='Web Automation with Streamlit and Selenium')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "inicio":
        inicio.load_view()
    elif route == "ebay":
        ebay.load_view()
    elif route == "ebayvendido":
        ebayvendido.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        inicio.load_view()


navigation()