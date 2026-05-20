import streamlit as st
import utils.state_manager as state_manager
import config

def render(domains_data, roadmaps_data):
    st.title("📊 Progress Dashboard")
    st.markdown("<p style='color: var(--muted);'>Track your learning journey and access your bookmarked resources.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Progress")
        has_progress = False
        for domain, r_data in roadmaps_data.items():
            total_nodes = len(r_data.get("nodes", []))
            progress = state_manager.get_progress(domain, total_nodes)
            
            if progress > 0:
                has_progress = True
                st.markdown(f"**{domain}**")
                st.progress(progress / 100)
                st.markdown(f"<p style='text-align: right; color: var(--primary); font-size: 0.8rem;'>{progress}% Completed</p>", unsafe_allow_html=True)
                
        if not has_progress:
            st.info("No progress tracked yet. Go to the Domain Explorer to start checking off nodes!")
            
    with col2:
        st.subheader("🔖 Your Bookmarks")
        if not st.session_state.bookmarks:
            st.info("You haven't bookmarked any roadmap nodes yet.")
        else:
            for bm in st.session_state.bookmarks:
                domain, node_id = bm.split("::")
                st.markdown(f"""
                <div class='glass-card' style='padding: 10px; margin-bottom: 10px;'>
                    <b>Domain:</b> {domain} <br>
                    <b>Skill:</b> {node_id}
                </div>
                """, unsafe_allow_html=True)
                
    st.markdown("---")
    st.subheader("Personalized Learning Plan")
    st.markdown("<p style='color: var(--muted);'>Based on your bookmarks and progress, here is what you should focus on next:</p>", unsafe_allow_html=True)
    
    if st.session_state.bookmarks:
        st.markdown(f"- Master the topics related to your bookmarked skill: **{st.session_state.bookmarks[0].split('::')[1]}**")
    else:
        st.markdown("- Explore the **Beginner** nodes in your preferred domain.")
