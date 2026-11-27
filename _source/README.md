# Site source (not served)

Python generators for bookedorion.com. Folders starting with `_` are not published by GitHub Pages.
They expect a working copy laid out as `blog/` (these .py files) next to `site/` (this repo's root files).
Run: `python3 home_v3.py && python3 build_blog.py && python3 build_pages.py && python3 finish.py`, then copy the output to the repo root and keep `CNAME`.

`finish.py` loads `/premium.css` last on every page (the premium visual layer) and sentence-cases section labels. `premium.css` lives at the site root and is edited by hand.

## Status note (27 Nov 2026)

The HTML at the repo root is the source of truth. These generators are behind it (for example, the home "setup" and "proof" sections exist only in `index.html`).

On 27 Nov 2026 the Night-only plan was removed from the site. Two plans remain: Pay-per-Job and Flat. `pricing.py` and `after_hours.py` here still contain Night-only text. Update them before running a rebuild, or the old plan comes back.
