#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from pytanque import Pytanque, PytanqueMode


def toc_element_to_dict(element):
    return {
        "name": element.name.v,
        "detail": element.detail,
        "kind": element.kind,
        "range": {
            "start": {
                "line": element.range.start.line + 1,
                "character": element.range.start.character,
            },
            "end": {
                "line": element.range.end.line + 1,
                "character": element.range.end.character,
            },
        },
        "children": [toc_element_to_dict(child) for child in (element.children or [])],
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a TOC for a Rocq file via pytanque.")
    parser.add_argument(
        "file",
        nargs="?",
        default="token_logrel/logrel.v",
        help="Path to the Rocq file to inspect.",
    )
    parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root passed to pet/pytanque.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full TOC as JSON.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    workspace = Path(args.workspace).resolve()
    file_path = Path(args.file).resolve()

    with Pytanque(mode=PytanqueMode.STDIO) as client:
        client.set_workspace(debug=False, dir=str(workspace))
        toc = client.toc(str(file_path))

    if args.json:
        payload = [
            {"entry": name, "elements": [toc_element_to_dict(element) for element in elements]}
            for name, elements in toc
        ]
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    for name, elements in toc:
        for element in elements:
            start = element.range.start
            print(
                f"{name}: {element.detail} "
                f"(kind={element.kind}, line={start.line + 1}, char={start.character})"
            )


if __name__ == "__main__":
    main()
