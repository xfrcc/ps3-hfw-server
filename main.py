import re
import sys
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
import requests
import shutil

PORT = 80
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
        if re.search("f..01.ps3.update.playstation.net/update/ps3/list/../ps3-updatelist.txt", url):
            region = url.split("/")[-2]
            print('Console region is {}'.format(region))
            res = "# {}\r\n".format(regions[region]["name"])+\
            "Dest={};ImageVersion=00010aae;SystemSoftwareVersion=9.99;CDN=PS3UPDAT.PUP;CDN_Timeout=30;\r\n".format(regions[region]["targetId"])
            print('Spoofing update... {}'.format(region))
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(res)))
            self.end_headers()
            self.wfile.write(bytes(res, "utf8"))

        elif url.lower().endswith('.pup'):
            self.path = url.replace("http://", "")
            SimpleHTTPRequestHandler.do_GET(self)

        elif "hen.pkg" in url.lower():
            print("Providing HEN.pkg downloaded from PS3Xploit.com...")
            self.path = "HEN.pkg"
            SimpleHTTPRequestHandler.do_GET(self)

        else:
            print("Redirecting to PS3Xploit installer...")
            ua = self.headers["user-agent"]
            fwv = ua[ua.index("5.0 (")+19:ua.index(") Apple")]
            fileName = "HEN.pkg"
            r = requests.get("http://ps3xploit.com/hen/installer/manual/index.html")
            self.send_response(r.status_code)
            body = r.content.decode("utf8")
            print(body)
            for name, value in r.headers.items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(bytes(body, "utf8"))
            r = requests.get("http://ps3xploit.com/hen/installer/manual/{}/HEN.pkg".format(fwv), stream=True)
            dl = open(fileName, 'wb')
            shutil.copyfileobj(r.raw, dl)
            dl.close()


    def do_HEAD(self):
        url = self.path if self.path[0] != "/" else self.path[1:]
        if url.lower().endswith('.pup'):
            self.path = url.replace("http://", "/")
            SimpleHTTPRequestHandler.do_HEAD(self)
        elif "hen.pkg" in url.lower():
            print("Providing HEN.pkg downloaded from PS3Xploit.com...")
            self.path = "HEN.pkg"
            SimpleHTTPRequestHandler.do_HEAD(self)



proxy = HTTPServer(('', PORT), PS3Proxy)
host, port = proxy.socket.getsockname()
print("Proxy Server Ready!")
try:
    proxy.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    sys.exit(0)
