#coding=utf-8
import argparse

__HELP_INFO = u"""
eg: \n%(prog)s --search-all -d "python" --regex '*\.doc|*\.pdf' --logfile Python_docs.txt
    \n%(prog)s --baidu 4 --google 2 --bing --regex '*\.doc|*\.pdf' --logfile Python_docs.txt
    \n搜索选项后跟的是搜索页数.--search-all 后跟搜索页数表示获取全部搜索的前几页.
    \n--regex 就是自定义的正则表达式了.
"""

global Search_All_Status,Search_None_Status

__parser = argparse.ArgumentParser(epilog=__HELP_INFO,formatter_class=argparse.RawDescriptionHelpFormatter)

__parser.add_argument("-b", "--baidu",
                      action="store",
                      nargs='?',
                      type=int,
                      default=False)

__parser.add_argument("-s", "--sogou",
                      action="store",
                      nargs='?',
                      type=int,
                      default=False)

__parser.add_argument("-j", "--jike",
                      action="store",
                      nargs='?',
                      type=int,
                      default=False)

__parser.add_argument("-bi", "--bing",
                      action="store",
                      nargs='?',
                      type=int,
                      default=False)

__parser.add_argument("-g","--google",
                      action="store",
                      nargs='?',
                      default=False,
                      type=int)

__parser.add_argument("-so","--so360",
                      action="store",
                      nargs='?',
                      default=False,
                      type=int)

__parser.add_argument("-r", "--regex",
                      nargs=1,
                      action="store",
                      default=False)

__parser.add_argument("-d","--dork",
                      nargs=1,
                      action="store",
                      required=True,
                      default=False)

__parser.add_argument("--search-all",
                        default=False,
                        nargs='?',
                        action="store",
                        type=int)

__parser.add_argument("-l", "--logfile",
                        action="store",
                        type=str,
                        default=False)

__Args = __parser.parse_args()
ArgsDict = __Args.__dict__

def Search_All_Status_Check(ArgsDict):
    if ArgsDict['search_all'] is None:
        global Search_All_Status
        for key in ArgsDict:
            if ArgsDict[key] is not False and key not in ['regex', 'search_all', 'dork','logfile']:
                Search_All_Status = False
                break
            else:
                Search_All_Status = True
    else:
        Search_All_Status = False


def Search_None_Status_Check(ArgsDict):
    global Search_None_Status
    for key in ArgsDict:
        if ArgsDict[key] is False and key not in ['regex', 'search_all', 'dork', 'logfile']:
            Search_None_Status = True
        #            break
    for key in ArgsDict:
        if ArgsDict[key] is not False and key not in ['regex', 'search_all', 'dork', 'logfile']:
            Search_None_Status = False
#            break



Search_All_Status_Check(ArgsDict)
Search_None_Status_Check(ArgsDict)

def __DoJob():
    for key in ArgsDict:
        if Search_All_Status or type(ArgsDict['search_all']) is int:  # ArgsDict['search_all'] and
            print "Do All Job."
            break

        elif ArgsDict['search_all'] is None:
            print "search-all cannot use with others."
            break

        elif not ArgsDict['search_all'] and ArgsDict[key] is not False and key not in ['regex', 'search_all', 'dork','logfile']:
            print key, ArgsDict[key]

        elif not Search_All_Status and not Search_None_Status: # not ArgsDict['search_all']
            print 'error 1'
            break
    print '============='
    print 'Search_None_Status',Search_None_Status
    print 'Search_All_Status',Search_All_Status
    print '-------------'
    print ArgsDict

def DoJob():
    for key in ArgsDict:
        if Search_All_Status or type(ArgsDict['search_all']) is int:  # ArgsDict['search_all'] and
            print "Do All Job."
            break

        elif (ArgsDict['search_all'] is None):
            print "search-all cannot use with others."
            break

        elif not (ArgsDict['search_all'] is None) and ArgsDict[key] is not False and key not in ['regex', 'search_all', 'dork','logfile']:
            print key, ArgsDict[key]

        elif not Search_All_Status and Search_None_Status: # not ArgsDict['search_all']
            print 'error 1'
            break
    print '============='
    print 'Search_None_Status',Search_None_Status
    print 'Search_All_Status',Search_All_Status
    print '-------------'
    print ArgsDict

if __name__ == '__main__':
    DoJob()