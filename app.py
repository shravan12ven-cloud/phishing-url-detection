def check_url(url):
    suspicious_words = [
        "login", "verify", "bank", "secure",
        "update", "account", "paypal"
    ]

    for word in suspicious_words:
        if word.lower() in url.lower():
            return "⚠️ Warning: This URL may be a phishing website!"

    return "✅ Safe URL"

print("=== Phishing URL Detection System ===")
url = input("Enter Website URL: ")
result = check_url(url)
print(result)