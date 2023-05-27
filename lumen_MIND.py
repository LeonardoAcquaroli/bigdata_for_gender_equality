import streamlit as st
import pandas as pd
import random as rdm

def random_gpg(mean: float, std: float):
    gpg = rdm.gauss(mean,std)
    return round(gpg,2)

def cite():
    # Add a button to your Streamlit app
    if st.button('Click me!'):
        # When the button is clicked, execute the JavaScript code
        st.markdown(
            """
            <script>
            function showAlert() {
                alert('Progetto HOLOS: Gender equality @MIND (2023), Fondazione Triulza');
            }
            </script>
            """
            , unsafe_allow_html=True)
        
        # Call the JavaScript function to display the alert
        st.markdown('<script>showAlert();</script>', unsafe_allow_html=True)

# Immagine di intestazione presa da un URL di GitHub
# header_image_url = 'https://raw.githubusercontent.com/NOME_UTENTE/NOME_REPOSITORY/master/immagine.jpg'
header_image_url = "https://www.mindmilano.it/wp-content/uploads/2022/04/mind_logo_light_blue.svg"

# Dati per la tabella "Dati aggregati"
aziende = ['A2A','ABB','Accenture','AstraZeneca','Bio4dreams','Bracco','Cereal Docks','Cisco','Daikin','Enel X','E.ON Italia','Elettronica','Esselunga','Fabrick','Forte Secur Group','Illumina','Lendlease','Life Sciences District','Maire Tecnimont','Mapei','Nippon Gases','Novartis','Podium','Poste Italiane','Promocoop Lombardia','Rold','Samsung SDS','Schneider Electric','Sicuritalia','Stevanato Group','Stora Enso','TIM','VSBLTY','Valore Italia','WINDTRE','Wood Beton']
dati_aggregati = {
    'Azienda': aziende,
    'Proporzione donne nei ruoli apicali (%)': [random_gpg(mean=25,std=10) for _ in range(len(aziende))],
    'Gender Pay Gap (%)': [random_gpg(mean=10,std=3) for _ in range(len(aziende))]
}
df_dati_aggregati = pd.DataFrame(dati_aggregati)

# Dati per la tabella "Singola azienda"
posizioni = ['Top executives', 'Dirigenti', 'Quadri', 'Impiegati']
dati_singola_azienda = {
    'Posizione lavorativa': posizioni,
    'Percentuale donne (%)': [random_gpg(mean=45,std=10) for _ in range(len(posizioni))],
    'Gender Pay Gap (%)': [random_gpg(mean=10,std=3) for _ in range(len(posizioni))]
}
df_dati_singola_azienda = pd.DataFrame(dati_singola_azienda)

# Configurazione della pagina
st.set_page_config(page_title='Web App con Streamlit', page_icon=':computer:')

# Intestazione con immagine da URL di GitHub
st.image(header_image_url, use_column_width=False)

# Menù di selezione laterale
scelta_pagina = st.sidebar.radio('Seleziona una pagina', ('Dati aggregati', 'Dettaglio azienda'))

# Pagina "Dati aggregati"
if scelta_pagina == 'Dati aggregati':
    st.header('Dati Aggregati')
    st.dataframe(df_dati_aggregati)

# Pagina "Singola azienda"
elif scelta_pagina == 'Dettaglio azienda':
    st.header('Dettaglio azienda')

    # Selettore dell'azienda
    azienda_selezionata = st.selectbox('Seleziona un\'azienda', aziende)

    # Filtraggio dei dati per l'azienda selezionata
    df_azienda_selezionata = df_dati_singola_azienda.copy()

    # Mostra la tabella per l'azienda selezionata
    st.dataframe(df_azienda_selezionata)

st.text("Dati generati casualmente")
cite()
