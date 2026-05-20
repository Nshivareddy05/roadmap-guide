import streamlit as st

def render(domains_data):
    st.title("📅 Daily Learning Planner")
    st.markdown("<p style='color: var(--muted);'>Generate a structured weekly study plan based on your chosen domain.</p>", unsafe_allow_html=True)
    
    if not domains_data:
        st.error("Data unavailable.")
        return
        
    target_domain = st.selectbox("Select Domain to study:", list(domains_data.keys()))
    hours_per_day = st.slider("How many hours can you study per day?", 1, 8, 2)
    
    if st.button("Generate Plan"):
        st.markdown("---")
        st.subheader(f"Your {hours_per_day} hr/day Study Plan for {target_domain}")
        
        skills = domains_data[target_domain].get("skills", ["Core Concepts"])
        tech = domains_data[target_domain].get("technologies", ["Tools"])
        
        # Simple cyclic distribution
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for i, day in enumerate(days):
            st.markdown(f"#### {day}")
            with st.container():
                st.markdown(f"""
                <div class='glass-card' style='padding: 15px; margin-bottom: 10px;'>
                    <b>Focus:</b> {skills[i % len(skills)] if i % 2 == 0 else tech[i % len(tech)]} <br>
                    <b>Task:</b> Study theory for {hours_per_day/2:.1f} hrs, Practice/Code for {hours_per_day/2:.1f} hrs. <br>
                </div>
                """, unsafe_allow_html=True)
