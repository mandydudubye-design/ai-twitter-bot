import requests
import json

def send_feishu_message(webhook_url, message, msg_type="text"):
    if not webhook_url:
        print("⚠️ 未配置飞书 Webhook")
        return False
    
    payload = {
        "msg_type": msg_type,
        "content": {"text": message}
    }
    
    try:
        response = requests.post(webhook_url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                print("✅ 飞书消息发送成功")
                return True
        return False
    except Exception as e:
        print(f"❌ 飞书消息发送异常: {e}")
        return False
