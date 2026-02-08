import streamlit as st
import ollama
from PIL import Image
import base64
import io


st.set_page_config(
    page_title="AI Image Summarizer",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Clean and minimal CSS
st.markdown("""
    <style>
    /* Hide Streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Clean font */
    * {font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;}
    
    /* Container spacing */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 900px;
    }
    
    /* Header */
    .header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    
    .header p {
        font-size: 1.1rem;
        color: #666;
        font-weight: 400;
    }
    
    /* Result cards */
    .result-box {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #4A90E2;
    }
    
    .result-box h3 {
        font-size: 1.2rem;
        color: #1a1a1a;
        margin: 0 0 1rem 0;
        font-weight: 600;
    }
    
    .result-box .content {
        color: #333;
        line-height: 1.7;
        font-size: 0.95rem;
        white-space: pre-wrap;
    }
    
    /* Color coding */
    .result-box.description {border-left-color: #4A90E2;}
    .result-box.summary {border-left-color: #9B59B6;}
    
    /* Image container */
    .image-box {
        background: white;
        border: 1px solid #e1e4e8;
        border-radius: 12px;
        padding: 1rem;
        margin: 1.5rem 0;
    }
    
    /* Loading */
    .loading {
        text-align: center;
        color: #666;
        padding: 2rem;
        font-size: 1.1rem;
    }
    
    /* Placeholder */
    .placeholder {
        text-align: center;
        padding: 3rem 2rem;
        color: #666;
    }
    
    .placeholder-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    /* Button */
    .stButton > button {
        background: #4A90E2;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: #357ABD;
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: #e1e4e8;
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "results" not in st.session_state:
    st.session_state.results = None

# Header
st.markdown("""
<div class="header">
    <h1>🔍 AI Image Summarizer</h1>
    <p>Upload an image for AI-powered analysis</p>
</div>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"],
    help="Supported: PNG, JPG, JPEG"
)

if uploaded_file:
    # Display image
    st.markdown('<div class="image-box">', unsafe_allow_html=True)
    st.image(uploaded_file, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Convert to base64
    image = Image.open(uploaded_file)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_b64 = base64.b64encode(buffer.getvalue()).decode()
    
    # Process if not already done
    if st.session_state.results is None:
        st.markdown('<div class="loading">🤖 Analyzing image...</div>', unsafe_allow_html=True)
        
        try:
            # Description
            desc_response = ollama.chat(
                model='llava:13b',
                messages=[{
                    'role': 'user',
                    'content': 'Describe this image in detail. Include all visible objects, text, people, and context.',
                    'images': [image_b64]
                }]
            )
            
            # Summary
            summary_response = ollama.chat(
                model='llava:13b',
                messages=[{
                    'role': 'user',
                    'content': 'Provide a brief summary of this image in 3-4 bullet points.',
                    'images': [image_b64]
                }]
            )
            
            st.session_state.results = {
                'description': desc_response['message']['content'],
                'summary': summary_response['message']['content']
            }
            
            st.rerun()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    # Display results
    if st.session_state.results:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # Description
        st.markdown(f"""
        <div class="result-box description">
            <h3>📝 Description</h3>
            <div class="content">{st.session_state.results['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Summary
        st.markdown(f"""
        <div class="result-box summary">
            <h3>💡 Summary</h3>
            <div class="content">{st.session_state.results['summary']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Reset button
        if st.button("🔄 Analyze Another Image"):
            st.session_state.results = None
            st.rerun()

else:
    # Placeholder
    st.markdown("""
    <div class="placeholder">
        <div class="placeholder-icon">📸</div>
        <h3 style="color: #333; margin-bottom: 0.5rem;">No Image Uploaded</h3>
        <p style="color: #666;">Upload an image to get started with AI analysis</p>
    </div>
    """, unsafe_allow_html=True)