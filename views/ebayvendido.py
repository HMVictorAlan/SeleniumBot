import streamlit as st
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import pandas as pd

def load_view():

    # Definir una aplicación Streamlit
    st.title("Ebay Explorer: Liberando el poder de Streamlit y Selenium")

    # Definir widgets Streamlit para la entrada del usuario
    ebay_url = st.text_input("Introducir URL:")
    button_text = st.text_input("Búsqueda:")

    # Definir una función para automatizar las interacciones web.
    def automate_web_interactions(ebay_url, button_text):
        # Inicialice el WebDriver (asegúrese de tenerlo instalado y configurado)
        driver = webdriver.Chrome()

        try:
            driver.get(ebay_url)

            # Espere explícitamente a que se pueda hacer clic en el botón (ajuste el tiempo de espera según sea necesario)
            wait = WebDriverWait(driver, 20)
            # Agregue su lógica para hacer clic en el botón si es necesario
            ar = button_text
            articulo = driver.find_element(By.XPATH, '//input[@placeholder="Buscar artículos"]')
            articulo.send_keys(ar)

            lista_nombres = []
            lista_fechas = []
            lista_precios = []
            lista_urls= []
            lista_envios = []
            lista_vendedores = []

            # Encuentra elementos
            enviar = driver.find_element(By.XPATH, '//input[@value="Buscar"]')
            enviar.click()
            time.sleep(2)

            # Agregue su lógica para hacer clic en el botón de Artículos finalizados, Artículos vendidos
            checkbox = driver.find_element(By.XPATH, '//input[@aria-label="Artículos vendidos"]')
            time.sleep(2)
            checkbox.click()

            for i in range(20):

                # Buscar títulos de elementos
                nombres = driver.find_elements(By.XPATH,
                                               '//ul[@class="srp-results srp-list clearfix"]/li//div[@class="s-item__title"]')
                nombres = [i.text for i in nombres]
                #st.write(nombres)

                # Buscar fecha de elementos
                fecha = driver.find_elements(By.XPATH,
                                                '//ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__caption-section"][1]')
                fecha = [i.text for i in fecha]
                #st.write(fecha)

                # Encuentra el precio del elemento
                precios = driver.find_elements(By.XPATH,
                                               '//ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__details clearfix"]/div[1]/span')
                precios = [i.text for i in precios]
                #st.write(precios)

                # Buscar Información Sobre Envio
                envios = driver.find_elements(By.XPATH,
                                                '//ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__details clearfix"]/div[3]/span[1]')
                envios = [i.text for i in envios]
                #st.write(envios)

                # Buscar Información De Vendedor
                vendedores = driver.find_elements(By.XPATH,
                                             '//ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__details clearfix"]/span[1]')
                vendedores = [i.text for i in vendedores]
                #st.write(vendedores)

                # Buscar URL
                urls = driver.find_elements(By.XPATH,
                                            '//ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__info clearfix"]//a[@class="s-item__link"]')
                urls = [i.get_attribute("href") for i in urls]
                #st.write(urls)

                lista_nombres.extend(nombres)
                lista_precios.extend(precios)
                lista_urls.extend(urls)
                lista_envios.extend(envios)
                lista_vendedores.extend(vendedores)
                lista_fechas.extend(fecha)


                while True:
                    try:
                        siguiente = driver.find_element(By.XPATH, '//input[@aria-label="Ir a la página de búsqueda siguiente"]')
                        siguiente.click()
                        time.sleep(2)
                    except:
                        break

        finally:
            driver.quit()

        df = pd.DataFrame(
            {"Titulo": lista_nombres, "Fecha De Ventas": lista_fechas, "Precios Final De Venta": lista_precios,
             "Url": lista_urls, "Costo De Envio": lista_envios, "Calificacion De Vendedors": lista_vendedores})
        st.write(df)

    # Crea un botón Streamlit para activar la automatización
    if st.button("Automatizar las interacciones web"):
        st.write("Automatización de interacciones web. Espere por favor...")
        automate_web_interactions(ebay_url, button_text)
        st.write("Interacciones web completadas.")

    # Mostrar el resultado
    st.write("La aplicación Streamlit está lista para automatizar las interacciones web.")








