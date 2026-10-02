"""Font Cache Rebuild — Rebuild the Windows font cache after a preview warning."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='font_cache_rebuild',
        description='Rebuild the Windows font cache after a preview warning.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Font Cache Rebuild')
    print('Fix missing or stale font previews.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
