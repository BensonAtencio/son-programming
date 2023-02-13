const fs = require('fs');
const path = require('path');

//Create a folder
// fs.mkdir(path.join(__dirname, 'test'), {}, err => {
//     if (err) throw err;
//     console.log('Folder created')
// })

// Create and wriite to file
// fs.writeFile(path.join(__dirname, 'test', 'hello.txt'), 'Hello node', err => {
//     if (err) throw err;
//     console.log('File created')

//     //Append 
//     fs.appendFile(path.join(__dirname, 'test', 'hello.txt'), ' I love Node.js', err => {
//         if (err) throw err;
//         console.log('File created')
//     })
// })

//Read File
// fs.readFile(path.join(__dirname, 'test', 'hello.txt'), 'utf8', (err, data) => {
//         if (err) throw err;
//         console.log(data)
// })

//Rename
// fs.rename(path.join(__dirname, 'test', 'hello.txt'), (path.join(__dirname, 'test', 'narename.txt')), err => {
//         if (err) throw err;
//         console.log('renamed')
// })