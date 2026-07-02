# yunchih.github.io

This site now just **redirects to <https://sys-nthu.tw/yunchih/>** (NTHU SYSLAB).

- `index.html` / `404.html` — client-side redirect (meta refresh + `location.replace`,
  with a `canonical` link for search engines).
- `.github/workflows/deploy.yml` — publishes the redirect to GitHub Pages.

The old Hugo personal site was removed; its history remains in git.
