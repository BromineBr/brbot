# brbot
基于Nonebot和mai-bot的个人qq机器人，主要面对0721群群友
## 项目部署
依赖于 Nonebot 和 mai-bot 的支持，可以通过

	pip install -r requirements.txt

安装依赖,

	python bot.py

运行项目
## 关于CQ-HTTP
前往 https://github.com/Mrs4s/go-cqhttp > Releases，下载适合自己操作系统的可执行文件。
go-cqhttp 在初次启动时会询问代理方式，选择反向 websocket 代理即可。

之后用任何文本编辑器打开`config.yml`文件，设置反向 ws 地址、上报方式：
```yml
message:
  post-format: array
  
servers:
  - ws-reverse:
      universal: ws://127.0.0.1:10219/cqhttp/ws
```
然后设置您的 QQ 号和密码。您也可以不设置密码，选择扫码登陆的方式。

至此，您可以和对应的 QQ 号聊天并使用 mai bot 的所有功能了。
## brbot能够实现的功能

---
### mai-bot自带功能
---
#### 今日舞萌
查看今天的舞萌运势
#### XXXmaimaiXXX什么
随机一首歌
#### 随个[dx/标准][绿黄红紫白]<难度> 
随机一首指定条件的乐曲
#### 查歌<乐曲标题的一部分> 
查询符合条件的乐曲
#### [绿黄红紫白]id<歌曲编号> 
查询乐曲信息或谱面信息
#### <歌曲别名>是什么歌 
查询乐曲别名对应的乐曲
#### 定数查歌 <定数>  
查询定数对应的乐曲
#### 定数查歌 <定数下限> <定数上限>
#### 分数线 <难度+歌曲id> <分数线> 
详情请输入“分数线 帮助”查看

---

### 额外功能
---
#### roll.<检定技能>.<技能点> 
roll点
#### choose.<事件1>.<事件2>.…….<事件n> 
从n个事件中选择某一事件
#### BrBot抽卡&图鉴查询
抽卡
#### BrBot贴贴 
贴贴
#### 饭 <人数>、饭 几 
统计、查询恰饭人数
#### 随个龙图 
随机发送龙图
#### 随机贴贴
贴到群友老婆会被骂
#### 戳一戳功能
*可以戳戳试试*
#### 消息撤回自动回复
*你撤回干啥*
#### +1s 
为长者续一秒
#### 随机击剑 
群友乱交(bushi)
#### 随机怪话
随机群友怪话
