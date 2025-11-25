# theme.py
# Enhanced Dark/Light Mode CSS for Perry App

def get_custom_css(dark_mode=False):
    """Get custom CSS based on theme with enhanced dark mode support"""
    
    # Base CSS that applies to both themes
    base_css = """
    <style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease !important;
    }
    
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .main-header {
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .metric-card {
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .risk-high {
        border-left: 5px solid #f44336;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .risk-medium {
        border-left: 5px solid #ff9800;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .risk-low {
        border-left: 5px solid #4caf50;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .timer-display {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        font-family: 'Courier New', monospace;
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        transition: all 0.3s ease;
    }
    
    .quote-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        font-style: italic;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .streak-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.2rem;
        box-shadow: 0 2px 8px rgba(245, 87, 108, 0.3);
    }
    
    .session-card {
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .session-card:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .blocking-active {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
        animation: pulse 2s infinite;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.85; transform: scale(0.98); }
    }
    
    .camera-active {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        font-size: 0.9rem;
        animation: pulse 2s infinite;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.4);
    }
    
    .journal-entry-card {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .journal-entry-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .journal-entry-date {
        font-weight: bold;
        color: #667eea;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .journal-entry-text {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        line-height: 1.6;
    }
    
    .emotion-tag {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.85rem;
        margin: 0.2rem;
        font-weight: 500;
    }
    
    .schedule-card {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid;
        transition: all 0.3s ease;
    }
    
    .schedule-card:hover {
        transform: translateX(5px);
    }
    
    .schedule-card.priority-high {
        border-left-color: #f44336;
    }
    
    .schedule-card.priority-medium {
        border-left-color: #ff9800;
    }
    
    .schedule-card.priority-low {
        border-left-color: #4caf50;
    }
    
    /* Improved scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #667eea;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #764ba2;
    }
    
    /* Button improvements */
    .stButton button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    </style>
    """
    
    # Light theme specific CSS
    light_theme_css = """
    <style>
    /* Streamlit base */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ebf0 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
        border-right: 1px solid #e0e0e0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 1px solid #e0e0e0;
    }
    
    .risk-high {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
    }
    
    .risk-medium {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
    }
    
    .risk-low {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    }
    
    .timer-display {
        color: #667eea;
        background: linear-gradient(135deg, #ffffff 0%, #f5f7fa 100%);
        border: 2px solid #667eea;
    }
    
    .session-card {
        background: white;
        border: 1px solid #e0e0e0;
    }
    
    .journal-entry-card {
        background: white;
        border: 1px solid #e0e0e0;
    }
    
    .journal-entry-text {
        background: rgba(102, 126, 234, 0.05);
        color: #333;
    }
    
    .schedule-card {
        background: white;
        border: 1px solid #e0e0e0;
    }
    
    .emotion-tag {
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
    }
    </style>
    """
    
    # Dark theme specific CSS
    dark_theme_css = """
    <style>
    /* Streamlit base - True dark mode */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a202c 0%, #0f172a 100%);
        border-right: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #8b9dff 0%, #a076d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .metric-card:hover {
        box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        border: 1px solid rgba(139, 157, 255, 0.4);
    }
    
    .risk-high {
        background: linear-gradient(135deg, #4a1a1a 0%, #3a1515 100%);
        border-left: 5px solid #ff6b6b;
        color: #ffcdd2;
    }
    
    .risk-medium {
        background: linear-gradient(135deg, #4a3a1a 0%, #3a2e15 100%);
        border-left: 5px solid #ffa726;
        color: #ffe0b2;
    }
    
    .risk-low {
        background: linear-gradient(135deg, #1a4a2e 0%, #153a23 100%);
        border-left: 5px solid #66bb6a;
        color: #c8e6c9;
    }
    
    .timer-display {
        color: #8b9dff;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border: 2px solid rgba(139, 157, 255, 0.3);
        box-shadow: 0 4px 20px rgba(139, 157, 255, 0.2);
    }
    
    .session-card {
        background: #1e293b;
        border-left: 4px solid #8b9dff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .session-card:hover {
        background: #334155;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }
    
    .journal-entry-card {
        background: #1e293b;
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .journal-entry-card:hover {
        background: #334155;
        border: 1px solid rgba(139, 157, 255, 0.4);
    }
    
    .journal-entry-date {
        color: #8b9dff;
    }
    
    .journal-entry-text {
        background: rgba(139, 157, 255, 0.1);
        color: #e2e8f0;
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .schedule-card {
        background: #1e293b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .schedule-card:hover {
        background: #334155;
    }
    
    .emotion-tag {
        background: rgba(139, 157, 255, 0.2);
        color: #a0aec0;
        border: 1px solid rgba(139, 157, 255, 0.3);
    }
    
    .quote-box {
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Dark scrollbar */
    ::-webkit-scrollbar-track {
        background: #0f172a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #334155;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #667eea;
    }
    
    /* Streamlit component overrides for dark mode */
    .stMarkdown, .stText {
        color: #e2e8f0 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9 !important;
    }
    
    p, span, div {
        color: #cbd5e1;
    }
    
    a {
        color: #8b9dff;
    }
    
    a:hover {
        color: #a076d4;
    }
    
    hr {
        border-color: rgba(139, 157, 255, 0.2);
    }
    
    /* Input fields dark mode */
    .stTextInput input, .stTextArea textarea, .stSelectbox select, 
    .stNumberInput input, .stDateInput input, .stTimeInput input {
        background: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(139, 157, 255, 0.3) !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {
        border: 1px solid rgba(139, 157, 255, 0.6) !important;
        box-shadow: 0 0 0 1px rgba(139, 157, 255, 0.3) !important;
    }
    
    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #cbd5e1 !important;
    }
    
    /* Metrics dark mode */
    .stMetric {
        background: #1e293b;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid rgba(139, 157, 255, 0.2);
    }
    
    .stMetric label {
        color: #94a3b8 !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #f1f5f9 !important;
    }
    
    /* Expander dark mode */
    .stExpander {
        background: #1e293b;
        border: 1px solid rgba(139, 157, 255, 0.2);
        border-radius: 8px;
    }
    
    /* Tabs dark mode */
    .stTabs [data-baseweb="tab-list"] {
        background: #1e293b;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #94a3b8;
    }
    
    .st Tabs [aria-selected="true"] {
        color: #8b9dff !important;
    }
    
    /* Alert boxes dark mode */
    .stAlert {
        background: rgba(30, 41, 59, 0.8) !important;
        border: 1px solid rgba(139, 157, 255, 0.3) !important;
        color: #e2e8f0 !important;
    }
    
    /* Progress bar dark mode */
    .stProgress > div > div {
        background: #8b9dff;
    }
    
    /* Button dark mode improvements */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #8b9dff 0%, #a076d4 100%);
    }
    </style>
    """
    
    if dark_mode:
        return base_css + dark_theme_css
    else:
        return base_css + light_theme_css
