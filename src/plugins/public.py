import random
import re,os
import csv
import datetime

from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot
from src.libraries.image import *
from random import randint


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令如下：
今日舞萌 查看今天的舞萌运势
XXXmaimaiXXX什么 随机一首歌
随个[dx/标准][绿黄红紫白]<难度> 随机一首指定条件的乐曲
查歌<乐曲标题的一部分> 查询符合条件的乐曲
[绿黄红紫白]id<歌曲编号> 查询乐曲信息或谱面信息
<歌曲别名>是什么歌 查询乐曲别名对应的乐曲
定数查歌 <定数>  查询定数对应的乐曲
定数查歌 <定数下限> <定数上限>
分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看
roll.<检定技能>.<技能点> roll点
choose.<事件1>.<事件2>.…….<事件n> 从n个事件中选择某一事件
BrBot抽卡 抽卡
BrBot贴贴 贴贴
饭 <人数>、饭 几 统计、查询恰饭人数
随个龙图 随机发送龙图
随机贴贴
戳一戳功能
+1s 为长者续一秒
随机击剑 群友乱交()'''
    await help.send(Message([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        }
    }]))


async def _group_poke(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    rd = random.randint(1,4)
    if rd == 1:
        await poke.send(Message([{
            "type": "poke",
            "data": {
                "qq": f"{event.sender_id}"
            }
        }]))
    elif rd == 2:
        img = Image.open(f"src/static/image/l.jpg").convert('RGBA')
        await poke.send(Message([{
            "type": "image",
            "data": {
                "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
            }
        }]))
    elif rd == 3:
        await poke.send(Message([{
            "type": "text",
            "data": {
                "text": f"戳你妈"
            }
        }]))
    elif rd == 4:
        await poke.send(Message([{
            "type": "text",
            "data": {
                "text": f"这边建议去戳阿贤呢"
            }
        }]))

rdmimg = on_command("随个涩图")
@rdmimg.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1,2)
    img = Image.open(f"src/static/image/images/{rd}.jpg").convert('RGBA')
    await rdmimg.finish([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
        }
    }])


rdragon = on_command("随个龙图")
@rdragon.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1,191)
    img = Image.open(f"src/static/image/imaged/{rd}.jpg").convert('RGBA')
    await rdragon.finish([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
        }
    }])


rji = on_command("随个鸡图")
@rji.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1, 48)
    img = Image.open(f"src/static/image/imagej/{rd}.jpg").convert('RGBA')
    await rji.finish([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
        }
    }])


rsjn = on_command("随个老干部")
@rsjn.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1, 6)
    img = Image.open(f"src/static/image/sjn/{rd}.jpg").convert('RGBA')
    await rsjn.finish([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
        }
    }])


fan = on_command("饭")
@fan.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(" ", 1)
    id = str(event.get_user_id())
    time0 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    qwq = 0
    if argv[0] == "几":
        f = open("src/static/fan.txt","r")
        qwq = f.read()
        f.close()
        f = open("src/static/time.txt", "r")
        time = f.read()
        f.close()
        if id == "3223196324":
            img = Image.open(f"src/static/image/zzx.jpg").convert('RGBA')
            await fan.send(Message([
            {
                "type": "text",
                "data": {
                    "text": f"饭 {qwq}\n阿贤该减肥了，你不许吃了(｡ì _ í｡)\n上次更新于{time}"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }
        ]))
        elif id == "1187710717":
            img = Image.open(f"src/static/image/sjn.jpg").convert('RGBA')
            await fan.send(Message([
                {
                    "type": "text",
                    "data": {
                        "text": f"饭 {qwq}\n今天的老干部不省钱了吗(⊙o⊙)\n上次更新于{time}"
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                    }
                }
            ]))
        elif id == "1516077112":
            await fan.send(f"饭 {qwq}\n主人贴贴(˶╹ꇴ╹˶）\n上次更新于{time}")
        elif id == "1350165753":
            await fan.send(f"饭 {qwq}\n米浴，我好喜欢你啊（♡▽♡）\n上次更新于{time}")
        else:
            await fan.send(f"饭 {qwq}\n上次更新于{time}")
    elif is_number(argv[0]):
        f = open("src/static/fan.txt", "w")
        f.write(argv[0])
        f.close()
        f = open("src/static/time.txt", "w")
        f.write(time0)
        f.close()
        if id == "3223196324":
            img = Image.open(f"src/static/image/zzx.jpg").convert('RGBA')
            await fan.send(Message([
            {
                "type": "text",
                "data": {
                    "text": "收到٩(๑•̀ω•́๑)۶\n阿贤该减肥了，你不许吃了\n(｡ì _ í｡)"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }
        ]))
        elif id == "1187710717":
            img = Image.open(f"src/static/image/sjn.jpg").convert('RGBA')
            await fan.send(Message([
                {
                    "type": "text",
                    "data": {
                        "text": "收到٩(๑•̀ω•́๑)۶\n今天的老干部不省钱了吗(⊙o⊙)"
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                    }
                }
            ]))
        elif id == "1516077112":
            await fan.send("收到٩(๑•̀ω•́๑)۶\n主人贴贴(˶╹ꇴ╹˶）")
        elif id == "1350165753":
            await fan.send("收到٩(๑•̀ω•́๑)۶\n米浴，我好喜欢你啊（♡▽♡）")
        else:
            await fan.send("收到٩(๑•̀ω•́๑)۶")


tietie = on_command("BrBot贴贴")
@tietie.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    img = Image.open(f"src/static/image/l.jpg").convert('RGBA')
    img1 = Image.open(f"src/static/image/害怕.jpg").convert('RGBA')
    if id == "1516077112":
        await tietie.send(Message([
                {
                    "type": "at",
                    "data": {
                        "qq": f"{id}"
                    }
                },
                {
                    "type": "text",
                    "data": {
                        "text": "主人贴贴(˶╹ꇴ╹˶）"
                    }
                }
        ]))
    elif id == "3223196324":
        await tietie.send(Message([
            {
                "type": "at",
                "data": {
                    "qq": f"{id}"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "别靠近我啊，死变态！(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img1), encoding='utf-8')}"
                }
            }
        ]))
    else:
        await tietie.send(Message([
            {
                "type": "at",
                "data": {
                    "qq": f"{id}"
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "爪巴"
                }
            },
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }
        ]))


gacha = on_command("BrBot抽卡")
@gacha.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    if os.path.isfile(f"src/static/account/{id}.txt"):
        rd = random.randint(1, 40)
        f = open(f"src/static/account/tj/{id}.txt", "r", encoding='utf-8', errors='ignore')
        tj = f.read().strip()
        f.close()
        f = open(f"src/static/account/tj1/{id}.txt", "r", encoding='utf-8', errors='ignore')
        tj1 = f.read().strip()
        f.close()
        if rd >= 9:
            f = open(f"src/static/account/tj/{id}.txt", "w")
            f.write(f"{int(tj)+1}")
            f.close()
            f = open(f"src/static/account/tj1/{id}.txt", "w")
            f.write(f"{int(tj1) + 1}")
            f.close()
            await gacha.send("没有抽到捏(๑ŏ ﹏ ŏ๑)")
        else:
            img = Image.open(f"src/static/gacha/{rd}.jpg").convert('RGBA')
            f = open(f"src/static/gacha/{rd}.txt", "r",encoding='utf-8', errors='ignore')
            txt = f.read()
            f.close()
            f = open(f"src/static/account/{id}.txt", "r", encoding='utf-8', errors='ignore')
            qwq = f.read().strip().split(" ")
            f.close()
            f = open(f"src/static/account/{id}.txt", "a")
            j = 1
            for i in qwq:
                if i == f'{rd}':
                    j = 0
            if j == 1 :
                f.write(f" {rd}")
            f.close()
            f = open(f"src/static/account/tj1/{id}.txt", "w")
            f.write(f"{int(tj1) + 1}")
            f.close()
            await gacha.finish([{
                    "type": "at",
                    "data": {
                        "qq": f"{id}"
                    }
                },
                {
                    "type": "text",
                    "data": {
                        "text": f"恭喜你抽到了\n\n{txt}"
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }])
    else:
        await search.send("请先输入“BrBot注册”指令注册(๑ŏ ﹏ ŏ๑)")


rgt = on_command("BrBot注册")
@rgt.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    if os.path.isfile(f"src/static/account/{id}.txt"):
        await rgt.send("该用户已注册")
    else:
        f = open(f"src/static/account/{id}.txt", "a")
        f.write("0")
        f.close()
        f = open(f"src/static/account/tj/{id}.txt", "a")
        f.write("0")
        f.close()
        f = open(f"src/static/account/tj1/{id}.txt", "a")
        f.write("0")
        f.close()
        await rgt.send("收到٩(๑•̀ω•́๑)۶")


search = on_command("图鉴查询")
@search.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    if os.path.isfile(f"src/static/account/{id}.txt"):
        f = open(f"src/static/account/{id}.txt", "r")
        qwq = f.read().strip().split(" ")
        for i in qwq:
            for j in range(1,8):
                if int(i) == j:
                    f = open(f"src/static/gacha/{j}.txt", "r", encoding='utf-8', errors='ignore')
                    txt = f.read()
                    f.close()
                    f = open("src/static/tj.txt", "a")
                    f.write(f"id{j}: {txt}\n")
                    f.close()
        f = open("src/static/tj.txt", "r", encoding='gbk', errors='ignore')
        tj = f.read()
        f.close()
        f = open("src/static/tj.txt", "w")
        f.write("")
        f.close()
        f = open(f"src/static/account/tj/{id}.txt", "r", encoding='utf-8', errors='ignore')
        tj0 = f.read().strip()
        f.close()
        f = open(f"src/static/account/tj1/{id}.txt", "r", encoding='utf-8', errors='ignore')
        tj1 = f.read().strip()
        f.close()
        await search.finish([{
            "type": "text",
            "data": {
                "text": f"图鉴如下\n{tj}\n共计抽卡{tj1}次，有{tj0}次没有抽到"
            }
        }])
    else:
        await search.send("请先输入“BrBot注册”指令注册(๑ŏ ﹏ ŏ๑)")


roll = on_command("roll.")
@roll.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    rd = random.randint(1,100)
    argv = str(event.get_message()).strip().split(".")
    num = int(argv[1])
    if num <= 50:
        ifn = 100
    else:
        ifn = 96
    if rd == 1:
        text = "大成功"
    elif rd >= ifn:
        text = "大失败"
    elif rd >num:
        text = "失败"
    elif rd <= num and rd > num/2:
        text = "成功"
    elif rd <= num/2 and rd > num/5:
        text = "困难成功"
    elif rd <= num/5:
        text = "极难成功"
    await roll.send(f"{argv[0]}检定为{rd}/{num}, {text}")


choose = on_command("choose.")
@choose.handle()
async def _(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    argv = str(event.get_message()).strip().split(".")
    lenth = len(argv)
    f = open("src/static/choose.txt", "w")
    f.write(":")
    f.close()
    for i in range(0,lenth):
        f = open("src/static/choose.txt","a")
        f.write (f" {argv[i]}")
        f.close()
    rd = random.randint(0, lenth-1)
    f = open("src/static/choose.txt", "r")
    text = f.read()
    f.close()
    await choose.send(f"建议从{text}中选择{argv[rd]}呢")


rdtt = on_command("随机贴贴")
@rdtt.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1,24)
    id = str(event.get_user_id())
    f = open(f"src/static/rdtt/{rd}.txt", "r",encoding='utf-8', errors='ignore')
    text = f.read()
    f.close()
    img = Image.open(f"src/static/rdtt/{rd}.jpg").convert('RGBA')
    if id == "1516077112":
        txt = f"主人和{text}贴贴\n(๑´∀`๑)"
    else:
        if rd <= 4:
            txt = f"这是主人的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        elif rd == 15:
            if id == "3223196324":
                txt = "阿贤和老婆贴贴\n(๑´∀`๑)"
            else:
                txt = f"这是阿贤的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        elif rd == 17:
            if id == "1187710717":
                txt = "老干部和老婆贴贴\n(๑´∀`๑)"
            else:
                txt = f"这是老干部的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        elif rd == 18:
            if id == "2924272643":
                txt = "拉卡和老婆贴贴\n(๑´∀`๑)"
            else:
                txt = f"这是拉卡的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        elif rd == 20:
            if id == "287849328":
                txt = "摸鱼和老婆贴贴\n(๑´∀`๑)"
            else:
                txt = f"这是摸鱼的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        elif rd == 22:
            if id == "1344128076":
                txt = "机破和老婆贴贴\n(๑´∀`๑)"
            else:
                txt = f"这是机破的老婆，你不许贴贴\n(งᵒ̌皿ᵒ̌)ง⁼³₌₃"
        else:
            txt = f"和{text}贴贴\n(๑´∀`๑)"
    await rdtt.finish([{
            "type": "at",
            "data": {
                "qq": f"{id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": f"{txt}"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
        }
    }])


async def _group_recall(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "group_recall")
    return value


recall = on_notice(rule=_group_recall, priority=10, block=True)
@recall.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1,2)
    if rd == 1:
        txt = "女装了就该给大家看看，让兄弟们爽一下，你撤回干啥"
    elif rd == 2:
        txt = "你要是嫖娼进局子了就跟大家说，大家帮你想办法，你撤回干啥"
    await recall.send(f"{txt}")


'''async def _group_image(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.get_message == {"type":"image","data":{"file":"e955e928e6524f681d88c4f659036230.image"}})
    return value

