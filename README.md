# Amin Mehrvarz — Academic Website

An independent Jekyll / al-folio site using the supplied reference site's customized academic layout. The navigation is Home, Research, Publications, and Beyond Research. Content comes from `Amin Mehrvarz-CV.pdf`; the original PDF and `IMG_9578.HEIC` remain unchanged in the repository root.

## Local preview

Install Ruby 3.3, Bundler, Python 3, and Node.js 20 if using the optional formatting tools. From this directory:

```bash
gem install bundler -v 4.0.6
bundle install
python3 -m pip install PyYAML pillow pillow-heif
python3 scripts/prepare_portrait.py
python3 scripts/validate.py
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open <http://127.0.0.1:4000/>. The production `url` is deliberately empty until the future repository/domain is confirmed. `baseurl` is empty for the local preview.

The portrait helper converts the supplied HEIC to `assets/img/amin-mehrvarz.jpg`, applies its orientation, limits it to 1600 pixels, and strips EXIF metadata. It preserves the HEIC and keeps an existing JPEG. Until conversion succeeds, the sidebar provides a link to the original photograph instead of a broken image. The CI workflows run the conversion before building.

## Content and design

- `_config.yml`: identity, deployment origin, base path, and inherited al-folio settings.
- `_data/profile.yml`, `_data/socials.yml`: role, affiliation, photo, email, CV, and verified profile URLs.
- `_data/academic.yml`: education, experience, research interests, skills, awards, documented teaching, languages, memberships, and CV contact details.
- `_data/publications.yml`: all 17 publications listed in the supplied CV; three are selected for the homepage.
- `_data/research_projects.yml`: concise summaries of the CV's eight named projects.
- `_pages/`: four primary pages and a 404 page.
- `_layouts/academic.liquid`, `_includes/academic-sidebar.liquid`, `assets/css/academic-layout.css`: the reference site's custom academic shell, responsive sidebar, and styling, adapted for Amin.
- `_includes/publication-entry.liquid`: shared publication cards; text-only entries span the full width. Optional `thumbnail` and `thumbnail_alt` fields can be added later without changing the layout. None are currently set.
- `assets/pdf/Amin Mehrvarz-CV.pdf`: byte-identical public copy of the supplied CV, served through an encoded URL.

Amin's current role is listed as stated in the CV. Northeastern and Sharif are educational/research history; no current university appointment is claimed. No GitHub username or ORCID was provided, so those links are omitted. Beyond Research uses only the CV's languages and professional memberships. Missing publication DOIs and publisher URLs are omitted; two arXiv links use identifiers explicitly printed in the CV.

Keep the original input files excluded from Jekyll output; the intended public copies live in `assets/`. Windows `Zone.Identifier` sidecar files are preserved but excluded from output.

## Validation

```bash
python3 scripts/validate.py
bundle exec jekyll build --trace
python3 scripts/validate.py --site _site
```

The validator checks content consistency, navigation, source-file preservation, publication counts, the absence of publication images, and generated internal links/assets when a Jekyll build is supplied. It reports a pending portrait locally and requires the JPEG and a production origin with `--publish`. It does not validate remote links or replace browser inspection.

Check a project-site prefix before publishing to a repository subpath:

```bash
bundle exec jekyll build --baseurl /amin-preview
python3 scripts/validate.py --site _site --baseurl /amin-preview
bundle exec jekyll serve --baseurl /amin-preview
```

Open <http://127.0.0.1:4000/amin-preview/>. Inspect all four pages at desktop and mobile widths, the navigation toggle, the dark-mode control, portrait, CV link, and publication wrapping.

Optional formatting:

```bash
npm ci
npm run lint:prettier
```

See `IMPLEMENTATION.md` for the checks actually run in the implementation environment and their limitations.

## Publish later on GitHub Pages

This checkout already contains commits and an origin tracking branch. This task does not commit, push, or deploy changes.

1. Confirm Amin's GitHub username and intended repository. Set `url` in `_config.yml` to the confirmed HTTPS origin, such as `https://USERNAME.github.io`; do not put a repository path in `url`.
2. For `USERNAME.github.io`, keep `baseurl: ""`. For a project repository, use `baseurl: "/REPOSITORY"` with no trailing slash. Configure a custom domain separately if wanted.
3. Generate and inspect the JPEG portrait. Run the build and link validation above, then inspect desktop and mobile layouts in a browser. `python3 scripts/validate.py --publish` checks the portrait and origin prerequisites.
4. When authorized, commit the reviewed files, connect the chosen GitHub remote, and push the working branch. This checkout already has an origin tracking branch; verify that its destination is the intended repository before pushing.
5. Choose **Settings → Pages → Source → GitHub Actions** in that repository. The `Build website` workflow builds and uploads a preview artifact on pushes and pull requests; it does not deploy.
6. When ready to publish, manually run **Publish GitHub Pages (manual)** on the intended branch and select its `publish` checkbox. The default is false; the workflow never deploys on a push.

The GitHub Pages workflows build Jekyll with the pinned custom gems; GitHub Pages' built-in restricted Jekyll builder is not used. No original-site deployment, Docker publishing, citation updates, scheduled jobs, or release workflows have been carried into this project.

## Attribution

Based on the customized local `ehsnoo.github.io` reference and the [al-folio](https://github.com/alshedivat/al-folio) starter and gems. The MIT license and its copyright notice are retained in `LICENSE`.
