import streamlit as st

def init_session_state():
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = []
    if 'completed_nodes' not in st.session_state:
        st.session_state.completed_nodes = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hi! I'm your Engineering Roadmap AI. How can I help you today?"}
        ]

def toggle_bookmark(domain, node_id):
    item = f"{domain}::{node_id}"
    if item in st.session_state.bookmarks:
        st.session_state.bookmarks.remove(item)
        return False
    else:
        st.session_state.bookmarks.append(item)
        return True

def toggle_completion(domain, node_id):
    item = f"{domain}::{node_id}"
    if item in st.session_state.completed_nodes:
        st.session_state.completed_nodes.remove(item)
        return False
    else:
        st.session_state.completed_nodes.append(item)
        return True

def is_bookmarked(domain, node_id):
    return f"{domain}::{node_id}" in st.session_state.bookmarks

def is_completed(domain, node_id):
    return f"{domain}::{node_id}" in st.session_state.completed_nodes

def get_progress(domain, total_nodes):
    if total_nodes == 0:
        return 0
    completed = sum(1 for item in st.session_state.completed_nodes if item.startswith(f"{domain}::"))
    return int((completed / total_nodes) * 100)
