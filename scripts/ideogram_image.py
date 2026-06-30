#!/usr/bin/env python3
"""Generate a LinkedIn post image with Ideogram.

The API key is read from the IDEOGRAM_API_KEY environment variable.
Never hardcode the key. Set it as an environment secret, not in code.

Usage:
    export IDEOGRAM_API_KEY=...        # set as an env secret, not in chat
    python scripts/ideogram_image.py "your image prompt" out/post.png
    python scripts/ideogram_image.py "prompt" out/post.png --aspect 1x1

Default aspect is 1x1 (square, good for LinkedIn feed). Use 16x9 for landscape.
"""
import os
import sys
import argparse
import urllib.request

API_URL = "https://api.ideogram.ai/v1/ideogram-v3/generate"


def generate(prompt: str, out_path: str, aspect: str = "1x1") -> str:
    # Preferred name is IDEOGRAM_API_KEY. Fallbacks tolerate common near-misses.
    key = (
        os.environ.get("IDEOGRAM_API_KEY")
        or os.environ.get("HYDROGRAM_API_KEY")
        or os.environ.get("IDEOGRAM_API")
    )
    if not key:
        sys.exit(
            "IDEOGRAM_API_KEY is not set. Set it as an environment secret named "
            "IDEOGRAM_API_KEY (no spaces). Env var names cannot contain spaces."
        )

    # Ideogram v3 generate expects multipart/form-data.
    boundary = "----bqideogramboundary"
    parts = []
    for name, value in (
        ("prompt", prompt),
        ("aspect_ratio", aspect),
        ("rendering_speed", "DEFAULT"),
        ("magic_prompt", "AUTO"),
    ):
        parts.append(f"--{boundary}")
        parts.append(f'Content-Disposition: form-data; name="{name}"')
        parts.append("")
        parts.append(value)
    parts.append(f"--{boundary}--")
    parts.append("")
    body = "\r\n".join(parts).encode("utf-8")

    req = urllib.request.Request(API_URL, data=body, method="POST")
    req.add_header("Api-Key", key)
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")

    import json
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    url = data["data"][0]["url"]
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    urllib.request.urlretrieve(url, out_path)
    return out_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("out", nargs="?", default="out/linkedin.png")
    ap.add_argument("--aspect", default="1x1")
    args = ap.parse_args()
    saved = generate(args.prompt, args.out, args.aspect)
    print(f"saved: {saved}")
