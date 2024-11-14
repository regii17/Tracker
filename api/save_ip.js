const fs = require('fs');
const path = require('path');

export default function handler(req, res) {
    // Dapatkan alamat IP pengguna
    const userIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    // Tentukan path file tempat IP akan disimpan
    const filePath = path.join(process.cwd(), 'ip.txt');

    // Tulis IP ke file dengan cara append (menambahkan di akhir file)
    fs.appendFile(filePath, `${userIp}\n`, (err) => {
        if (err) {
            console.error('Error saving IP:', err);
            res.status(500).send('Internal Server Error');
            return;
        }
        res.status(200).send('IP Anda telah tercatat.');
    });
}
