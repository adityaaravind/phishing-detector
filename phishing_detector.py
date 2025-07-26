import streamlit as st
import re
from urllib.parse import urlparse

# Set page config
st.set_page_config(page_title="Fake Payment Page Phishing Detector", layout="centered")
st.title("🔍 Fake Payment Page Phishing Detector")

st.markdown("""
This tool helps identify **potential phishing URLs** by checking:
- HTTPS usage
- Suspicious keywords
- Known domain mismatch
- Shortened URLs
""")

# User input
url = st.text_input("🔗 Enter a payment page URL to analyze:", "http://example-payment.com/pay")

# Detection functions
def is_https(url):
    return url.lower().startswith("https://")

def contains_suspicious_keywords(url):
    suspicious_keywords = ['login', 'secure', 'verify', 'paypal', 'banking', 'account', 'payment', 'confirm']
    return any(keyword in url.lower() for keyword in suspicious_keywords)

def has_mismatched_domain(url):
    trusted_domains = ['paypal.com', 'stripe.com', 'fiserv.com', 'bankofamerica.com', 'chase.com']
    parsed_domain = urlparse(url).netloc
    return not any(td in parsed_domain for td in trusted_domains)

def is_shortened_url(url):
    return re.match(r"(https?://)?(bit\.ly|tinyurl\.com|t\.co|goo\.gl|rb\.gy|is\.gd)", url)

# Analysis
def analyze_url(url):
    return {
        'Uses HTTPS': is_https(url),
        'Contains Suspicious Keywords': contains_suspicious_keywords(url),
        'Domain Matches Known Providers': not has_mismatched_domain(url),
        'Shortened URL Detected': bool(is_shortened_url(url))
    }

if url:
    results = analyze_url(url)
    st.subheader("🔎 Analysis Result")
    for check, passed in results.items():
        if passed:
            st.success(f"✅ {check}")
        else:
            st.error(f"⚠️ {check}")

    if not all(results.values()):
        st.warning("⚠️ This URL may be suspicious. Be cautious before entering sensitive data.")
    else:
        st.success("✅ This URL looks safe based on these checks.")
