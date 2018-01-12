#encoding=utf-8
'''
Created on 2018年1月9日

@author: aadebuger
'''
import os
import sys
from git import Repo
import pystache
def isDir(item):
    if item.startswith("."):
        return False
    else:
        if item.endswith(".txt"):
            return False
        else:
            return True
def buildsh(dir):
        dirs = os.listdir(dir)
        gitdir =filter(isDir,dirs)
        urlv = map(lambda name: lsdir(dir,name),gitdir)
        print("urlv",urlv)
        return urlv
def lsdir(dir,name):
        print("dir",dir)
        print("name",name)
        repo=Repo(dir+"/"+ name)
        master = repo.remotes
#        print("repo.remotes.origin.url",repo.remotes.origin.url)
        for item in master:
            print item.urls
            for item1 in item.urls:
                print item1
                return item1
def outputShell(urlv):
        templatestr="""{{#repo}}
git clone {{name}}
{{/repo}}
"""
        arrayv = map(lambda item: {'name':item},urlv)
        print pystache.render(templatestr, {'repo': arrayv})
        
if __name__ == '__main__':
    if len(sys.argv)==1:
        dirs= buildsh("/Users/aadebuger/Ext/github/docker-ros/moveittutorial/codews/src")
    else:
        dirs=buildsh(sys.argv[1])
    print(dirs)
    outputShell(dirs)
