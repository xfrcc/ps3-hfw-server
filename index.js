const axios = require('axios').default;
const regions = require('./regions.json');
const express = require('express');
const stream = require('stream');
const app = express();
const port = 80;

app.get('/*', async(req, res) => {
    let url = req.originalUrl[0] == '/' ? req.originalUrl.substring(1) : req.originalUrl;
    console.log(url.length);
    let localPath = url.startsWith('http://') ? url.substring(7) : url;
    if(url.match('f..01.ps3.update.playstation.net/update/ps3/list/../ps3-updatelist.txt')) {
        console.log('Spoofing update...');
        const region = url.substring(url.indexOf('list/')+5, url.indexOf('/ps3-updatelist.txt'));
        console.log(`Console region is ${region}`);
        const updateResponse = `# ${regions[region].name}\r\nDest=${regions[region].targetId};ImageVersion=ffffffff;SystemSoftwareVersion=4.89;CDN=PS3UPDAT.PUP;CDN_Timeout=30;\r\n`;
        res.setHeader('Content-Type', 'text/plain');
        res.setHeader('Content-Length', updateResponse.length);
        res.status(200).send(updateResponse);
    }
    else if (url.match('http://ps3xploit.com/hen/installer/manual/..../HEN.pkg')) {
        console.log('Providing HEN.pkg from PS3Xploit.com...');
        const response = await axios.get(url, { responseType: 'arraybuffer' });
        const buffer = Buffer.from(response.data, 'binary');
        let readStream = new stream.PassThrough();
        readStream.end(buffer);
        res.set('Content-disposition', 'attachment; filename=HEN.pkg');
        res.setHeader('Content-Length', response.headers['content-length']);
        res.set('Content-Type', 'application/octet-stream');
        readStream.pipe(res);
    }
    else if (localPath == 'PS3UPDAT.PUP') {
        console.log('Providing PS3UPDAT.PUP...');
        res.download('./firmware/PS3UPDAT.PUP');
    }
    else {
        try {
            console.log("Redirecting to PS3Xploit's HEN Installer...");
            const response = await axios.get('https://ps3xploit.com/hen/installer/manual/index.html', {
                headers: {
                    'User-Agent':'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
                    'Accept': 'text/html'
                }
              });
            const userAgent = req.headers['user-agent'];
            const firmwareVer = userAgent.substring(userAgent.indexOf('5.0 (')+19, userAgent.indexOf(') Apple'));
            const regex = new RegExp(/\'\+baseURL\+fwv\+\'/, 'g');
            const body = response.data.replace(regex,  `http://ps3xploit.com/hen/installer/manual/${firmwareVer}`);
            res.setHeader('Content-Type', 'text/html');
            res.setHeader('Content-Length', body.length);
            res.status(response.status).send(body);
        }
        catch (e) {
            console.error(e);
            res.setHeader('Content-Type', 'text/html');
            res.setHeader('Content-Length', e.response.data.length);
            res.status(e.response.status).send(e.response.data);
        }
        
    }
});



app.listen(port, () =>
  console.log(`Listening on port ${port}`)
);
