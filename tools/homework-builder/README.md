# Homework builder

Every session's homework has 5 parts (pass mark 80%, auto-marked in `homework/index.html`):

1. Vocabulary test · 2. Reading · 3. Listening (script shown after submitting) · 4. Shadowing (speech recognition → score /10, words green/red) · 5. Translation VN → EN (2 pts exact, 1 pt if one word off)

Build (TTS audio cached in `cache5/`):

    SSL_CA_BUNDLE=/root/.ccr/ca-bundle.crt python3 hw5.py S01 S02 S03 S04

Content lives in `<Sxx>/hw5_content.py`. Listening audio is either generated from `lines` or an existing file
(`homework/audio/Sxx/Sxx_listen_*.mp3`). `legacy/` keeps the scripts that first recorded those files — do not run
them now (they overwrite `homework/data/*.json`).
