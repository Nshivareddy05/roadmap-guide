import streamlit as st

def get_icon_for_category(category):
    category = category.lower()
    if "youtube" in category: return "▶️"
    elif "github" in category: return "🐙"
    elif "docs" in category: return "📄"
    elif "course" in category: return "🏫"
    elif "platform" in category: return "💻"
    elif "research" in category: return "🔬"
    elif "roadmap" in category: return "🗺️"
    elif "competitive" in category: return "🏆"
    else: return "🔗"

def render(resources_data):
    st.title("📚 Comprehensive Resource Hub")
    st.markdown("<p style='color: var(--muted); font-size: 1.1rem; line-height: 1.6; max-width: 900px;'>Explore our massive curated library of premium engineering resources. Filter through official documentation, courses, preparation platforms, and more to accelerate your technical journey.</p>", unsafe_allow_html=True)
    st.markdown("---")

    if not resources_data:
        st.warning("Resource data is currently unavailable.")
        return

    # Extract unique values for filters
    all_domains = sorted(list(set([d for r in resources_data for d in r.get("domain", [])])))
    all_categories = sorted(list(set([r.get("category", "General") for r in resources_data])))
    all_levels = ["Beginner", "Intermediate", "Advanced"] # Hardcoded logical ordering
    
    # Filters
    st.markdown("<h4 style='margin-bottom: 1rem;'>🔍 Filter Resources</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        search_q = st.text_input("Search keywords...", "")
    with col2:
        selected_domain = st.selectbox("Filter by Domain", ["All Domains"] + all_domains)
    with col3:
        selected_category = st.selectbox("Filter by Category", ["All Categories"] + all_categories)
    with col4:
        selected_level = st.selectbox("Skill Level", ["All Levels"] + all_levels)

    st.markdown("<br>", unsafe_allow_html=True)

    # Filtering logic
    filtered = []
    for r in resources_data:
        # Search filter
        if search_q and search_q.lower() not in r.get("title", "").lower() and search_q.lower() not in "".join(r.get("career_path", [])).lower():
            continue
        # Domain filter
        if selected_domain != "All Domains" and selected_domain not in r.get("domain", []):
            continue
        # Category filter
        if selected_category != "All Categories" and selected_category != r.get("category", ""):
            continue
        # Level filter
        if selected_level != "All Levels" and selected_level != r.get("level", ""):
            continue
        filtered.append(r)

    # Display Results
    st.subheader(f"Found {len(filtered)} Resources")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not filtered:
        st.info("No resources found matching your current filters. Try broadening your search criteria.")
    else:
        # Display in a grid format
        cols = st.columns(2)
        for idx, res in enumerate(filtered):
            with cols[idx % 2]:
                icon = get_icon_for_category(res.get("category", ""))
                domains_html = "".join([f'<span class="skill-tag" style="font-size: 0.7rem; padding: 2px 8px; margin: 2px 4px 2px 0;">{d}</span>' for d in res.get("domain", [])])
                paths_html = ", ".join(res.get("career_path", []))
                
                st.markdown(f"""
                <div class="glass-card" style="padding: 20px; margin-bottom: 20px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                            <h4 style="margin: 0; font-size: 1.15rem; line-height: 1.3;">
                                <span style="margin-right: 8px;">{icon}</span>{res.get("title")}
                            </h4>
                            <a href="{res.get("url")}" target="_blank" style="background: rgba(0, 242, 254, 0.15); border: 1px solid rgba(0,242,254,0.3); padding: 4px 10px; border-radius: 6px; text-decoration: none; color: var(--primary); font-size: 0.75rem; font-weight: 700; transition: all 0.2s; white-space: nowrap; margin-left: 10px;">Visit ↗</a>
                        </div>
                        <p style="margin: 0 0 10px 0; color: rgba(255,255,255,0.7); font-size: 0.85rem;">
                            <strong>Category:</strong> {res.get("category")} &nbsp;|&nbsp; 
                            <strong>Level:</strong> {res.get("level")}
                        </p>
                        <p style="margin: 0 0 12px 0; color: rgba(255,255,255,0.5); font-size: 0.8rem;">
                            <strong>Target Paths:</strong> {paths_html}
                        </p>
                    </div>
                    <div>
                        {domains_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)
