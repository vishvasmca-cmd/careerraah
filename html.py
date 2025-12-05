
def get_css():
    return """
    <style>
    .stApp { background-color: #FFF8F0; }
    .block-container { padding-top: 1rem !important; padding-bottom: 6rem !important; }
    
    /* ✨ PREMIUM TILE STYLE (New) */
    .welcome-card {
        background: #FFFFFF;
        padding: 15px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        height: 160px; /* Fixed height for uniformity */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .welcome-card:hover {
        transform: translateY(-5px);
        border-color: #FF6B00;
        box-shadow: 0 8px 20px rgba(255, 107, 0, 0.15);
    }

    .card-icon {
        font-size: 35px;
        background: #E3F2FD;
        width: 60px; height: 60px;
        line-height: 60px;
        border-radius: 50%;
        margin-bottom: 10px;
    }
    
    .card-title {
        color: #1A3C8D;
        font-weight: 800;
        font-size: 1rem;
        margin-bottom: 5px;
    }
    
    .card-desc {
        color: #666;
        font-size: 0.8rem;
        line-height: 1.2;
    }
    
    /* Button Polish */
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Bottom Nav */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; width: 100%; height: 70px;
        background-color: white; border-top: 1px solid #eee;
        display: flex; justify-content: space-around; align-items: center;
        z-index: 99999; padding-bottom: 5px;
    }
    .nav-item { text-align: center; font-size: 0.7rem; color: #888; cursor: pointer; }
    .nav-icon { font-size: 1.4rem; display: block; }
    .nav-item.active { color: #FF6B00; font-weight: bold; }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
"""

def get_header():
    return """
    <style>
    .header-container {
        background: linear-gradient(135deg, #1A3C8D 0%, #0d255e 100%);
        background-size: cover; background-position: center;
        border-radius: 0 0 20px 20px;
        height: auto;
        padding: 1.5rem; margin: -1rem -1rem 1rem -1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    <div class="header-container">&nbsp;</div>
"""
