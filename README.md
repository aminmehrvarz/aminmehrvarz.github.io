# aminmehrvarz.github.io

# Ehs Noo — Academic Website

## Introduction

Welcome to my academic and professional website. I hold a Ph.D. in Mechanical Engineering, specializing in mechatronics and robotics, from Northeastern University. My research and engineering interests include robotics, control systems, motion planning, kinematics, and intelligent mechatronic systems. My work spans robotic control algorithms, optimization, embedded software, and the development of advanced robotic systems, with a focus on surgical robotics and real-world applications. This website provides an overview of my background, research interests, publications, engineering experience, and selected projects.

## Website

**[Visit aminmehrvarz.github.io](https://aminmehrvarz.github.io)**

You can also find me on [GitHub](https://github.com/aminmehrvarz).

## Sections

- **About** — Biography, profile photo, and links.
- **Research** — Research interests and projects.
- **Publications** — Publication records and related materials.
- **Teaching** — Teaching experience and course information.
- **Beyond Research** — A few interests and milestones outside my academic work.

## Built With

The site is built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) academic website starter and its plugins. [GitHub Actions](.github/workflows/deploy.yml) builds the site and publishes it to GitHub Pages. The repository also uses Ruby and Bundler for the Jekyll dependencies, and Node.js, npm, and Prettier for formatting and development checks.

## Repository Structure

- [`_pages/`](_pages/) contains the About, Research, Publications, Teaching, and Beyond Research pages.
- [`_data/`](_data/) contains structured site content, including profile settings, publications, teaching entries, and research projects.
- [`assets/img/`](assets/img/) stores site images, including the profile photo.
- [`assets/pdf/`](assets/pdf/) contains the CV PDF.
- [`_config.yml`](_config.yml) configures Jekyll and the site.
- [`Gemfile`](Gemfile) and [`Gemfile.lock`](Gemfile.lock) define and lock Ruby dependencies.
- [`.github/workflows/`](.github/workflows/) contains GitHub Actions workflows, including deployment.
- [`LICENSE`](LICENSE) retains the MIT license and its original al-folio copyright notice.

## Maintenance

- Update the biography and profile photo through [`_pages/about.md`](_pages/about.md) and the image in [`assets/img/`](assets/img/).
- Replace the CV at [`assets/pdf/CV.pdf`](assets/pdf/CV.pdf); its configured path is in [`_data/profile.yml`](_data/profile.yml).
- Add confirmed publication records to [`_data/publications.yml`](_data/publications.yml).
- Add teaching entries to [`_data/teaching.yml`](_data/teaching.yml).
- Add research projects to [`_data/research_projects.yml`](_data/research_projects.yml).

Only add verified publications, appointments, and project details to these data files.

## Deployment

The [deployment workflow](.github/workflows/deploy.yml) runs for qualifying pushes and pull requests targeting `main` or `master`. It installs Ruby and Node dependencies, builds the Jekyll site, and deploys the generated `_site` directory to the `gh-pages` branch on pushes. README-only changes are excluded from its path filters, so updating this file alone does not trigger a site deployment.

## Acknowledgments

This site is based on [al-folio](https://github.com/alshedivat/al-folio), an open-source academic website starter, and uses Jekyll and its plugin ecosystem. See [`LICENSE`](LICENSE) for the retained MIT license and required copyright and permission notice.
