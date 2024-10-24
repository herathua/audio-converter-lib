// test.js
const audioConverter = require('./index');

const src = 'input.wav';       // Input audio file
const dest = 'output.mp3';     // Output audio file
const format = 'mp3';          // Desired output format

audioConverter.convertAudio(src, dest, format);
console.log('Conversion completed!');
