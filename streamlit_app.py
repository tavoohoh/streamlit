import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Gustavo Santamaría | Venta de garage",
    page_icon="https://tavoohoh.com/favicon.ico",
    layout="centered"
)

products = [
    {
        "name": "IK Multimedia iRig Keys 2",
        "price": 520000,
        "description": "Poco uso, en su caja con sus accesorios.",
        "image": "assets/images/irig-keys.jpg"
    },
    {
        "name": "Set de raquetas (Artengo Tr110)",
        "price": 160000,
        "description": "Menos de un año de uso. Incluye bolso y pelotas",
        "image": "assets/images/kit-raquetas.png"
    },
    {
        "name": "Bolso raqueta (Artengo 100M negro)",
        "price": 65000,
        "description": "Poco uso",
        "image": "assets/images/bolso-raquetas.png"
    },
    {
        "name": "2 Raquetas de squash (Opfeel Sr100)",
        "price": 80000,
        "description": "Menos de un año de uso",
        "image": "assets/images/raqueta-squash.png"
    },
    {
        "name": "Bershka Between-season jacket in Dark Purple",
        "price": 250000,
        "description": "Nueva. Comprada hace 2 años",
        "image": "assets/images/chaqueta.png"
    },
    {
        "name": "Dungeons & Dragons, Castle Ravenloft - Board Game",
        "price": 150000,
        "description": "Juego de mesa de Dungeons & Dragons usado",
        "description": "Juego de mesa de Dungeons & Dragons usado",
        "image": "assets/images/dnd.jpg"
    },
    {
        "name": "The Point of no Return - Walltones by Ecstase",
        "price": 120000,
        "description": "Nunca usado, el empaque esta en perfecto estado aunque abierto. Medidas 70x93.5cm, referencia E402L",
        "image": "assets/images/cuadro.png"
    }
]

st.logo(
    "https://tavoohoh.com/favicon.ico",
    icon_image="https://tavoohoh.com/favicon.ico",
)

st.title("Venta de Garaje")
st.markdown('<p style="font-size:18px;">Me mudé hace menos de un año y me di cuenta de que tengo muchas cosas que ya no necesito. Seguro que alguien más podría aprovecharlas mejor. Si estás interesado, escríbeme.</p>', unsafe_allow_html=True)

whatsapp_link = "https://wa.me/573002383905"
whatsapp_style = "border: 1px solid #fff; color: white; padding: 4px 12px; border-radius: 12px; cursor: pointer; text-decoration: none; margin-top: 1.2rem; width: max-content; display: block;"

st.divider()

for product in products:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(product["image"], use_column_width=True)

    with col2:
        formatted_price = "${:,.0f} COP".format(product['price'])
        message = f"Hola, quisiera comprar {product['name']}"
        encoded_message = urllib.parse.quote(message)

        st.subheader(product["name"])

        description = f'<p style="margin: 0;">{product["description"]}</p>'
        price = f'<p><b>Precio:</b> {formatted_price}</p>'
        btn = f'<a style="{whatsapp_style}" target="_blank" href="{whatsapp_link}?text={encoded_message}" target="_blank">Comprar</a>'

        st.html(f'{description}{price}{btn}')

    st.divider()