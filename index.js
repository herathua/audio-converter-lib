// index.js
const audioConverter = require('./build/Release/audio_converter');

module.exports = {
    convertAudio: audioConverter.convertAudio
};
