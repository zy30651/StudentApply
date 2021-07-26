import base64
import json
import random
import time
import datetime
import os


def picture_to_base64(path):
    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    return s


def dict_to_json_to_base64(dict_str):
    """
    字典转json字符串，再转Base64编码
    :param dict_str: 字典
    :return: 返回字典的base64编码
    """
    str_json = json.dumps(dict_str)
    return str_to_base64(str_json)


def str_to_base64(char):
    """
    字符串转base64
    :param char:
    :return:b'123af1sdf124'
    """
    bytes_str = char.encode(encoding='utf-8')
    base_str = base64.b64encode(bytes_str)
    return base_str


def base64_to_str(base_str):
    """
    base64转字符串
    :param base_str:
    :return:'zhangyang'
    """
    b_str = base64.b64decode(base_str)
    char = b_str.decode()
    return char


def get_time_stamp():
    """
    获取秒级时间戳
    :return:1515774430
    """
    return int(time.time())


def get_time000_stamp():
    """
    获取毫秒级时间戳
    :return:1515774430000
    """
    return int(round(time.time() * 1000))


def get_time_now():
    """
    获取当前日期时间
    :return:YY-MM-DD HH:MM:SS
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def change_time_to_stamp(time_temp):
    """
    将日期转为秒级时间戳
    :param time_temp:YY-MM-DD HH:MM:SS
    :return:
    """
    return int(time.mktime(time.strptime(time_temp, "%Y-%m-%d %H:%M:%S")))


def change_stamp_to_time(stamp):
    """
    将日期转为秒级时间戳
    :param stamp:
    :return: YY-MM-DD HH:MM:SS
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp))


def change_time_to_time(time_temp):
    """
    时间格式转成另一种时间格式
    :param time_temp:
    :return:2019-08-02 01:00:00
    """
    return datetime.datetime.strptime(time_temp, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')


def change_time_to_struct(time_temp):
    """
    日期转结构体时间struct_time
    :param time_temp:
    :return:
    """
    return time.strptime(time_temp, '%Y-%m-%d %H:%M:%S')


def change_stamp_to_struct(stamp: int):
    """
    时间戳转结构体，注意时间戳要求为int,秒级
    :param stamp:
    :return:
    """
    return time.localtime(stamp)


def change_stamp_to_datetime(stamp: int):
    """
    时间戳转datetime，注意时间戳要求为int,秒级
    :param stamp:
    :return:
    """
    return datetime.datetime.fromtimestamp(stamp).strftime("%Y--%m--%d %H:%M:%S")


def create_random_string(len):
    """
    返回指定长度的随机数字符串
    :param len: 返回字符串长度
    :return:
    """
    raw = ""
    range1 = range(58, 65)
    range2 = range(91, 97)

    i = 0
    while i < len:
        seed = random.randint(48, 122)
        if (seed in range1) or (seed in range2):
            continue
        raw += chr(seed)
        i += 1
    return raw


def create_random_int():
    sn = ''.join(
        str(i).zfill(2) for i in random.sample(range(0, 19), 9))
    return int(sn)




