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
    st.title("Web Scraping artículos de Ebay con Streamlit y Selenium")

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
            lista_precios = []
            lista_urls = []
            lista_envios = []



            for i in range(4):
                # Encuentra elementos
                enviar = driver.find_element(By.XPATH, '//input[@value="Buscar"]')
                enviar.click()
                time.sleep(2)


                # Buscar títulos de elementos
                nombres = driver.find_elements(By.XPATH,
                                               '//ul[@class="srp-results srp-grid clearfix"]/li//div[@class="s-item__title"]')
                nombres = [i.text for i in nombres]
                st.write(nombres)

                # Encuentra el precio del elemento
                precios = driver.find_elements(By.XPATH,
                                               '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__details clearfix"]/div[1]/span')
                precios = [i.text for i in precios]
                st.write(precios)

                # Buscar Información Sobre Envio
                envios = driver.find_elements(By.XPATH,
                                              '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__details clearfix"]/div[3]/span[1]')
                envios = [i.text for i in envios]
                st.write(envios)

                # Buscar URL
                urls = driver.find_elements(By.XPATH,
                                            '//ul[@class="srp-results srp-grid clearfix"]//div[@class="s-item__info clearfix"]//a[@class="s-item__link"]')
                urls = [i.get_attribute("href") for i in urls]

                lista_nombres.extend(nombres)
                lista_precios.extend(precios)
                lista_envios.extend(envios)
                lista_urls.extend(urls)

                df = pd.DataFrame({"Titulo":lista_nombres, "Precios":lista_precios, "Precio De Envios":lista_envios,"Url":lista_urls})
                st.write(df)

                try:
                    siguente = driver.find_element(By.XPATH, '//a[@class="pagination__items"]')
                    siguente.click()
                except:
                    break


        except Exception as e:
            st.write(f"Ocurrió un error: {e}")

        finally:
            driver.quit()

    # Crea un botón Streamlit para activar la automatización
    if st.button("Automatizar las interacciones web"):
        st.write("Automatización de interacciones web. Espere por favor...")
        automate_web_interactions(ebay_url, button_text)
        st.write("Interacciones web completadas.")

    # Mostrar el resultado
    st.write("La aplicación Streamlit está lista para automatizar las interacciones web.")

