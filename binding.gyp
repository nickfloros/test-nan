{
  "targets": [
    {
      "target_name": "test-nan",
      "sources": [
        "src/addon.cc",
        "src/pi_est.cc",
        "src/sync.cc",
        "src/async.cc"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"]
    }
  ]
}
