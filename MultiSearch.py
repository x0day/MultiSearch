#coding=utf-8
__author__ = 'DM_'
from lib.Searchers import baiduSearch,bingSearch,so360Search,sogouSearch,googleSearch,jikeSearch
from lib.printers import printRed,printPink
import lib.Argvs
from lib.SaveLog import SaveLog
import time
ArgsDict = lib.Argvs.ArgsDict
Search_All_Status = lib.Argvs.Search_All_Status
Search_None_Status = lib.Argvs.Search_None_Status

__SearchersList = dict(baidu=baiduSearch,
                       google=googleSearch,
                       bing=bingSearch,
                       so360=so360Search,
                       sogou=sogouSearch,
                       jike=jikeSearch)

def __DoJob():
    """
函数主程序,主要对命令行参数进行判断并执行相关命令.

    """
#    global OutUrls
    OutUrls = []
    for key in ArgsDict:
        if Search_All_Status or type(ArgsDict['search_all']) is int:  # ArgsDict['search_all'] and
            SearchStr = ArgsDict['dork'][0]
            SearchPages = ArgsDict['search_all']
            print "[+]Use all search options."
            printPink("[+]Search Keyword: %s,Search Pages: %s.(None is all)" %(SearchStr, str(SearchPages)))
            for Searcher in __SearchersList:
                printPink("\n[!]Searching at:%s" % str(Searcher))
                Searcher = __SearchersList[Searcher](SearchStr,SearchPages)
                Searcher.GetUrls()
                OutUrls.extend(Searcher.Urls)
            break

        elif ArgsDict['search_all'] is None:
            printRed("[-]--search-all cannot use with other search options.\n")
            break

        elif not (ArgsDict['search_all'] is None) and ArgsDict[key] is not False and key not in ['regex', 'search_all', 'dork','logfile']:
            SearchPages = ArgsDict[key]
            SearchStr = ArgsDict['dork'][0]
            if SearchPages:
                printPink("[+]Options:%s,Page's amounts: %d." % (key, SearchPages))
            else:
                printPink("[+]Options:%s,Page's amounts: all." %key)
            Searcher = __SearchersList[key](SearchStr,SearchPages)
            Searcher.GetUrls()
            OutUrls.extend(Searcher.Urls)

        elif not Search_All_Status and Search_None_Status: # not ArgsDict['search_all']
            printRed('[-]Please specify a search term,or use --search-all to search with all search options.\n')
            break
    return OutUrls

if __name__ == '__main__':
    print "\n\n[!]Start at time: %s\n\n" % time.ctime()
    StartTime = time.time()
    OutUrls = __DoJob()
    LogFilePath = ArgsDict['logfile']
    if ArgsDict['regex']:
        Regex = ArgsDict['regex'][0]
    else:
        Regex = False
    if OutUrls:
        printPink(u"\n\n[!]最终获取到了%d条链接." % len(OutUrls))
        OutUrls = list(set(OutUrls))
        printPink(u"[!]去重后得到了%d条链接.\n" % len(OutUrls))
        SaveLog(OutUrls,LogFilePath,Regex)
    print "\n\n[!]Done at time:",time.ctime()
    print u"[!]总共耗时%d秒." % int(time.time() - StartTime)

