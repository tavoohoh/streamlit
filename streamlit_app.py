import streamlit as st

products = [
    {
        "name": "IK Multimedia iRig Keys 2",
        "price": 520000,
        "description": "Poco uso",
        "image": "https://images.unsplash.com/photo-1721332154161-847851ea188b?q=80&w=3135&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "IK Multimedia iRig Keys 2",
        "price": 585000,
        "description": "Nuevo / 3 teclas vinieron dañadas",
        "image": "https://images.unsplash.com/photo-1724093121148-ec407f45e44c?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
]

st.logo(
    "https://tavoohoh.com/favicon.ico",
    icon_image="https://tavoohoh.com/favicon.ico",
)

st.title("Venta de Garaje")
st.markdown('<p style="font-size:18px;">Me mudé hace menos de un año y me di cuenta de que tengo muchas cosas que ya no necesito. Seguro que alguien más podría aprovecharlas mejor. Si estás interesado, escríbeme.</p>', unsafe_allow_html=True)

whatsapp_link = "https://wa.me/573002220000"
whatsapp_style = "border: 1px solid #fff; color: white; padding: 8px 12px; border-radius: 12px; cursor: pointer; text-decoration: none;"

for product in products:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(product["image"], use_column_width=True)

    with col2:
        st.subheader(product["name"])
        st.text(product['description'])
        
        formatted_price = "${:,.0f} COP".format(product['price'])
        st.write(f"**Precio**: {formatted_price}")
        st.markdown(f'<a style="{whatsapp_style}" href="{whatsapp_link}" target="_blank">Comprar</a>', unsafe_allow_html=True)
    
    st.divider()