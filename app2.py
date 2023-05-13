import streamlit as st
import pickle
from typing import List, Tuple
from streamlit_searchbox import st_searchbox
from crp_model import TrieNode
from crp_model import Trie


st.set_page_config(page_title="VeePee", page_icon=":sparkles:", layout="centered")


# Load your model using pickle
@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


# Load your model here
model_path = 'trie.pkl'
model = load_model(model_path)


@st.cache_data
def get_autocomplete_suggestions(searchterm: str) -> List[Tuple[str, any]]:
    if not searchterm:
        return []
    # Implement your function to return autocomplete suggestions based on the model
    suggestions = model.autocomple(searchterm.lower())[:10]
    return [
        (f"{autocomple}", f"{autocomple}")
        for autocomple in suggestions
    ]


st.markdown("<h1 style='text-align: center; color: pink;'>Bienvenue Chez VeePee</h1>", unsafe_allow_html=True)


with st.container():
    st.write("")  # Empty line for spacing
    left_column, middle_column, right_column = st.columns(3)

    with middle_column:
        selected_value = st_searchbox(
            search_function=get_autocomplete_suggestions,
            placeholder="Recherchez une marque, un produit...",
            default="",
            clear_on_submit=False,
            clearable=True,
            key="autocomplete",
        )
        # st.info(f"{selected_value}")



