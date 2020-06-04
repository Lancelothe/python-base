## 百度网盘多文件下载教程

1. 利用`BaiduExporter`导出需要下载文件的下载链接文本，由于Mac系统不支持IDM，所以我选择用`Neat Download Manager`逐一下载。
2. 执行` python selenium-download.py `利用`selenium`模拟浏览器操作，唤起`Neat Download Manager`的Chrome插件，以下载相应文件。


> 比较low的使用轮询的办法逐一下载，因为`Neat Download Manager`好像没办法触发多个网盘文件的下载，不然下载链接打开会报网盘的错误。


** 参考 **  
[c\# \- How to open a Chrome Profile through \-\-user\-data\-dir argument of Selenium \- Stack Overflow](https://stackoverflow.com/questions/50635087/how-to-open-a-chrome-profile-through-user-data-dir-argument-of-selenium/50637211#50637211)  
[python \- InvalidArgumentException: Message: invalid argument: user data directory is already in use error using \-\-user\-data\-dir to start Chrome using Selenium \- Stack Overflow](https://stackoverflow.com/questions/59987080/invalidargumentexception-message-invalid-argument-user-data-directory-is-alre)

