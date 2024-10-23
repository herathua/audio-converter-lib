{
  "targets": [
    {
      "target_name": "audio_converter",
      "sources": ["src/converter.c"],
      "include_dirs": [
        "<!(node -e \"require('node-addon-api').include\")"
      ],
      "libraries": [
        "-lavcodec", "-lavformat", "-lavutil"
      ]
    }
  ]
}
