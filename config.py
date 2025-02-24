# -*- coding: utf-8 -*-
import os
from mUtils.datetimeUtil import TimeUtil

# 导出Excel路径,默认file
FILE_PATH = './file/' + TimeUtil().get_chinesedate() + '/'

def check_path():
    if not os.path.exists('./file/'+ TimeUtil().get_chinesedate()):
        os.mkdir('./file/'+ TimeUtil().get_chinesedate())

# 需要监控的歌曲列表 (歌名+演唱者)
SONGS = [
    ['你要的全拿走', '胡彦斌'],
    ['MV不必在乎我是谁 (Live)', '胡彦斌'],
    ['月光', '胡彦斌'],
    ['红颜', '胡彦斌'],
    ['还魂门', '胡彦斌'],
    ['还为你我受冷风吹', '胡彦斌'],
    ['干脆忘了你', 'xx'],
    ['超级公主', 'xx'],
    ['青梅信札', '冯提莫'],
    ['分手加时赛', 'xxx'],
    ['你大可不必', 'xxx'],
    ['娘子我错了', 'xxx'],
    ['全部的骄傲来自你', 'xxx'],
    ['要你管', '杜淳'],
    ['红黑', '周杰伦']
]

# 飞书 通过webhook将自定义服务的消息推送至飞书
# WEB_HOOK_URL = r'https://open.feishu.cn/open-apis/bot/v2/hook/de4e7d58-4a59-42fc-bc25-4b59e1f137d4'
