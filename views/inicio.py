from pathlib import Path
from random import randrange

import streamlit as st
import pandas as pd
from PIL import Image


def load_view():

	# Título de la página y diseño
	st.markdown('##')
	st.markdown("<h1 style='text-align: center; color: #d4d4d4;'> Selenium Bot </h1>", unsafe_allow_html=True)
	st.markdown("<h2 style='text-align: center; color: grey'>Transforme su aplicación Streamlit en un asistente web dinámico</h2>", unsafe_allow_html=True)
	st.markdown('##')


	# Imagen de la página
	col1, col2, col3 = st.columns([6, 6, 6])
	with col2:
		st.image("assets/images/selenium.jpg")
	with col1:
		st.write(' ')
	with col3:
		st.write(' ')

	st.markdown("<h2 style='text-align: center; color: grey'> Puedes convertir tu aplicación en un asistente de automatización web que realiza tareas e interactúa con la web como nunca antes. </h2>", unsafe_allow_html=True)


