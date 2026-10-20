"""Create a square, face-and-shoulders JPEG without altering the supplied HEIC.

Requires: python -m pip install pillow pillow-heif
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "IMG_9578.HEIC"
OUTPUT = ROOT / "assets/img/amin-mehrvarz.jpg"


def main():
    try:
        from PIL import Image, ImageOps
        from pillow_heif import register_heif_opener
    except ImportError as error:
        raise SystemExit(
            "Portrait conversion requires Pillow and pillow-heif. Run:\n"
            "  python3 -m pip install pillow pillow-heif\n"
            "  python3 scripts/prepare_portrait.py\n"
            "The original HEIC has not been changed."
        ) from error
    register_heif_opener()
    with Image.open(SOURCE) as image:
        portrait = ImageOps.exif_transpose(image).convert("RGB")
        # Largest square in the oriented source, aligned to the top to keep
        # the face and shoulders and exclude the hands from the circular mask.
        side = min(portrait.size)
        left = (portrait.width - side) // 2
        portrait = portrait.crop((left, 0, left + side, side))
        portrait.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        # No EXIF/GPS metadata is copied into the public derivative.
        portrait.save(OUTPUT, "JPEG", quality=92, optimize=True)
    print(f"Created {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
