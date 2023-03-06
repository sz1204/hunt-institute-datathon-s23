import streamlit as st

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Homepage", page_icon=":books:", layout="wide")

st.image("assets/hunt-institute.jpg", width=100)

st.title("Welcome to the Steminists' Hunt Institute Datathon 2023 dashboard!")
st.markdown("Our project focused on measuring how certain legislation affecting affordable housing and youth mental health impacted student physical health, mental health, and graduation.")
st.markdown('   ')


# Sidebar
st.sidebar.title("Please Filter Here")
# demographic = st.sidebar.radio() # Filter side bars through urban-rural density
#density = st.sidebar.multiselect(
#    "Select the Density:",
#    options=df[""].unique()
#)
# health = st.sidebar.radio() # Filter side bars through type of healthcare - physical or mental




primary_color = "#bf293c"
secondary_color = "#3a3d7f"
text_color = "#37393e"

# Add CSS to customize text colors
st.markdown(f"""
    <style>
        div.css-edivx2.e16fv1kl3 {{
            color: {secondary_color};
        }}
        p {{
            color: {text_color};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {primary_color};
        }}
    </style>
""", unsafe_allow_html=True)