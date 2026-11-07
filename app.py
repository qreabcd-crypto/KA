import streamlit as st
import io
from PIL import Image
from fpdf import FPDF
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="KA Text to PDF and Pic Generator", 
    page_icon="🫀", 
    layout="centered"
)

# Custom Styling for Beautiful Telugu/English Fonts & Backgrounds
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 12px;
        font-weight: bold;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Authentication & Security System
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "recovery_mode" not in st.session_state:
    st.session_state["recovery_mode"] = False

def login_screen():
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>🔒 KA App Master Login</h2>", unsafe_allow_html=True)
    
    if not st.session_state["recovery_mode"]:
        username = st.text_input("User Name:")
        password = st.text_input("Password:", type="password")
        
        if st.button("Login 🚀"):
            # Master Credentials
            if username == "bujji" and password == "bujji123":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("❌ యూజర్ నేమ్ లేదా పాస్‌వర్డ్ తప్పు!")
        
        if st.button("పాస్‌వర్డ్ మర్చిపోయారా? (Recovery)"):
            st.session_state["recovery_mode"] = True
            st.rerun()
    else:
        st.subheader("🔑 Password Recovery")
        recovery_input = st.text_input("మీ రిజిస్టర్డ్ Phone / Email ఎంటర్ చేయండి:")
        captcha = st.text_input("Captcha: 7 + 5 = ఎంత?")
        
        if st.button("Verify & Reset"):
            if captcha == "12" and recovery_input:
                st.success("✅ సక్సెస్! మీ మాస్టర్ పాస్‌వర్డ్: bujji123")
                if st.button("Back to Login"):
                    st.session_state["recovery_mode"] = False
                    st.rerun()
            else:
                st.error("❌ తప్పు వివరాలు ఎంటర్ చేశారు.")

if not st.session_state["logged_in"]:
    login_screen()
else:
    # 3. KA Master Dashboard
    st.markdown("<h1 style='text-align: center; color: #d90429;'>❤️ KA Master Journal & PDF Generator ❤️</h1>", unsafe_allow_html=True)
    st.write("✨ మీ ప్రైవేట్ టెక్స్ట్, పిక్చర్స్ మరియు అపరిమిత PDF క్రియేటర్ ✨")
    
    # Navigation Tabs
    tab1, tab2, tab3 = st.tabs(["📝 జర్నల్ & PDF క్రియేటర్", "🖼️ ప్రైవేట్ ఫోటో వ్యూయర్", "⚙️ అకౌంట్ సెట్టింగ్స్"])
    
    with tab1:
        st.subheader("అందమైన డిజైన్‌తో పేజీ క్రియేట్ చేయండి")
        
        title = st.text_input("కథ / చాప్టర్ టైటిల్ (Headline):")
        bg_style = st.selectbox("బ్యాక్‌గ్రౌండ్ కలర్ థీమ్ ఎంచుకోండి:", ["Classic White", "Romantic Pink", "Golden Glow", "Midnight Dark"])
        
        text_content = st.text_area("మీ టెక్స్ట్ లేదా రాయాలనుకున్న విషయాలు ఇక్కడ ఇవ్వండి:", height=200)
        uploaded_image = st.file_uploader("పర్సనల్ ఫోటో యాడ్ చేయండి (Optional):", type=["jpg", "png", "jpeg"])
        
        # Simple AI Enhancement Simulation
        if st.checkbox("✨ AI Text Enhancement (ఎమోజీలు & స్టైలిష్ ప్యాకింగ్ యాడ్ చేయి)"):
            if text_content:
                text_content = f"💖 {text_content} 🌸\n\n#KA_Special_Memories #Bujji 🫀✨"
        
        if title or text_content:
            st.markdown("---")
            st.subheader("Preview (మీ పేజీ ఇలా కనిపిస్తుంది):")
            st.markdown(f"### 🌺 {title}")
            st.write(text_content)
            if uploaded_image:
                img = Image.open(uploaded_image)
                st.image(img, width=300, caption="Attached Personal Photo")
        
        # Unlimited PDF Download Option
        if st.button("📄 Unlimited PDF గా మార్చు (Download PDF)"):
            if title and text_content:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=16)
                pdf.cell(200, 10, txt=title.encode('latin-1', 'replace').decode('latin-1'), ln=1, align='C')
                pdf.ln(10)
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=text_content.encode('latin-1', 'replace').decode('latin-1'))
                
                pdf_output = pdf.output(dest='S').encode('latin-1')
                st.download_button(
                    label="💾 📥 డౌన్‌లోడ్ PDF",
                    data=pdf_output,
                    file_name=f"{title}_KA_Journal.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning("దయచేసి PDF తయారీకి టైటిల్ మరియు కంటెంట్ ఎంటర్ చేయండి!")
                
    with tab2:
        st.subheader("🔒 దాచుకున్న ప్రైవేట్ ఫోటోలు & గ్యాలరీ")
        st.info("ఇక్కడ మీరు సేవ్ చేసుకున్న రహస్య ఫోటోలు మాత్రమే కనిపిస్తాయి.")
        if uploaded_image:
            st.image(uploaded_image, caption="మీరు అప్‌లోడ్ చేసిన ప్రైవేట్ ఫొటో", use_column_width=True)
        else:
            st.write("ఇంకా ఎలాంటి పర్సనల్ పిక్స్ దాచలేదు.")
            
    with tab3:
        st.subheader("👤 అకౌంట్ మాస్టర్ కంట్రోల్")
        st.write("యూజర్ నేమ్: **bujji**")
        st.write("మాస్టర్ అప్‌డేట్ యాక్సెస్: **Active (Only For You)**")
        if st.button("Logout 🚪"):
            st.session_state["logged_in"] = False
            st.rerun()
