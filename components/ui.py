import streamlit as st
import config

def render_metric_card(title, value, subtitle="", icon=""):
    import re
    
    # Extract numbers for animation
    numeric_match = re.search(r'\d+', str(value))
    if numeric_match and len(str(value)) < 15:
        target = numeric_match.group()
        parts = str(value).split(target)
        prefix = parts[0]
        suffix = parts[1] if len(parts) > 1 else ""
        display_html = f'{prefix}<span class="animate-number" data-target="{target}">0</span>{suffix}'
    else:
        display_html = str(value)
        
    st.markdown(f"""
        <div class="glass-card metric-card" style="text-align: center; position: relative; overflow: hidden; border-top: 2px solid rgba(0, 242, 254, 0.1);">
            <div style="font-size: 2.2rem; margin-bottom: 12px; filter: drop-shadow(0 0 8px rgba(0,242,254,0.4));">{icon}</div>
            <h3 style="margin:0; font-size: 0.95rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px;">{title}</h3>
            <h2 style="margin:12px 0; font-size: 2.5rem; color: var(--primary); font-weight: 800; text-shadow: 0 0 20px rgba(0,242,254,0.3);">
                {display_html}
            </h2>
            <p style="margin:0; font-size: 0.85rem; color: var(--muted); opacity: 0.8; letter-spacing: 0.5px;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

def render_skill_tags(skills):
    tags_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
    st.markdown(f"<div>{tags_html}</div><br>", unsafe_allow_html=True)

def render_resource_link(title, url, type_icon="🔗"):
    st.markdown(f"""
        <a href="{url}" target="_blank" class="resource-link">
            <span style="font-size: 1.5rem; margin-right: 15px;">{type_icon}</span>
            <div style="flex-grow: 1;">
                <h4 style="margin:0; font-size: 1.1rem;">{title}</h4>
                <p style="margin:0; font-size: 0.8rem; color: var(--muted);">Click to open resource</p>
            </div>
            <span style="color: var(--primary);">→</span>
        </a>
    """, unsafe_allow_html=True)
