{
  "targets": [
    {
      "target_name": "audio-converter-lib",
      "sources": [
        "src/binding.c",
        "src/converter.c"
      ],
      "include_dirs": [
        "<!(node -e \"require('node-addon-api').include\")"
      ],
      "libraries": [
        "-lavcodec", "-lavformat", "-lavutil"
      ]
    }
  ]
}
