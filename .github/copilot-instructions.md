# Copilot instructions — LargeType (Ulauncher extension)

Purpose
- This repository is a small Ulauncher extension that shows entered text fullscreen using GTK3. Keep changes minimal and focused: most important files are `main.py` (extension entry), `show_text.py` (GTK window), and `manifest.json` (metadata).

Entry points & architecture
- `main.py`: Ulauncher extension class `LargeType` subscribes to `KeywordQueryEvent` and `ItemEnterEvent`. On a keyword query it builds an `ExtensionResultItem` and (currently) spawns `show_text.py` via `subprocess.Popen`.
- `show_text.py`: standalone GTK3 script that creates a fullscreen translucent window and a centered `Gtk.Label` from `sys.argv`.
- Data flow: user types keyword -> `KeywordQueryEvent` -> build result item -> on enter spawn `show_text.py` with the text -> `show_text.py` displays fullscreen text.

Important patterns & repo-specific quirks
- Ulauncher API v2: follow the `EventListener` pattern used in `main.py`. Example: `self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())`.
- Files referenced by code: `images/largetype.png` (icon), `styles.css` (CSS). Paths in `main.py` and `show_text.py` are currently relative or absolute to the install location (see notes below) — be careful when changing them.
- Known small issues to be aware of: `show_text.py` loads CSS from an absolute path (`/home/herman/.local/share/ulauncher/extensions/largetype/styles.css`) and contains a stray `te` at the file end. CSS declares `#bigtext` but `show_text.py` sets name `largetype` on the label. Mention these in PRs if you fix them.

Developer workflows & quick tests
- Run the display component locally (recommended for UI changes):
  - `python3 show_text.py "Hello world"` — requires X server and GTK3/PyGObject (`python3-gi`).
- Testing `main.py`: it is an extension that expects Ulauncher runtime. To iterate quickly:
  - Add logging statements in `main.py` and run Ulauncher, or restart Ulauncher after installing the extension. A quick restart: `pkill -f ulauncher && ulauncher` (user session) or use Ulauncher UI to reload extensions if developer mode is available.
- Debugging GTK UI: use `python3 -m pdb show_text.py "test"` or add diagnostic `print()`/logging before `Gtk.main()`.

Dependencies
- GTK3 / PyGObject (`python3-gi`) for `show_text.py`.
- Ulauncher runtime for `main.py` (`ulauncher.api.*` imports). Install Ulauncher to test extension integration.

When editing code
- Preserve manifest keys (`id`, `required_api_version`) unless explicitly changing the extension identity.
- Prefer constructing paths with `os.path.expanduser` and `os.path.join` rather than hard-coded absolute paths. If you change paths, update both `main.py` and `show_text.py` consistently and document the change in the PR.
- Keep `ExtensionResultItem` usage consistent with other Ulauncher extensions: `icon`, `name`, `description`, `on_enter`.

What to include in PRs
- Short description of impact (UI, API, packaging).
- How you tested locally (commands used, whether you restarted Ulauncher, sample text used).
- If you fix UI quirks (CSS id mismatch, stray characters), include before/after screenshots or steps used to reproduce.

If anything is unclear, tell me which area (packaging, runtime paths, or GTK UI) you want expanded and I will iterate.
