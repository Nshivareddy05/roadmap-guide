import streamlit as st

def render(domains_data):
    st.title("🤖 AI Career Recommendation")
    st.markdown("<p style='color: var(--muted);'>Take this quick quiz, and our heuristic engine will recommend the best engineering domain for you based on your interests and strengths.</p>", unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        st.subheader("1. What type of problems do you enjoy solving?")
        q1 = st.radio("Select one:", [
            "Logic puzzles, writing scripts, optimizing algorithms",
            "Analyzing data trends, statistics, predicting outcomes",
            "Designing physical structures, figuring out how machines work",
            "Working with circuits, hardware, electromagnetism",
            "Finding vulnerabilities, security, breaking things"
        ], key="q1", label_visibility="collapsed")
        
        st.subheader("2. What is your preferred work environment?")
        q2 = st.radio("Select one:", [
            "Deep focus at a computer, mostly software",
            "Research-oriented, heavily mathematical",
            "A mix of design software (CAD) and physical testing labs",
            "Working with electronics, soldering, testing signals",
            "Fast-paced, constantly adapting to new threats"
        ], key="q2", label_visibility="collapsed")
        
        st.subheader("3. Which of these sounds like the coolest project?")
        q3 = st.radio("Select one:", [
            "Building a scalable web application or mobile app",
            "Training an AI model to recognize objects in images",
            "Designing an aerodynamic car chassis or a bridge",
            "Creating a smart home automation system with IoT",
            "Hacking into a simulated network to patch vulnerabilities"
        ], key="q3", label_visibility="collapsed")
        
        submitted = st.form_submit_button("Get Recommendation")
        
    if submitted:
        st.markdown("---")
        with st.spinner("Analyzing your profile..."):
            scores = {
                "Computer Science": 0,
                "AI & Machine Learning": 0,
                "Mechanical Engineering": 0,
                "Civil Engineering": 0,
                "Electrical Engineering": 0,
                "Cybersecurity": 0,
                "Data Science": 0
            }
            
            # Simple heuristic scoring
            if "Logic puzzles" in q1: scores["Computer Science"] += 2
            if "data trends" in q1: scores["Data Science"] += 2; scores["AI & Machine Learning"] += 1
            if "machines work" in q1: scores["Mechanical Engineering"] += 2; scores["Civil Engineering"] += 1
            if "circuits" in q1: scores["Electrical Engineering"] += 2
            if "vulnerabilities" in q1: scores["Cybersecurity"] += 2
            
            if "software" in q2: scores["Computer Science"] += 1; scores["Cybersecurity"] += 1
            if "mathematical" in q2: scores["Data Science"] += 2; scores["AI & Machine Learning"] += 2
            if "CAD" in q2: scores["Mechanical Engineering"] += 2; scores["Civil Engineering"] += 2
            if "soldering" in q2: scores["Electrical Engineering"] += 2
            if "threats" in q2: scores["Cybersecurity"] += 2
            
            if "web application" in q3: scores["Computer Science"] += 3
            if "AI model" in q3: scores["AI & Machine Learning"] += 3; scores["Data Science"] += 1
            if "chassis" in q3: scores["Mechanical Engineering"] += 3; scores["Civil Engineering"] += 2
            if "IoT" in q3: scores["Electrical Engineering"] += 3
            if "Hacking" in q3: scores["Cybersecurity"] += 3
            
            # Find the top recommendation
            top_domain = max(scores, key=scores.get)
            
        st.success(f"### 🎉 We recommend: **{top_domain}**")
        st.markdown(f"Based on your answers, your interests strongly align with {top_domain}.")
        
        if top_domain in domains_data:
            st.markdown(f"**Brief Overview:** {domains_data[top_domain].get('overview', '')}")
            st.info("Head over to the **Domain Explorer** page to see the full roadmap and required skills for this domain!")
