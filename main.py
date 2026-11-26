import os

SCENE = 'At Sunday dinner, my sister and I split the last slice of pie with a ruler. Mum watched, sighed, and ate the crusts standing up \u2014 "the cook\'s tax," she said.'

def main():
    # Gate self-check: 1-280 chars, 1-2 lines, not only whitespace.
    assert 1 <= len(SCENE) <= 280, f"scene length {len(SCENE)} outside 1-280"
    assert 1 <= len(SCENE.splitlines()) <= 2, "scene must be 1-2 lines"
    assert SCENE.strip(), "scene must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SCENE)

if __name__ == "__main__":
    main()
