import streamlit as st
from components.ui import render_metric_card
import config

def render(domains_data):
    st.title(f"{config.APP_ICON} Welcome to {config.APP_NAME}")
    st.markdown("""
        <p style='font-size: 1.25rem; color: var(--muted); line-height: 1.6; max-width: 800px;'>
        The ultimate intelligence platform for accelerating your engineering career. 
        Navigate complex industry landscapes, leverage deep technical roadmaps, and engineer your future with precision.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Animated Stats Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        render_metric_card("Engineering Domains", str(len(domains_data)) if domains_data else "12+", "Comprehensive Pathways", "🚀")
    with col2:
        render_metric_card("Dynamic Roadmaps", "Tiered", "Foundational to Advanced", "🗺️")
    with col3:
        render_metric_card("Market Analytics", "Real-time", "Salary & Industry Trends", "📈")
        
    st.markdown("---")
    
    st.subheader("Platform Capabilities")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class='glass-card'>
            <h4 style='margin-bottom: 0.5rem;'>🔍 Deep Domain Intelligence</h4>
            <p style='color: var(--muted); font-size: 0.95rem; line-height: 1.5;'>Immerse yourself in specialized engineering fields. Uncover critical skill requirements, state-of-the-art technology stacks, and interactive node-based learning trajectories.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='glass-card'>
            <h4 style='margin-bottom: 0.5rem;'>⚖️ Strategic Architecture Comparison</h4>
            <p style='color: var(--muted); font-size: 0.95rem; line-height: 1.5;'>Evaluating Computer Science vs AI? Or Mechanical vs Aerospace? Utilize our advanced comparison matrix to benchmark salary vectors, market demand, and skill intersections.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='glass-card'>
            <h4 style='margin-bottom: 0.5rem;'>🤖 AI-Driven Career Synthesis</h4>
            <p style='color: var(--muted); font-size: 0.95rem; line-height: 1.5;'>Uncertain of your optimal trajectory? Engage with our intelligent diagnostic engine to algorithmically map your inherent interests to the perfect engineering discipline.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='glass-card'>
            <h4 style='margin-bottom: 0.5rem;'>🎯 Precision Skill-Gap Analysis</h4>
            <p style='color: var(--muted); font-size: 0.95rem; line-height: 1.5;'>Input your existing technical baseline and target objective. Our analytics engine will compute the exact delta and generate a prioritized execution plan.</p>
        </div>
        """, unsafe_allow_html=True)
