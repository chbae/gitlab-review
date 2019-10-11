#!/usr/bin/env python

import sys
import json
import gitlab

def main(uri):
    gl = gitlab.Gitlab.from_config('swfactory', ['/Users/chanbae/gitlab/gitlab.cfg'])
    try:
        gl.auth()
    except Exception as ex:
        print('Error: ', ex)

    url = uri.split('/')
    prj = gl.projects.get(url[3]+'/'+url[4])
    mr = prj.mergerequests.get(url[6])

    print("\033[1;35;40m============================================== MR ==================================================\033[1;37;40m")
    print("\033[1;34;40mFrom (%s): \033[1;37;40m%s/%s/tree/%s" % (
        mr.attributes['author']['name'],
        mr.attributes['author']['web_url'],
        url[4],
        mr.attributes['source_branch']))
    print("\033[1;34;40mTitle:\033[1;37;40m %s" % ( mr.attributes['title']))

    commits = mr.commits()

    count = 0
    print("\033[1;35;40m============================================= COMMITS ===============================================\033[1;37;40m")
    for commit in commits:
        print("\033[1;35;40m[%d] START -------------------------------------------------------------------------------------------\033[1;37;40m" % count)
        print("\033[1;34;40mcommit title (%d): \033[1;37;40m%s" % (len(commit.title), commit.title))
        print("\033[1;34;40mcommit id: \033[1;37;40m%s" % (commit.id))
        print("\033[1;34;40mcommit message:\033[1;37;40m\n%s" % (commit.message))
        diff = commit.diff()
        print("\033[1;34;40mcommit diff:\033[1;37;40m\n%s" % (diff[0]['diff']))
        print("\033[1;35;40m[%d] END ---------------------------------------------------------------------------------------------\033[1;37;40m" % count)
        print("\n")
        count = count + 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Please add url"
