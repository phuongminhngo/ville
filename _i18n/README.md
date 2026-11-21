# English version (en.html)

`en.html` is generated from `index.html`. After changing the French site, rebuild it:

    cd _i18n && python3 make_en.py

- `t1.py`, `t2.py`, `t3.py`: translations, keyed by position in `todo.json` (the French strings).
- `t4.py`: extra labels (`EXTRA`) and code-level replacements (`SRC`) for text drawn on canvases or built in code.
- New French text that is not in these tables stays in French on `en.html`: add it to `EXTRA` in `t4.py`.
