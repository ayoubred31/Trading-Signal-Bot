import requests
import pandas as pd

# إعدادات الربط الخاصة بك
USER_KEY = "U4ja2s7cjw7xua1dpeymw22jc4zgdu"
APP_TOKEN = "Az1utea8g5p2uz19njt9futa9uhd4x"

def send_notification(title, message):
    url = "https://api.pushover.net/1/messages.json"
    data = {"token": APP_TOKEN, "user": USER_KEY, "title": title, "message": message}
    requests.post(url, data=data)

# --- استراتيجية SK System ---
def sk_system_logic(current_price, high, low):
    fib_level = high - (0.618 * (high - low))
    if current_price <= fib_level:
        return "شراء (منطقة ذهبية SK)"
    return None

# --- استراتيجية CMS ---
def cms_logic(ema_fast, ema_slow):
    if ema_fast > ema_slow:
        return "شراء (زخم صاعد CMS)"
    return None

def main():
    # هنا يتم جلب البيانات (سنستخدم بيانات تجريبية حالياً للتأكد من الربط)
    price = 50000
    h, l = 55000, 48000
    ema_f, ema_s = 51000, 50000

    sk_res = sk_system_logic(price, h, l)
    cms_res = cms_logic(ema_f, ema_s)

    if sk_res and cms_res:
        send_notification("🔥 إشارة مدمجة قوية", f"الاستراتيجيتان تعطيان دخول: {sk_res} و {cms_res}")
    else:
        send_notification("✅ السكريبت يعمل", "لا توجد إشارات قوية حالياً، سأستمر في المراقبة.")

if __name__ == "__main__":
    main()
