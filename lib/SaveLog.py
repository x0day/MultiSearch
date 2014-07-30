#coding=GBK
__author__ = 'DM_'
import os,re,time

def __WriteFile(SaveUrls, FilePath, Regex=False):
    if Regex:
        LogFile = open(FilePath, "a")

        for url in SaveUrls:
            if re.findall(Regex, url):
#                url = re.findall(Regex, url)
#                LogFile.write(url[0] + '\n')
                LogFile.write(url + '\n')

        print(u"文件已保存在 %s" % FilePath)
    else:
        LogFile = open(FilePath, "a")
        for url in SaveUrls:
            LogFile.write(url + '\n')
        print(u"文件已保存在指定文件中,路径是 %s." % FilePath)

def SaveLog(SaveUrls,FilePath,Regex=False):
    DefaultFilePath = "output\\%s_LogUrls" % str(time.strftime('%Y-%m-%d-%S',time.localtime(time.time())))

    if FilePath is False:
        FilePath = DefaultFilePath + "_Default.txt"

    if Regex is False:
            if os.path.exists(FilePath):
                print(u"[!]文件已存在,是否覆盖?[y/n]")
                Fj = raw_input()
                if Fj == 'y' or Fj == '':
                    __WriteFile(SaveUrls, FilePath)
                else:
                    __WriteFile(SaveUrls,DefaultFilePath + "_RAW.txt")
            else:
                __WriteFile(SaveUrls, FilePath)

    else:
        print(u"发现有正则选项.是否进行结果备份文件?[y/n]")
        Fj = raw_input()
        if Fj == 'y' or Fj == '':
            BakFilePath = raw_input("请输入备份文件地址:")
            try:
                __WriteFile(SaveUrls, BakFilePath)
            except:
                print(u"文件创建失败,将写入默认记录文件.LogUrls_bak.txt")
                __WriteFile(SaveUrls, DefaultFilePath + "_BAK.txt")
        else:
            if os.path.exists(FilePath):
                print(u"[!]将写入正则的匹配文件已存在,是否覆盖?[y/n]")
                Fj = raw_input()
                if Fj == 'y' or Fj == '':
                    __WriteFile(SaveUrls, FilePath, Regex)
                else:
                    __WriteFile(SaveUrls, (DefaultFilePath + "_regex.txt"),Regex)
            else:
                __WriteFile(SaveUrls, FilePath, Regex)
