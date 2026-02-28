import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feishu_notify import send_feishu_message
from config import FEISHU_WEBHOOK

def main(topic):
    scripts = f"""
✍️ **推文脚本 - {topic}**

### 📝 版本1 - 简洁版
{topic} #AI #科技

### 📝 版本2 - 互动版
刚刷到{topic}，太有意思了！
你怎么看？👇
#AI #讨论

### 📝 版本3 - 观点版
关于{topic}的5个关键点：
1. 技术创新
2. 应用场景
3. 行业影响
4. 机会风险
5. 未来展望
#AI #观点

### 📝 版本4 - 投票版
📢 {topic}
A) 看好 ❤️
B) 谨慎 🤔
C) 观望 👀
#AI #投票
"""
    send_feishu_message(FEISHU_WEBHOOK, scripts)

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "AI最新动态"
    main(topic)
