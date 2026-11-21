# BESSA website (bessa.co.za)

Static, dependency-free website for the Biomedical Engineering Society of South Africa.
Seven pages, one shared stylesheet, no build tooling required to host it.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Home |
| `about.html` | About BESSA, governance, and the IFMBE section (`#governance`, `#ifmbe`) |
| `membership.html` | Categories, benefits, fees, how to apply |
| `sabec-2027.html` | SABEC 2027: fees with member discount, key dates, tracks, links |
| `events.html` | Events, AGM, divisions and working groups |
| `contact.html` | Secretariat, resources, partners |
| `join.html` | Membership application form (emails the application to BESSA@uct.ac.za) |
| `404.html` | Not-found page (GitHub Pages serves it automatically) |
| `assets/styles.css`, `assets/site.js` | Shared styling and the mobile menu |
| `assets/bessa-logo.jpg`, `assets/ifmbe-logo.png`, `assets/favicon.svg` | Brand assets |
| `CNAME`, `robots.txt`, `sitemap.xml` | Hosting and search metadata |
| `build.py`, `join_body.html` | Optional generator: page bodies live in `build.py`; run `python3 build.py` to regenerate all pages with the shared header/footer |

## Editing

Edit the HTML files directly (every page is self-contained), or edit the page bodies in `build.py` and run
`python3 build.py` so the header, footer and metadata stay consistent across pages. Brand colours and type are
tokens at the top of `assets/styles.css`.

## Hosting on GitHub Pages (free)

1. Create a public repository (for example `bessa-website`) and push these files to its `main` branch.
2. Repository → Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. Settings → Pages → Custom domain: `bessa.co.za` (the `CNAME` file already carries it). Tick *Enforce HTTPS* once the certificate is issued (a few minutes after DNS resolves).

## DNS at the registrar (bessa.co.za)

Replace the records that currently point at Gamma with GitHub Pages:

| Host | Type | Value |
| --- | --- | --- |
| `@` | A | `185.199.108.153` |
| `@` | A | `185.199.109.153` |
| `@` | A | `185.199.110.153` |
| `@` | A | `185.199.111.153` |
| `www` | CNAME | `<github-account>.github.io` |

Propagation usually takes minutes to a few hours. For `bessa.org.za`, set a 301 forward to `https://bessa.co.za`
at its registrar/host (or add the same records and a second custom domain).

## Any other host

The site is plain HTML: upload the folder to any web host (UCT ICTS, cPanel, Netlify, Cloudflare Pages) and point
`bessa.co.za` at it. Nothing needs to be installed on the server.
