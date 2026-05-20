import json
import streamlit as st
import os

@st.cache_data
def load_domains_data():
    file_path = os.path.join("data", "domains.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

@st.cache_data
def load_roadmaps_data():
    file_path = os.path.join("data", "roadmaps.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

@st.cache_data
def load_resources_data():
    file_path = os.path.join("data", "resources_hub.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []
