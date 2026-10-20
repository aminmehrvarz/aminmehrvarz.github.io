"""Validate this site's content, assets, and (optionally) a real Jekyll build.

Requires PyYAML. Does not fetch external links or substitute for visual inspection.
"""

import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return yaml.safe_load((ROOT / name).read_text())


def front_matter(path):
    text = path.read_text()
    assert text.startswith("---\n"), f"Missing front matter: {path.name}"
    return yaml.safe_load(text.split("---", 2)[1])


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = set()
        self.publication_entries = 0
        self.publication_thumbnails = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "article" and "publication-entry-text" in classes:
            self.publication_entries += 1
        if "publication-thumbnail" in classes:
            self.publication_thumbnails += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attr in ("href", "src", "poster"):
            if attrs.get(attr):
                self.references.append(attrs[attr])


def validate_build(directory, baseurl):
    directory = directory.resolve()
    assert directory.is_dir(), f"Build directory missing: {directory}"
    documents = {}
    for path in directory.rglob("*.html"):
        parser = Links()
        parser.feed(path.read_text())
        documents[path] = parser
    assert documents, "No HTML found; run the actual Jekyll build first"
    for permalink in ("", "research", "publications", "beyond-research"):
        assert directory / permalink / "index.html" in documents, f"Missing page: {permalink}"
    checked = 0
    for page, parser in documents.items():
        for reference in parser.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith("/"):
                if baseurl:
                    assert path == baseurl or path.startswith(baseurl + "/"), (
                        f"Link misses baseurl {baseurl}: {page.name}: {reference}"
                    )
                    path = path[len(baseurl):]
                target = directory / path.lstrip("/")
            elif path:
                target = page.parent / path
            else:
                target = page
            target = target.resolve()
            assert target.is_relative_to(directory), f"Link escapes build: {reference}"
            if target.is_dir():
                target = target / "index.html"
            assert target.is_file(), f"Broken internal reference: {page}: {reference}"
            if url.fragment and target in documents:
                assert unquote(url.fragment) in documents[target].ids, (
                    f"Missing anchor: {page}: {reference}"
                )
            checked += 1
    pubs = documents[directory / "publications/index.html"]
    assert pubs.publication_entries == 17, "Expected 17 text-only publication cards"
    assert pubs.publication_thumbnails == 0, "Unexpected publication thumbnail"
    home = documents[directory / "index.html"]
    assert home.publication_entries == 3
    print(f"PASS: {len(documents)} generated HTML pages; {checked} internal references; publication cards")


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--publish", action="store_true")
    args.add_argument("--site", type=Path)
    args.add_argument("--baseurl", help="Override for validating a build with a project prefix")
    options = args.parse_args()
    config = load("_config.yml")
    profile = load("_data/profile.yml")
    socials = load("_data/socials.yml")
    publications = load("_data/publications.yml")
    academic = load("_data/academic.yml")
    assert config["title"] == profile["name"] == "Amin Mehrvarz"
    assert config["first_name"] == "Amin" and config["last_name"] == "Mehrvarz"
    assert socials["email"] == academic["contact"]["email"] == "amin.mehrvarz@gmail.com"
    assert profile["affiliation"] == "Medtronic"
    assert profile["google_scholar"] == "https://scholar.google.com/citations?user=aRVDlhMAAAAJ"
    assert profile["linkedin"] == "https://www.linkedin.com/in/amin-mehrvarz/"
    assert not socials.get("github_username") and not profile.get("orcid")
    assert len(publications) == 17
    assert sum(bool(p.get("selected")) for p in publications) == 3
    assert len(load("_data/research_projects.yml")) == 8
    assert len(academic["education"]) == 4
    assert len(academic["experience"]) == 7
    assert len(academic["awards"]) == 6
    for publication in publications:
        assert all(publication.get(k) for k in ("title", "authors", "venue", "year"))
        assert any("Mehrvarz" in a for a in publication["authors"])
        assert not any(publication.get(k) for k in ("thumbnail", "image", "preview", "video_url", "youtube_id"))
        assert isinstance(publication["year"], int)
    for filename, title, url, order in (
        ("about.md", "Home", "/", 1),
        ("research.md", "Research", "/research/", 2),
        ("publications.md", "Publications", "/publications/", 3),
        ("beyond-research.md", "Beyond Research", "/beyond-research/", 4),
    ):
        page = front_matter(ROOT / "_pages" / filename)
        assert (page["title"], page["permalink"], page["nav_order"]) == (title, url, order)
        assert page["layout"] == "academic"
    forbidden = ("ehsnoo", "ehs noo", "ehs@", "baltimore", "office hours", "smoke-free", "alcohol-free")
    for folder in ("_pages", "_includes", "_layouts", "_data"):
        for path in (ROOT / folder).rglob("*"):
            if path.is_file():
                assert not any(token in path.read_text().lower() for token in forbidden), path
    original = ROOT / "Amin Mehrvarz-CV.pdf"
    public = ROOT / unquote(profile["cv_pdf"])
    assert original.read_bytes() == public.read_bytes(), "CV derivative changed"
    assert hashlib.sha256(original.read_bytes()).hexdigest() == (
        "f241425eaf065e0f71934fb7ab20e93c22dc5be6ea7420304fbdcd47dea8e3a0"
    )
    assert hashlib.sha256((ROOT / "IMG_9578.HEIC").read_bytes()).hexdigest() == (
        "4fcd5f921aeb4897b65c450aadd26412859c7c23e02063e184e8f10e3f5427c7"
    )
    assert (ROOT / "assets/img/amin-mehrvarz.heic").read_bytes() == (ROOT / "IMG_9578.HEIC").read_bytes()
    print("PASS: identity, four-page navigation, 17 publications, 8 projects, education, experience, awards, original CV/photo")
    portrait = ROOT / profile["image"]
    if not portrait.is_file():
        message = "JPEG portrait pending: run python3 scripts/prepare_portrait.py; sidebar links the supplied HEIC until then"
        assert not options.publish, message
        print("PENDING:", message)
    baseurl = config.get("baseurl", "")
    assert not baseurl or (baseurl.startswith("/") and not baseurl.endswith("/")), "Invalid baseurl"
    if options.publish:
        url = urlsplit(config.get("url", ""))
        assert url.scheme == "https" and url.netloc and url.path in ("", "/"), (
            "Set the confirmed production origin in _config.yml before publishing"
        )
        print("PASS: production origin and portrait configured")
    if options.site:
        validate_build(options.site, options.baseurl if options.baseurl is not None else baseurl)


if __name__ == "__main__":
    main()
