import streamlit as st
from components.ui import render_resource_link

def render(domains_data):
    st.title("🎓 Career & Placement Prep")
    st.markdown("<p style='color: var(--muted);'>Resources for cracking internships, placements, and competitive exams.</p>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Internships & Placements", "GATE Preparation", "Resume & Projects"])
    
    with tab1:
        st.subheader("How to land your first tech internship")
        st.markdown("""
        1. **Build a strong portfolio**: 2-3 solid projects are better than 10 trivial ones.
        2. **Master Data Structures & Algorithms**: The core of clearing technical rounds.
        3. **Open Source Contributions**: Shows you can work in a team and read large codebases.
        4. **Networking**: Referrals have a much higher conversion rate than cold applications.
        """)
        render_resource_link("LeetCode - Interview Prep", "https://leetcode.com/", "💻")
        render_resource_link("Pramp - Mock Interviews", "https://www.pramp.com/", "🗣️")
        
    with tab2:
        st.subheader("GATE (Graduate Aptitude Test in Engineering)")
        st.markdown("GATE is essential for pursuing Masters in premier Indian institutes (IITs/NITs) and securing jobs in PSUs.")
        domain = st.selectbox("Select Domain for GATE details:", list(domains_data.keys()))
        
        st.info("General strategy: Start early, clear fundamentals, solve previous year papers, and take mock test series.")
        render_resource_link("GATE Official Website", "https://gate.iitk.ac.in/", "🏛️")
        render_resource_link("NPTEL Lectures", "https://nptel.ac.in/", "📺")
        
    with tab3:
        st.subheader("Resume Building Tips")
        st.markdown("""
        - Keep it to **One Page**.
        - Use the **XYZ formula** for bullets: "Accomplished [X] as measured by [Y], by doing [Z]."
        - Quantify your impact (e.g., "reduced loading time by 40%").
        - Highlight technologies actually relevant to the job.
        """)
        render_resource_link("Overleaf Resume Templates", "https://www.overleaf.com/gallery/tagged/cv", "📄")
        render_resource_link("GitHub - Open Source Projects", "https://github.com/", "🐙")
