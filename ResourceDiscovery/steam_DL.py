import cgi
from curses import echo
import functools
import sys
from time import sleep
from tkinter import PIESLICE
from urllib import request
from urllib.parse import urlparse
import aiohttp
import aiofiles
import os
import asyncio
import cchardet as chardet
import magic
from bs4 import BeautifulSoup
from numba import jit
import mimetypes

import requests
import urllib3
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=0'


def find_data_format(content,url,content_type=None,content_encoding=None): 
    
    print("content_type M:",content_type)
    print("content_type len:",len(content_type) )
    if content_type is not None and len(content_type) <= 5:
        content_type=None
    if content_encoding is not None and len(content_encoding) <= 2:
        content_encoding=None
    m_mime_encoding = magic.Magic(mime_encoding=True)
    if content_type is None:
        o = urlparse(url)
        content_type = mimetypes.guess_type(o.path, strict=True)[0]
        print("guess_type",content_type)
    if content_type is None:
        content_type = magic.from_buffer(content, mime=True)
        print("magic",content_type)
    if content_encoding is None:
        mime, options = cgi.parse_header(content_type)
        if "charset" in options.keys():
            content_encoding = options["charset"]
        else:
            content_encoding = chardet.detect(content)['encoding']
    if content_encoding is None:
        content_encoding = m_mime_encoding.from_buffer(content)
    return content,content_encoding,content_type
                            

class ResourceDownloader:
    def __init__(self,url,path = None,name= "", rb=None,session=None,pool=None,filters_in_ext=None,filters_out_ext=None,filters_in_mime=None,mime="") -> None:
        self.url = url
        self.path = path
        self.rb = rb
        self.pool = pool
        self.mime = mime
        self.session=session
        self.filters_in_mime = filters_in_mime
        if path is None :
            task = asyncio.current_task()
            task_name = task.get_name()
            self.path = "./"+task_name+"_"+name+"_" +".temp"
        else:
            self.path = path
            
    
    async def __aenter__(self):
        loop = asyncio.get_running_loop()
        self.check =False
        self.file =None
        mime = self.mime
        text = ""
        encoding = ""
        status = 0
        self.cleanup = False
        
        for i in range(9):
            # filter in  extension 
            url_is_good=True
            if self.filters_in_mime is not None:
                o = urlparse(self.url)
                content_type = mimetypes.guess_type(o.path, strict=True)[0]
                if content_type is not None and len(content_type) > 0:
                    url_is_good=False
                    for filters_in_mime in self.filters_in_mime:
                        if  filters_in_mime in content_type:
                            url_is_good = True
                            break
                if not  url_is_good:
                    print("bad type:",content_type)
                    break
                
            try:
                if self.rb is not None:
                    if not self.rb.can_fetch("*", self.url):
                        break
                    time = self.rb.request_rate("*")
                    if time is not None:
                        await asyncio.sleep(time)
                async with self.session.get(self.url) as response:
                        status = response.status
                        content = await response.content.read()
                        try:
                            mime = response.headers['content-type']
                        except:
                            pass
                        
                        if self.filters_in_mime is not None and len(mime) > 0:
                            url_is_good=False
                            for filters_in_mime in self.filters_in_mime:
                                 if  filters_in_mime in mime:
                                     url_is_good = True
                                     break
                        if not url_is_good:
                            break
                        try:
                            encoding = response.headers['content-encoding']
                        except:
                            pass
                        if (mime is None) or (encoding is None) or (len(mime) <= 5) or (len(encoding) <= 2):
                            content,encoding, mime = await loop.run_in_executor(self.pool,functools.partial(find_data_format,content,self.url,content_type=mime,content_encoding=encoding))
                        try:
                            text = await response.text()
                        except:
                            text = await response.text(encoding)
                            
                        self.check = response.status == 200
                self.cleanup = True
                break
            except aiohttp.TooManyRedirects:
                break
            except asyncio.TimeoutError:
                break
            except aiohttp.ClientConnectorError:
                break
            except aiohttp.InvalidURL:
                break
            except aiohttp.ServerDisconnectedError:
                break
            except BaseException as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print("G",exc_type, exc_obj, exc_tb,fname,exc_tb.tb_lineno)
                continue
        return (self.check,self.cleanup,text,mime,status,encoding)
    
    async def __aexit__(self, exc_type, exc, tb):
            pass



class NewWebsiteCheck:
    def __init__(self,url,path = None,name= "", rb=None,session=None,pool=None,filters_in_ext=None,filters_out_ext=None,filters_in_mime=None,filters_out_mime=None) -> None:
        self.url = url
        self.path = path
        self.rb = rb
        self.pool = pool
        self.session=session
        self.filters_in_mime = filters_in_mime
        if path is None :
            task = asyncio.current_task()
            task_name = task.get_name()
            self.path = "./"+task_name+"_"+name+"_" +".temp"
        else:
            self.path = path
            
    
    async def __aenter__(self):
        loop = asyncio.get_running_loop()
        self.check_page =False
        self.check_site =False
        self.file =None
        mime = ""
        text = ""
        encoding = ""
        status = 0
        self.cleanup = False
        
        for i in range(9):
            # filter in  extension 
            url_is_good=True
            if self.filters_in_mime is not None:
                o = urlparse(self.url)
                content_type = mimetypes.guess_type(o.path, strict=True)[0]
                if content_type is not None and len(content_type) > 0:
                    url_is_good=False
                    for filters_in_mime in self.filters_in_mime:
                        if  filters_in_mime in content_type:
                            url_is_good = True
                            break
                if not  url_is_good:
                    print("bad type:",content_type)
                    break
                
            try:
                if self.rb is not None:
                    if not self.rb.can_fetch("*", self.url):
                        break
                    time = self.rb.request_rate("*")
                    if time is not None:
                        await asyncio.sleep(time)
                async with self.session.get(self.url) as response:
                        status = response.status
                        content = await response.content.read()
                        try:
                            mime = response.headers['content-type']
                        except:
                            pass
                        
                        if self.filters_in_mime is not None and len(mime) > 0:
                            url_is_good=False
                            for filters_in_mime in self.filters_in_mime:
                                 if  filters_in_mime in mime:
                                     url_is_good = True
                                     break
                        if not url_is_good:
                            break
                        try:
                            encoding = response.headers['content-encoding']
                        except:
                            pass
                        if (mime is None) or (encoding is None) or (len(mime) <= 5) or (len(encoding) <= 2):
                            content,encoding, mime = await loop.run_in_executor(self.pool,functools.partial(find_data_format,content,self.url,content_type=mime,content_encoding=encoding))
                        try:
                            text = await response.text()
                        except:
                            text = await response.text(encoding)
                            
                        self.check_page = response.status == 200
                self.cleanup = True
                self.check_site = True
                break
            except aiohttp.TooManyRedirects:
                self.check_site = True
                break
            except asyncio.TimeoutError:
                break
            except aiohttp.ClientConnectorError:
                break
            except aiohttp.InvalidURL:
                break
            except aiohttp.ServerDisconnectedError:
                break
            except BaseException as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print("G",exc_type, exc_obj, exc_tb,fname,exc_tb.tb_lineno)
                continue
        return (self.check_page,self.cleanup,text,mime,status,encoding)
    
    async def __aexit__(self, exc_type, exc, tb):
            pass

