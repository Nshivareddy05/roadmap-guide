import streamlit as st
from components.ui import render_skill_tags, render_resource_link
from components.visualizer import render_roadmap_graph
from components.charts import plot_salary_trends
import utils.state_manager as state_manager
import config

def render(domains_data, roadmaps_data):
    st.title("🔍 Domain Explorer")
    
    # Smart filtering
    search_query = st.text_input("Search for a domain, skill, or keyword...").lower()
    
    domain_names = list(domains_data.keys()) if domains_data else config.DOMAINS
    
    if search_query:
        filtered_domains = []
        for name, data in domains_data.items():
            if search_query in name.lower() or search_query in data.get('overview', '').lower():
                filtered_domains.append(name)
            else:
                for skill in data.get('skills', []) + data.get('technologies', []):
                    if search_query in skill.lower():
                        filtered_domains.append(name)
                        break
        domain_names = filtered_domains if filtered_domains else domain_names
        if not filtered_domains:
            st.warning("No matches found. Showing all domains.")
    
    selected_domain = st.selectbox("Select an Engineering Domain to explore:", domain_names)
    
    if not domains_data or selected_domain not in domains_data:
        st.warning("Detailed data for this domain is currently being updated.")
        return
        
    data = domains_data[selected_domain]
    
    st.markdown(f"### About {selected_domain}")
    st.markdown(f"<p style='color: var(--muted); font-size: 1.1rem;'>{data.get('overview', '')}</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Interactive Roadmap", "🛠️ Skills & Tech", "💼 Career & Salary", "📚 Resources"])
    
    with tab1:
        st.subheader(f"Learning Roadmap for {selected_domain}")
        st.markdown("<p style='color: var(--muted);'>Click on any node to view details, mark as complete, or bookmark.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            clicked_node = render_roadmap_graph(selected_domain, roadmaps_data)
            
        with col2:
            st.markdown("### Node Details")
            if clicked_node:
                st.markdown(f"**Selected Node:** `{clicked_node}`")
                
                # Fetch detailed info if available in roadmaps_data (we need to add this)
                nodes = roadmaps_data.get(selected_domain, {}).get("nodes", [])
                node_info = next((n for n in nodes if n["id"] == clicked_node), None)
                
                if node_info:
                    st.markdown(f"**Level:** {node_info.get('group', 'Beginner').title()}")
                    st.markdown(f"**Description:** Essential topics related to {node_info.get('label', clicked_node)}.")
                    
                    st.markdown("---")
                    
                    is_bookmarked = state_manager.is_bookmarked(selected_domain, clicked_node)
                    if st.button("🔖 Remove Bookmark" if is_bookmarked else "🔖 Add Bookmark", key=f"bm_{clicked_node}"):
                        state_manager.toggle_bookmark(selected_domain, clicked_node)
                        st.rerun()
                        
                    is_completed = state_manager.is_completed(selected_domain, clicked_node)
                    if st.button("✅ Mark Incomplete" if is_completed else "✅ Mark Complete", key=f"mc_{clicked_node}"):
                        state_manager.toggle_completion(selected_domain, clicked_node)
                        st.rerun()
            else:
                st.info("👈 Click on a node in the graph to see its details and track your progress.")
                
    with tab2:
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.subheader("Core Skills")
            render_skill_tags(data.get("skills", []))
        with col_s2:
            st.subheader("Technologies & Tools")
            render_skill_tags(data.get("technologies", []))
            
        st.subheader("Real-world Projects")
        for proj in data.get("projects", []):
            st.markdown(f"- **{proj}**")
            
    with tab3:
        col_c1, col_c2 = st.columns([1, 1])
        with col_c1:
            st.subheader("Career Opportunities")
            for role in data.get("career_opportunities", []):
                st.markdown(f"- {role}")
            st.markdown(f"**Future Scope:** {data.get('future_scope', '')}")
        with col_c2:
            st.plotly_chart(plot_salary_trends(data.get("salary_trends", {})), use_container_width=True)
            
    with tab4:
        st.subheader("Recommended Learning Resources")
        for res in data.get("resources", []):
            res_type = res.get("type", "").lower()
            if "youtube" in res_type:
                icon = "▶️"
            elif "github" in res_type:
                icon = "🐙"
            elif "doc" in res_type:
                icon = "📄"
            elif "cert" in res_type:
                icon = "📜"
            elif "intern" in res_type or "placement" in res_type or "career" in res_type:
                icon = "💼"
            elif "gate" in res_type:
                icon = "🎓"
            elif "course" in res_type:
                icon = "🏫"
            elif "tool" in res_type:
                icon = "🛠️"
            else:
                icon = "🔗"
            render_resource_link(res.get("title", ""), res.get("url", "#"), icon)
