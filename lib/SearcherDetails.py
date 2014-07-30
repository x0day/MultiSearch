#coding=utf-8
__author__ = 'DM'

################################################################
#保存了每一个搜索使用的来源url和匹配链接的正则表达式.               #
#MultiSearch ver 2.0 FileName:SearcherDetails.py               #
################################################################
SearcherDetails = dict()
############################################## Headers #################################################################
#如果有需要 请在这里修改.

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'gb18030,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'
}

###Bing
SearcherDetails["Bing"] = dict()
SearcherDetails["Bing"]["SearchUrl"] = lambda SearchStr,Page: "http://cn.bing.com/search?q={0:s}&first={1:d}1&FORM=PERE".format(SearchStr,Page - 1)
SearcherDetails["Bing"]["UrlRegex"] = r'<li class="sa_wr">[\s\S]+?<h3><a href="([\s\S]+?)"[\s\S]+?</a></h3>[\s\S]+?</li>'



#Google
SearcherDetails["Google"] = dict()
SearcherDetails["Google"]["SearchUrl"] = lambda SearchStr,Page: "http://203.208.46.176/search?q={0:s}&start={1:d}00&num=100".format(SearchStr, Page)
SearcherDetails["Google"]["UrlRegex"] = r'<li class="g">[\s\S]+?href="([\s\S]+?)"[\s\S]+?</li>'

#Baidu
SearcherDetails["Baidu"] = dict()
SearcherDetails["Baidu"]["SearchUrl"] = lambda SearchStr,Page: "http://www.baidu.com/s?wd={0:s}&pn={1:d}00&ie=utf-8&rn=10".format(SearchStr, Page)
SearcherDetails["Baidu"]["UrlRegex"] = r'<h3 class="t">[\s\S]*?href="([\s\S]+?)"[\s\S]+?</h3>'

#Jike
SearcherDetails["Jike"] = dict()
SearcherDetails["Jike"]["SearchUrl"] = lambda SearchStr,Page: "http://www.jike.com/so?q={0:s}&page={1:d}".format(SearchStr, Page)
SearcherDetails["Jike"]["UrlRegex"] = r'_dom_name="\d">[\s\S]+?div class="T1"><a href="([\s\S]+?)"'



#Sogou
SearcherDetails["Sogou"] = dict()
SearcherDetails["Sogou"]["SearchUrl"] = lambda SearchStr,Page: "http://www.sogou.com/web?query={0:s}&page={1:d}&num=100".format(SearchStr, Page)
SearcherDetails["Sogou"]["UrlRegex"] = r'id="uigs_d0_\d{1,2}" href="([\s\S]+?)"'

#So360
SearcherDetails["So360"] = dict()
SearcherDetails["So360"]["SearchUrl"] = lambda SearchStr,Page: "http://www.so.com/s?ie=utf-8&q={0:s}&pn={1:d}".format(SearchStr, Page)
SearcherDetails["So360"]["UrlRegex"] = r'<h3 class="res-title ">[\s]+?<a href="([\s\S]+?)"'

