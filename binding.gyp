{
  "targets": [
    {
      "target_name": "audio-converter-lib",
      "sources": [
        "src/binding.c",
        "src/converter.c"
      ],
      "include_dirs": [
        "<!(node -e \"require('node-addon-api').include\")",
        "D:/audio-converter-lib/ffmpeg-7.1/libavcodec", 
        "D:/audio-converter-lib/ffmpeg-7.1/libavformat", 
        "D:/audio-converter-lib/ffmpeg-7.1/libavutil"
      ],
      "libraries": [
        "D:/audio-converter-lib/ffmpeg-7.1/libs/avcodec.lib",
        "D:/audio-converter-lib/ffmpeg-7.1/libs/avformat.lib",
        "D:/audio-converter-lib/ffmpeg-7.1/avutil.lib"
      ]
    }
  ]
}
