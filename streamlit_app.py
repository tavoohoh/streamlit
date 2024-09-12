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
        "description": "Poco uso",
        "image": "https://images.unsplash.com/photo-1721332154161-847851ea188b?q=80&w=3135&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Set de raquetas (Artengo Tr110)",
        "price": 160000,
        "description": "Menos de un año de uso. Incluye bolso y pelotas",
        "image": "https://images.unsplash.com/photo-1724093121148-ec407f45e44c?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Bolso raqueta (Artengo 100M negro)",
        "price": 65000,
        "description": "Poco uso",
        "image": "https://testimage-ima.com"
    },
    {
        "name": "2 Raquetas de squash (Opfeel Sr100)",
        "price": 80000,
        "description": "Menos de un año de uso",
        "image": "https://testimage-ima.com"
    },
    {
        "name": "Chaqueta Berska",
        "price": 250000,
        "description": "Nueva. Comprada hace 2 años",
        "image": "https://testimage-ima.com"
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