sp = on_notice(rule=_group_image, priority=10, block=True)
@sp.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1, 2)
    if rd == 1:
        txt = "帝宝快把你家阿贤锁在地下室，别让他出来沾花惹草"
    elif rd == 2:
        txt = "天天老婆老婆，爪巴"
    await recall.send(f"{txt}")'''


jzm = on_command("+1s")
@jzm.handle()
async def _(bot: Bot, event: Event, state: T_State):
    f = open(f"src/static/jzm.txt", "r",encoding='utf-8', errors='ignore')
    text = f.read()
    f.close()
    text0 = int(f"{text}") + 1;
    f = open(f"src/static/jzm.txt", "w")
    f.write(f"{text0}")
    f.close()
    id = str(event.get_user_id())
    rd = random.randint(1, 5)
    if rd == 1:
        text1 = "祝你闷声发大财"
    elif rd == 2:
        text1 = "你们给我搞的这个东西啊，exciting！"
    elif rd == 3:
        text1 = "你这个意识觉悟，不知道高到哪里去了"
    elif rd == 4:
        text1 = "这就是坠吼的"
    elif rd == 5:
        text1 = "你以后吃华莱士必不会喷射"
    await jzm.finish([{
        "type": "at",
        "data": {
            "qq": f"{id}"
        }
    },
        {
            "type": "text",
            "data": {
                "text": f"{text1}\n\n目前累计续了{text0}秒"
            }
        }])


rdjj = on_command("随机击剑")
@rdjj.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd1 = random.randint(1, 13)
    rd2 = random.randint(1, 13)
    if rd1 == 1:
        text1 = "老干部"
    elif rd1 == 2:
        text1 = "阿贤"
    elif rd1 == 3:
        text1 = "摸鱼"
    elif rd1 == 4:
        text1 = "mio"
    elif rd1 == 5:
        text1 = "br"
    elif rd1 == 6:
        text1 = "DRP"
    elif rd1 == 7:
        text1 = "拉卡"
    elif rd1 == 8:
        text1 = "机破"
    elif rd1 == 9:
        text1 = "K老师"
    elif rd1 == 10:
        text1 = "米浴"
    elif rd1 == 11:
        text1 = "四哈人"
    elif rd1 == 12:
        text1 = "阿船"
    elif rd1 == 13:
        text1 = "谭晓阳"
    if rd2 == 1:
        text2 = "老干部"
    elif rd2 == 2:
        text2 = "阿贤"
    elif rd2 == 3:
        text2 = "摸鱼"
    elif rd2 == 4:
        text2 = "mio"
    elif rd2 == 5:
        text2 = "br"
    elif rd2 == 6:
        text2 = "DRP"
    elif rd2 == 7:
        text2 = "拉卡"
    elif rd2 == 8:
        text2 = "机破"
    elif rd2 == 9:
        text2 = "K老师"
    elif rd2 == 10:
        text2 = "米浴"
    elif rd2 == 11:
        text2 = "四哈人"
    elif rd2 == 12:
        text2 = "阿船"
    elif rd2 == 13:
        text2 = "谭晓阳"
    await rdjj.finish([
        {
            "type": "text",
            "data": {
                "text": f"下面有请{text1}和{text2}击剑"
            }
        }])


lion = on_command("狮")
@lion.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(" ", 1)
    id = str(event.get_user_id())
    time0 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    qwq = 0
    if argv[0] == "几":
        f = open("src/static/number/lion/lion.txt","r")
        qwq = f.read()
        f.close()
        f = open("src/static/number/lion/time.txt", "r")
        time = f.read()
        f.close()
        await lion.send(f"狮 {qwq}\n上次更新于{time}")
    elif is_number(argv[0]):
        f = open("src/static/number/lion/lion.txt", "w")
        f.write(argv[0])
        f.close()
        f = open("src/static/number/lion/time.txt", "w")
        f.write(time0)
        f.close()
        await lion.send("收到٩(๑•̀ω•́๑)۶")


rdgh = on_command("随机怪话")
@rdgh.handle()
async def _(bot: Bot, event: Event, state: T_State):
    rd = random.randint(1, 24)
    id = str(event.get_user_id())
    img = Image.open(f"src/static/rdgh/{rd}.jpeg").convert('RGBA')
    await rdgh.finish([{
        "type": "at",
        "data": {
            "qq": f"{id}"
        }
    },
        {
            "type": "image",
            "data": {
                "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
            }
        }])


rddy = on_command("roll")
@rddy.handle()
async def _(bot: Bot, event: Event, state: T_State):
    i = 0
    id = str(event.get_user_id())
    argv = str(event.get_message()).strip().split(".")
    if argv[0] == "dy":
        for j in range(0,i):
            if id == ids[j]:
                txt = "cnssm"
            else:
                rd = random.randint(1, 3)
                ids[i] = id
                dim[i] = rd
                i=i+1
                if i == 3:
                    txt = f"{dim[0]},{dim[1]},{dim[2]}"
    await rddy.finish([
        {
            "type": "text",
            "data": {
                "text": f"{txt}"
            }
        }])

