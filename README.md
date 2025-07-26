# phishing-detector
# 🔐 Fake Payment Page Phishing Detector

Welcome to a simple, smart, and beginner-friendly tool that helps you **detect potentially fake or phishing payment pages** — especially useful if you're about to make a payment online or share personal info.

Built using **Streamlit** and **Python**, this tool is inspired by real-world security systems used in companies like **Fiserv**, a global leader in fintech and digital banking.

---

## 🌐 Live App

👉 [Click here to try the app](https://payment-phishing-detector.streamlit.app/)

---

## 🚨 What This App Does

You paste a payment page URL into the tool. It will scan the link for common signs of **phishing** or **fraud**, such as:

| ✅ Safe Practice | ⚠️ Risk Detected |
|-----------------|------------------|
| Uses `https://` (secure) | Uses plain `http://` (not secure) |
| Real domain like `paypal.com` | Fake domain like `paypal-security-login.net` |
| Clean and simple URL | Suspicious words like `verify`, `secure`, `login` |
| Trusted provider (PayPal, Stripe, Fiserv) | Unknown or mismatched domains |
| Full link visible | Shortened link like `bit.ly/3hXyz` |

The app **does not require you to log in** or enter private data. Just paste the **URL of the payment page** you're unsure about.

---

## 💼 Why This Project Matters

Every year, millions fall victim to fake payment pages that steal sensitive financial info like:
- Debit/credit card numbers
- Bank login credentials
- UPI or PayPal access

This project helps raise awareness about **safe digital habits** while also simulating how companies like **Fiserv** monitor transactions to detect fraud.

---

## 🧪 How It Works (In Simple Terms)

The app runs a few behind-the-scenes checks on the link you provide:

| Check | What It Means |
|-------|----------------|
| 🔒 **Uses HTTPS** | Is the link encrypted and secure? |
| 🕵️ **Suspicious Keywords** | Does the URL have words like `login`, `verify`, or `secure` that scammers often use? |
| 🌐 **Trusted Domain Match** | Is it a known provider (like `paypal.com`) or something sketchy? |
| ⛔ **Shortened URL Detected** | Is the link hiding its real destination (e.g., `bit.ly`)? |

Each result will be shown as:

✅ Safe → Good to go  
⚠️ Warning → Be cautious!  
❌ Risk → Likely phishing, don’t proceed

---

## 🧠 Who Can Use This?

This tool is designed for **everyone**, not just techies. Whether you're:
- A regular online shopper
- A small business owner
- A banking or fintech professional
- Or just someone who wants to be cautious online

You can use this tool to **quickly verify a link** before trusting it.

---

## 📦 How to Run Locally (for developers)

If you want to run it on your own computer:

```bash
git clone https://github.com/your-username/phishing-detector-fiserv.git
cd phishing-detector-fiserv
pip install -r requirements.txt
streamlit run phishing_detector.py
