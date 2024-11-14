const fs = require('fs');
const path = require('path');

export default function handler(req, res) {
    const userIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log(`User IP: ${userIp}`);

    res.writeHead(302, { Location: 'https://drive.google.com/drive/folders/1m2Fs1OaE2wfJWTMCu-M5-f4ltnbQQN1L' });
    res.end();
}
