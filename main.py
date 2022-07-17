import re
import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib import request, error, response

from matplotlib.pyplot import close

PORT = 80
LOCALIP = "192.168.1.236"
regions = {
    "jp": { "name": "JP", "targetId": "83" },
    "us": { "name": "US", "targetId": "84" },
    "eu": { "name": "EU", "targetId": "85" },
    "kr": { "name": "KR", "targetId": "86" },
    "uk": { "name": "UK", "targetId": "87" },
    "mx": { "name": "MX", "targetId": "88" },
    "au": { "name": "AU/NZ", "targetId": "89" },
    "sa": { "name": "SouthAsia", "targetId": "8A" },
    "tw": { "name": "TW", "targetId": "8B" },
    "ru": { "name": "RU", "targetId": "8C" },
    "cn": { "name": "CN", "targetId": "8D" },
    "br": { "name": "BR", "targetId": "8F" }
    }
	

class PS3Proxy(SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path if self.path[0] != "/" else self.path[1:]
        print("URL requested: " + url)
        if re.search("f..01.ps3.update.playstation.net/update/ps3/list/../ps3-updatelist.txt", url):
            region = url.split("/")[-2]
            res = "# {}\r\n".format(regions[region]["name"])+\
            "Dest={};ImageVersion=99999999;SystemSoftwareVersion=9.99;CDN=PS3UPDAT.PUP;CDN_Timeout=30;\r\n".format(regions[region]["targetId"])
            print(res)
            #print(res)

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", len(res))
            #self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(bytes(res, "utf8"))
        elif "PS3UPDAT.PUP" in url:
            try:
                self.path = self.path.replace("http://", "")
                print("Serving update...")
                f = self.send_head()
                if f:
                    try:
                        self.copyfile(f, self.wfile)
                    finally:
                        f.close()
                #self.copyfile(request.urlopen(url), self.wfile)
            except error.HTTPError as e:
                self.send_response_only(e.code)
                self.end_headers()
                return
        else:
            msg = sys.version
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", len(msg))
            self.end_headers()
            self.wfile.write(bytes(msg, "utf8"))
    def do_HEAD(self):
        url = self.path if self.path[0] != "/" else self.path[1:]    
        if "PS3UPDAT.PUP" in url:
            try:
                self.path = self.path.replace("http://", "")
                print("Serving update HEAD...")
                f = self.send_head()
                if f:
                    #try:
                    self.copyfile(f, self.wfile)
                    #finally:
                        #f.close()
            except error.HTTPError as e:
                self.send_response_only(e.code)
                self.end_headers()
                return


proxy = HTTPServer(('', PORT), PS3Proxy)
host, port = proxy.socket.getsockname()
print(f'Listening on {host}:{port}')
try:
    proxy.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    sys.exit(0)