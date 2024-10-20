# 飞书助手
## 构想
编写一个python小程序，实时访问知乎热榜，提取标题，定时存储进入数据库。如果出现热度超过500w，则通过飞书机器人推送消息，返回热榜标题、摘要和链接。此外，针对同一个话题，定时将其热度存入飞书表格，实现对热度的追踪。
pip
## 结构设计
功能分解：
1. 网页访问部分：读取网页信息，提取标题
2. 数据库部分：数据的存取
3. 飞书机器人部分：信息的推送
4. 飞书表格部分：数据的读写