#!/usr/bin/env python 
#coding = utf-8

import url_manager
import html_downloader
import html_parser
import html_outputer

if __name__ == "__main__":
    urls = url_manager.UrlManager()
    downloader = html_downloader.HtmlDownloader()
    parser = html_parser.HtmlParser()
    outputer = html_outputer.HtmlOutputer()
    
    root_url = 'http://baike.baidu.com/view/125370.htm'
    count = 1
    urls.add_new_url(root_url)
    while urls.has_new_url():
        try:
            new_url = urls.get_new_url()
            print 'craw %d:%s' % (count,new_url)
            html_cont = downloader.download(new_url)

            '''
            with open('first.html','w') as f:
                f.write(html_cont)
            '''
 
            new_urls,new_data = parser.parse(new_url,html_cont)
            urls.add_new_urls(new_urls)
            outputer.collect_data(new_data)
            if count == 1000:
                break
            count = count+1
        except:
            print 'craw failed!'
















