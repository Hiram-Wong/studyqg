# 每日强国『学习强国助手』◕‿-｡

# 吉祥物护法『来源于网络，如侵权联系删除』 ｡◕‿◕｡

```python
　　  へ　　　　／|
　　/＼7　　   / ／
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　ｲ●　､　●　　⊂⊃〈　　/
　()　 へ　　　　|　＼〈
　　>ｰ ､_　 ィ　 │ ／／
　 / へ　　 /　ﾉ＜| ＼＼
　 ヽ_ﾉ　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`ｰ―＿_|

^^^^^^^^^^^^^^^^^^^^^^^^^^^
    皮卡丘护法  永无BUG

```

# 项目依赖

1. 小程序『含微信小程序 && QQ小程序』，组件采用[colorui组件库](https://github.com/weilanwl/ColorUI)
2. 后端 开发了Flask和Django两个版本『均基于Python』
3. 题库来源于[XXQG-TiaoZhanDaTi-TiKu](https://github.com/JiangZY5959/XXQG-TiaoZhanDaTi-TiKu/blob/master/README.md) ✌ 目前数据库数据整理至2020年3月23日 共1416
4. Python自动化基于Airtest开发

* Python自动化实现了学习强国自动登录，开发这个的初衷是由于本人上线了小程序，有用户给作者留言『聊天记录如下』

![用户留言](https://img02.sogoucdn.com/app/a/100520146/c9b10424855735273766e40dc153a2a3)

1. 下载`Airtest`工具，usb连接手机并开启开发者模式中的usb调试模式『据说还可以无线模式』『目前只限安卓（可使用模拟器，作者就是使用的模拟器开发），因为苹果需要开发者账号且需要付费，如果有好心人提供的话 也不是不可以』
2. 只需要将批量的账号密码填入`accounts.txt`,每个行号一行账号密码种用`#`分隔，最后一个账号需要回车留空白行，否则最后一个账号无法登录
3. Run

* Flask版本

1. P.s: Flask只开发了前端搜索『光年模板+Vue.js+axios』·api接口,无后台
2. 依赖第三方库『flask，pymysql，flask_cors』
![Search](https://ae01.alicdn.com/kf/Hda2271596a7e4edab8357c5ddc701f3cW.png)

* Django版本

1. P.s: Django开发了前端搜索『光年模板+Vue.js+axios』·api接口和后台管理『采用[simpleui主题](https://github.com/newpanjing/simpleui)』,支持Banner·题库·开发日志的修改
2. 依赖第三方库『django，django-cors-headers,django-simpleui』
3. 后台预览
![Search](https://ae01.alicdn.com/kf/Hda2271596a7e4edab8357c5ddc701f3cW.png)
![Home](https://ae01.alicdn.com/kf/Hdf5ae107b55b4e08b4d275d74edabd1cF.png)
![Banner](https://ae01.alicdn.com/kf/Hd69b9332bb6842baa401d1d9fa259060j.png)
![QuestionLib](https://ae01.alicdn.com/kf/H7dec88f2857546579fd3d67ac9785258r.png)
![QuestionLib-edit](https://ae01.alicdn.com/kf/H180d8cb4814a48b787ccd0e805d83785Z.png)
![Log](https://ae01.alicdn.com/kf/H7780b99381d64d358dd4e11f78d32b53e.png)

# 预览

[前端搜索](https://xuexi.catni.cn)

![微信小程序](https://ae01.alicdn.com/kf/H3824bf27301e460c9f97e0fc11069d25Z.png)
![QQ小程序](https://ae01.alicdn.com/kf/Hd455a251f2e24ec6bedf82443f6896fcf.png)
