from streamlit_agraph import agraph, Node, Edge, Config
import config
import streamlit as st
import utils.state_manager as state_manager

def render_roadmap_graph(domain_name, roadmaps_data):
    if domain_name not in roadmaps_data:
        st.warning("Detailed roadmap graph currently unavailable for this domain.")
        return None
        
    data = roadmaps_data[domain_name]
    node_data = data.get("nodes", [])
    edge_data = data.get("edges", [])
    
    nodes = []
    edges = []
    
    # Custom colors based on completion status
    for n in node_data:
        is_done = state_manager.is_completed(domain_name, n["id"])
        
        color = "#10b981" if is_done else config.THEME_COLORS["card_bg"]
        border_color = "#059669" if is_done else config.THEME_COLORS["primary"]
        
        nodes.append(Node(
            id=n["id"],
            label=n["label"],
            size=25,
            shape="box",
            color={"background": color, "border": border_color},
            font={"color": config.THEME_COLORS["text"], "size": 16, "face": "Inter"}
        ))
        
    for e in edge_data:
        edges.append(Edge(
            source=e["source"],
            target=e["target"],
            color=config.THEME_COLORS["secondary"],
            arrows={"to": {"enabled": True, "scaleFactor": 0.5}}
        ))
        
    cfg = Config(
        width="100%",
        height=600,
        directed=True,
        physics=True,
        hierarchical=True,
        nodeHighlightBehavior=True,
        highlightColor="#00f2fe",
        collapsible=True,
        backgroundColor="transparent",
        interaction={"hover": True, "navigationButtons": True, "keyboard": True}
    )
    
    st.markdown("""
    <style>
    .roadmap-container {
        border-radius: 16px;
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(0, 242, 254, 0.2);
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.1);
        overflow: hidden;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .roadmap-container:hover {
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
        border-color: rgba(0, 242, 254, 0.5);
    }
    </style>
    <div class="roadmap-container">
    """, unsafe_allow_html=True)
    
    # Returns the ID of the clicked node
    clicked_node = agraph(nodes=nodes, edges=edges, config=cfg)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    return clicked_node
