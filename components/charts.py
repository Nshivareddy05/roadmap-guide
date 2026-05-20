import plotly.graph_objects as go
import pandas as pd
import config

def plot_salary_trends(salary_data):
    levels = list(salary_data.keys())
    # Extract average from strings like "$80k - $120k"
    averages = []
    for level, range_str in salary_data.items():
        try:
            parts = range_str.replace('$', '').replace('k', '').replace('+', '').split('-')
            if len(parts) == 2:
                avg = (float(parts[0].strip()) + float(parts[1].strip())) / 2
            else:
                avg = float(parts[0].strip())
            averages.append(avg * 1000) # Convert back to real numbers
        except:
            averages.append(0)
            
    fig = go.Figure(data=[
        go.Bar(
            x=levels, 
            y=averages,
            marker_color=config.THEME_COLORS['primary'],
            text=[f"${int(avg/1000)}k" for avg in averages],
            textposition='auto'
        )
    ])
    
    fig.update_layout(
        title="Average Salary Trends (USD)",
        title_font_color=config.THEME_COLORS['text'],
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=config.THEME_COLORS['muted'],
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)", tickprefix="$", ticksuffix="k", tickformat=",.0s"),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_domain_comparison(domain1, data1, domain2, data2):
    # Radar chart for comparing abstract metrics
    categories = ['Demand', 'Difficulty', 'Math Required', 'Coding Required', 'Hardware Focus']
    
    # Dummy logic to assign scores based on domain name (since we don't have this in JSON currently)
    # In a real app, this would be in domains.json
    def get_scores(domain):
        if "Computer" in domain or "Software" in domain:
            return [9, 7, 6, 10, 2]
        elif "AI" in domain or "Data" in domain:
            return [10, 9, 10, 9, 3]
        elif "Mechanical" in domain or "Civil" in domain:
            return [7, 8, 8, 3, 9]
        elif "Electrical" in domain or "Electronics" in domain:
            return [8, 9, 9, 6, 10]
        else:
            return [6, 7, 7, 5, 5]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=get_scores(domain1),
        theta=categories,
        fill='toself',
        name=domain1,
        line_color=config.THEME_COLORS['primary']
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=get_scores(domain2),
        theta=categories,
        fill='toself',
        name=domain2,
        line_color=config.THEME_COLORS['secondary']
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], gridcolor="rgba(255,255,255,0.1)"),
            bgcolor="rgba(0,0,0,0)"
        ),
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=config.THEME_COLORS['text'],
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig
