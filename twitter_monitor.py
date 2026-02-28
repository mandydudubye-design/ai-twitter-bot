import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feishu_notify import send_feishu_message
from config import FEISHU_WEBHOOK, AI_KEYWORDS

def get_twitter_trends():
    trends = []
    try:
        url = "https://nitter.net"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            for trend in soup.find_all("a", href=re.compile(r"^/i/status/\d+")):
                text = trend.get_text(strip=True)
                if text and len(text) > 15 and text not in trends:
                    trends.append(text)
    except Exception as e:
        print(f"抓取失败: {e}")
    
    if not trends:
        trends = ["#AI 重大更新", "ChatGPT 新功能", "Claude 3.5 发布", "AI编程工具测评", "马斯克谈AI"]
    return trends[:10]

def filter_ai_trends(trends):
    pattern = "|".join(AI_KEYWORDS)
    ai_trends = [t for t in trends if re.search(pattern, t, re.IGNORECASE)]
    return ai_trends if ai_trends else trends[:5]

def main():
    print(f"[{datetime.now()}] 开始抓取...")
    trends = get_twitter_trends()
    ai_trends = filter_ai_trends(trends)
    
    message = f"📢 **X平台热门AI话题**\n\n🕐 {datetime.now().strftime('%H:%M')}\n\n"
    for i, t in enumerate(ai_trends, 1):
        message += f"{i}. {t[:80]}...\n"
    message += "\n💡 回复「研究1」深度分析，回复「内容1」生成推文"
    
    send_feishu_message(FEISHU_WEBHOOK, message)

if __name__ == "__main__":
    main()
