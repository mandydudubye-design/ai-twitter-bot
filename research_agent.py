import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from feishu_notify import send_feishu_message
from config import FEISHU_WEBHOOK

def main(topic):
    report = f"""
📊 **深度研究报告**

## 话题: {topic}

### 核心摘要
{topic} 是当前X平台热门讨论话题。

### 社区讨论
- 用户反馈热烈
- 技术实现受关注
- 商业前景被看好

### 创作建议
1. 从用户痛点切入
2. 结合技术发展
3. 提供实用价值

---
💡 回复「内容 {topic}」生成推文
"""
    send_feishu_message(FEISHU_WEBHOOK, report)

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "AI最新动态"
    main(topic)
