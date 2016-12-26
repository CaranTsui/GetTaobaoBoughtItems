# 获取淘宝——已买到的宝贝页面当中所有订单信息
淘宝买家现在不可以直接下载订单信息了，只能去支付宝下载账单，很不方便。后面想了一下，干脆直接爬虫爬下来吧。
本来想着用selenium直接定位元素的，结果我还是放弃了，只能去翻我最不熟悉最不懂的正则表达式。

截止2016-12-26，已买到的宝贝的页面中的宝贝信息都是由一段类似的代码构成的,无论是初次加载,还是在点击上一页/下一页的时候获得。所以可以使用正则表达式获得相关内容。
但是获取内容我暂时还是只能用手工获得了。登录以及cookie好麻烦orz...

一些关键字：

一、 订单总信息：
- 订单日期：createDay
- 订单号：id
- 相关费用：bpostFees
   - 含邮费：\u542b\u8fd0\u8d39
- 商铺名称：shopName

二、 订单明细
- itemInfo
- 商品类别：skuText name value
- 商品名称：title
- 价格与实际价格：priceInfo realTotal
- 数量：quantity


感谢以下的一些科普文章/网站工具等，排名不分先后

1. [正则表达式30分钟入门](http://deerchao.net/tutorials/regex/regex.htm)

2. [runoob - 正则表达式教程](http://www.runoob.com/regexp/regexp-tutorial.html)

3. [python 2.7 Doc - re Module](https://docs.python.org/2.7/library/re.html?highlight=re#search-vs-match)

4. [伯乐在线 - Python爬虫实战（5）：模拟登录淘宝并获取所有订单](http://python.jobbole.com/81361/) 

特别感谢1和4的两位作者，4是启发我用正则表达式去获取订单记录的源头，虽然这位作者的代码已经不适用，但是还是很感谢他。1则是一个非常完整通俗易懂的正则表达式入门的文档，基本上我就是在完整阅读了文档之后（真的大约是30分钟的样子），然后自己动手慢慢写慢慢验证，这位作者还提供了一个.NET的正则表达式测试工具，正是这个工具以及runoob网站的工具帮我完整地写出了我所需要的正则。
