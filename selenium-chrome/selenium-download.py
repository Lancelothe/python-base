# coding=utf-8
import os
import time
import urllib.parse
from queue import Queue

from selenium import webdriver

queue = Queue()
PATH = '/Users/lancelot/Downloads/'
URL = 'https://pan.baidu.com/disk/home'


def read_file_to_queue(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            queue.put(line.strip('\n'))


def launchChrome():
    # 启用带插件的浏览器
    option = webdriver.ChromeOptions()
    # chrome://version 查看用户数据缓存目录
    option.add_argument(r"--user-data-dir=/Users/lancelot/Library/Application Support/Google/Chrome/Profile 1")
    option.add_extension("/Users/lancelot/PycharmProjects/python-base/selenium-chrome/NeatDownloadManager-1.4.0.crx")
    # 无痕模式
    # option.add_argument("--incognito")
    # option.add_argument(r"--user-data-dir=/Users/lancelot/Library/Application Support/Google/Chrome/")
    # 初始化driver
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', port=0, options=option)
    # Test 打开网站
    # driver.get("https://www.baidu.com")
    driver.get(URL)
    # 最大化窗口
    # driver.maximize_window()
    return driver


def downloadFile(driver):
    while not queue.empty():
        download_url = queue.get()
        real_url_zh_name = urllib.parse.unquote(download_url)
        download_file_name = real_url_zh_name.split('/')
        download_file_name = download_file_name[-1]
        is_file = os.path.exists(PATH + download_file_name)
        if not is_file:
            print("下载: %s" % download_file_name)
            driver.get(download_url)
        else:
            print("文件名: %s, 已存在: %s" % (download_file_name, is_file))
            continue
        while True:
            is_file = os.path.exists(PATH + download_file_name)
            if is_file:
                print("%s 下载完成!  还剩 %s 个文件" % (download_file_name, queue.qsize()))
                break
            else:
                print("%s 下载中......" % download_file_name)
                time.sleep(3)


def main():
    driver = launchChrome()
    # 等待输入账号、密码，第一次是没有缓存的
    time.sleep(3)
    read_file_to_queue('link.txt')
    # 开始下载
    downloadFile(driver)
    driver.close()


if __name__ == '__main__':
    main()
