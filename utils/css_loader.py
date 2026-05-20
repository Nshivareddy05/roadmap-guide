import streamlit as st
import config

def load_css():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;500;700&display=swap');
        
        /* Base styles */
        :root {{
            --primary: {config.THEME_COLORS['primary']};
            --secondary: {config.THEME_COLORS['secondary']};
            --bg: {config.THEME_COLORS['background']};
            --card-bg: {config.THEME_COLORS['card_bg']};
            --text: {config.THEME_COLORS['text']};
            --muted: {config.THEME_COLORS['muted']};
        }}
        
        .stApp {{
            background-color: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            letter-spacing: 0.02em;
        }}
        
        /* Headers */
        h1, h2, h3, h4, h5 {{
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}
        
        /* Metric Cards */
        div[data-testid="metric-container"] {{
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }}
        
        div[data-testid="metric-container"]::before {{
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 50%; height: 100%;
            background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent);
            transform: skewX(-20deg);
            transition: all 0.5s;
        }}
        
        div[data-testid="metric-container"]:hover::before {{
            left: 150%;
        }}
        
        div[data-testid="metric-container"]:hover {{
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 10px 20px rgba(0, 242, 254, 0.2);
            border-color: var(--primary);
        }}
        
        /* Custom UI Elements */
        .glass-card {{
            background: rgba(15, 23, 42, 0.4);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 28px;
            margin-bottom: 24px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.3);
        }}
        .glass-card:hover {{
            border-color: rgba(0, 242, 254, 0.3);
            box-shadow: 0 15px 40px -5px rgba(0, 242, 254, 0.15);
            transform: translateY(-4px);
        }}
        
        /* Skill tags */
        .skill-tag {{
            display: inline-block;
            padding: 6px 16px;
            margin: 5px;
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 8px;
            font-size: 0.85em;
            font-weight: 500;
            letter-spacing: 0.5px;
            color: var(--text);
            transition: all 0.3s ease;
            cursor: default;
        }}
        .skill-tag:hover {{
            background: rgba(0, 242, 254, 0.1);
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 242, 254, 0.15);
        }}
        
        /* Resource Links */
        .resource-link {{
            display: flex;
            align-items: center;
            padding: 14px 20px;
            background: rgba(15, 23, 42, 0.5);
            border-radius: 12px;
            margin-bottom: 12px;
            text-decoration: none !important;
            color: var(--text) !important;
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.3s ease;
        }}
        .resource-link:hover {{
            background: rgba(30, 41, 59, 0.8);
            border-color: var(--primary);
            transform: translateX(6px);
            box-shadow: -4px 0 15px rgba(0, 242, 254, 0.1);
        }}
        
        /* Hide default Streamlit elements */
        header {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* Buttons */
        div.stButton > button:first-child {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--bg);
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px -3px rgba(0, 242, 254, 0.3);
        }}
        
        div.stButton > button:first-child:hover {{
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 8px 25px -5px rgba(0, 242, 254, 0.5);
            color: var(--bg);
        }}
        
        /* Animations */
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes pulseGlow {{
            0% {{ box-shadow: 0 0 10px rgba(0, 242, 254, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(0, 242, 254, 0.6); }}
            100% {{ box-shadow: 0 0 10px rgba(0, 242, 254, 0.2); }}
        }}
        
        /* Apply animations to layout */
        .block-container {{
            animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}

        /* Scrollbar Styling */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(15, 23, 42, 0.8);
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(0, 242, 254, 0.3);
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(0, 242, 254, 0.8);
        }}

        /* Sidebar Glass Effect */
        [data-testid="stSidebar"] {{
            background: rgba(15, 23, 42, 0.6) !important;
            backdrop-filter: blur(25px);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }}
        
        /* Metric Cards Counter Setup */
        .metric-value-anim {{
            display: inline-block;
            transition: all 0.5s ease;
        }}
        
        /* Streamlit Tabs */
        button[data-baseweb="tab"] {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em;
            color: var(--muted);
            background-color: transparent;
            padding-bottom: 12px;
            transition: all 0.3s ease;
        }}
        
        button[data-baseweb="tab"]:hover {{
            color: var(--primary);
            text-shadow: 0 0 10px rgba(0, 242, 254, 0.4);
        }}
        
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: var(--primary);
            border-bottom-color: var(--primary) !important;
            box-shadow: 0 4px 15px -10px var(--primary);
        }}
        
        button[data-baseweb="tab"][aria-selected="true"] p {{
            color: var(--primary) !important;
            font-weight: 800 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Inject Global JS
    import streamlit.components.v1 as components
    components.html("""
    <script>
        const parentDoc = window.parent.document;
        
        // Smooth scrolling for sidebar links and internal links
        parentDoc.addEventListener('click', function(e) {
            if(e.target.tagName === 'A' && e.target.href.includes('#')) {
                e.preventDefault();
                const targetId = e.target.getAttribute('href').substring(1);
                const targetElement = parentDoc.getElementById(targetId);
                if(targetElement) {
                    targetElement.scrollIntoView({behavior: 'smooth', block: 'start'});
                }
            }
        });
        
        // Add Intersection Observer for scroll animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });
        
        // Observe elements
        setTimeout(() => {
            const cards = parentDoc.querySelectorAll('.glass-card');
            cards.forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
                observer.observe(card);
            });
            
            // Animated Counters
            const counters = parentDoc.querySelectorAll('.animate-number');
            counters.forEach(counter => {
                const updateCount = () => {
                    const target = +counter.getAttribute('data-target');
                    const count = +counter.innerText;
                    const speed = 200; // lower is faster
                    const inc = target / speed;
                    
                    if (count < target) {
                        counter.innerText = Math.ceil(count + inc);
                        setTimeout(updateCount, 15);
                    } else {
                        counter.innerText = target;
                    }
                };
                
                // Use observer to only animate when visible
                const counterObserver = new IntersectionObserver(entries => {
                    if(entries[0].isIntersecting) {
                        updateCount();
                        counterObserver.disconnect();
                    }
                }, { threshold: 0.5 });
                
                counterObserver.observe(counter);
            });
            
        }, 500);
    </script>
    """, height=0)
