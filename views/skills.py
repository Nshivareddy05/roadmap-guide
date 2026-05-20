import streamlit as st
from components.ui import render_skill_tags

def render(domains_data):
    st.title("🎯 Skill Gap Analyzer")
    st.markdown("<p style='color: var(--muted);'>Find out what you need to learn to transition into your dream engineering role.</p>", unsafe_allow_html=True)
    
    if not domains_data:
        st.error("Domain data not available.")
        return
        
    domain_list = list(domains_data.keys())
    
    st.subheader("Your Target Role")
    target_domain = st.selectbox("Which domain do you want to master?", domain_list)
    
    target_skills = set(domains_data[target_domain].get("skills", []))
    target_techs = set(domains_data[target_domain].get("technologies", []))
    all_target = target_skills.union(target_techs)
    
    st.subheader("Your Current Skills")
    
    # Suggest common skills based on all domains
    all_possible_skills = set()
    for d in domains_data.values():
        all_possible_skills.update(d.get("skills", []))
        all_possible_skills.update(d.get("technologies", []))
        
    user_skills = st.multiselect("Select the skills/technologies you already know:", sorted(list(all_possible_skills)))
    
    if st.button("Analyze My Skill Gap"):
        user_skills_set = set(user_skills)
        missing_skills = all_target - user_skills_set
        matched_skills = all_target.intersection(user_skills_set)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ✅ What you know")
            if matched_skills:
                render_skill_tags(list(matched_skills))
            else:
                st.warning("No overlapping skills yet. Time to start learning!")
                
        with col2:
            st.markdown("### 🚀 What you need to learn")
            if missing_skills:
                render_skill_tags(list(missing_skills))
            else:
                st.success("You have all the required skills for this domain!")
                
        if missing_skills:
            st.info("💡 **Tip:** Go to the Domain Explorer to find courses and resources for these missing skills.")
