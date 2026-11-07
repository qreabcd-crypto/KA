import streamlit as st

# 1. యాప్ పేరు & ఐకాన్ (App Name: KA)
st.set_page_config(page_title="KA App", page_icon="🫀", layout="centered")

# 2. పాస్‌వర్డ్ & మాస్టర్ కంట్రోల్ (Security / Master Control)
def check_password():
    def password_entered():
        if st.session_state["password"] == "bujji123":  # ఇక్కడ మీ పాస్‌వర్డ్ మార్చుకోవచ్చు
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>🔒 KA App Login</h2>", unsafe_allow_html=True)
        st.text_input("మాస్టర్ పాస్‌వర్డ్ ఎంటర్ చేయండి:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>🔒 KA App Login</h2>", unsafe_allow_html=True)
        st.text_input("పాస్‌వర్డ్ తప్పు! మళ్లీ ప్రయత్నించండి:", type="password", on_change=password_entered, key="password")
        st.error("❌ ప్రవేశం నిరాకరించబడింది")
        return False
    else:
        return True

if check_password():
    # --- KA APP MAIN DASHBOARD ---
    st.markdown("<h1 style='text-align: center; color: #d90429;'>❤️ KA App ❤️</h1>", unsafe_allow_html=True)
    st.write("బుజ్జమ్మ కోసం ప్రత్యేకంగా తయారుచేసిన ప్రైవేట్ యాప్ 😍😘💋🍦🫀")
    st.markdown("---")

    # అన్‌లిమిటెడ్ పేజీలు & కంటెంట్ క్రియేషన్
    chapter_title = st.text_input("చాప్టర్ / కథ టైటిల్:")
    story_content = st.text_area("ఇక్కడ మీ కథ లేదా కవిత రాయండి (తెలుగు & Emojis పర్ఫెక్ట్‌గా వస్తాయి):", height=250)

    if st.button("సేవ్ చేయి 💾"):
        if chapter_title and story_content:
            st.success(f"'{chapter_title}' విజయవంతంగా KA యాప్‌లో సేవ్ అయింది!")
            st.markdown("---")
            st.subheader(chapter_title)
            st.write(story_content)
        else:
            st.warning("దయచేసి టైటిల్ మరియు కంటెంట్ ఎంటర్ చేయండి!")
          
