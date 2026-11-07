#!/usr/bin/env bash
# Rebuild Session 01 end to end.
#   1. gen_audio.py  -> mp3/  (Microsoft neural voices via edge-tts; cached in cache/)
#   2. assemble.py   -> dist/S01_embedded.html (single file, audio embedded — for offline use)
#   3. patch2.py     -> final styling pass on the embedded file
#   4. build_web.py  -> ../../../lessons/S01/ (website version, audio as separate MP3 + ZIP)
# Requirements: python3, ffmpeg, pip install edge-tts numpy
set -euo pipefail
cd "$(dirname "$0")"
python3 gen_audio.py
python3 assemble.py
python3 patch2.py
python3 patch3.py
python3 build_web.py
