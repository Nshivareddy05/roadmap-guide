import streamlit as st
from components.charts import plot_domain_comparison
from components.ui import render_skill_tags

def render(domains_data):
    st.title("⚖️ Compare Domains")
    st.markdown("<p style='color: var(--muted);'>Select two engineering domains to compare their required skills, salaries, and career characteristics side-by-side.</p>", unsafe_allow_html=True)
    
    if not domains_data:
        st.error("Domain data not loaded.")
        return
        
    domain_list = list(domains_data.keys())
    
    col1, col2 = st.columns(2)
    with col1:
        domain1 = st.selectbox("Domain 1", domain_list, index=0)
    with col2:
        domain2 = st.selectbox("Domain 2", domain_list, index=1 if len(domain_list) > 1 else 0)
        
    if domain1 == domain2:
        st.warning("Please select two different domains to compare.")
        return
        
    st.markdown("---")
    
    data1 = domains_data[domain1]
    data2 = domains_data[domain2]
    
    # Radar Chart
    st.subheader("Domain Characteristics Comparison")
    st.plotly_chart(plot_domain_comparison(domain1, data1, domain2, data2), use_container_width=True)
    
    st.markdown("---")
    
    # Side-by-side text comparison
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown(f"### {domain1}")
        st.markdown(f"**Starting Salary:** {data1.get('salary_trends', {}).get('Entry', 'N/A')}")
        st.markdown(f"**Senior Salary:** {data1.get('salary_trends', {}).get('Senior', 'N/A')}")
        st.markdown("**Core Skills:**")
        render_skill_tags(data1.get('skills', [])[:4])
        st.markdown("**Key Technologies:**")
        render_skill_tags(data1.get('technologies', [])[:4])
        
    with col_b:
        st.markdown(f"### {domain2}")
        st.markdown(f"**Starting Salary:** {data2.get('salary_trends', {}).get('Entry', 'N/A')}")
        st.markdown(f"**Senior Salary:** {data2.get('salary_trends', {}).get('Senior', 'N/A')}")
        st.markdown("**Core Skills:**")
        render_skill_tags(data2.get('skills', [])[:4])
        st.markdown("**Key Technologies:**")
        render_skill_tags(data2.get('technologies', [])[:4])
