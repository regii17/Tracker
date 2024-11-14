const fs = require('fs');
const path = require('path');

export default function handler(req, res) {
    const userIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log(`User IP: ${userIp}`);
    res.status(200).send('IP Anda telah tercatat di log.');
}

