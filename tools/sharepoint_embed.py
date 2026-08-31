#!/usr/bin/env python3
"""Turn a public OneDrive/SharePoint share URL into a Quarto embed block.

Usage:
    python3 tools/sharepoint_embed.py "<share-url>" [--typing] [--title "Heading"]

The share URL is the one from OneDrive's "Copy link" (looks like
https://<tenant>-my.sharepoint.com/:x:/g/personal/<user>/IQ...?e=xxxx).
The complete sharing URL is retained because its token grants anonymous access.
"""
import argparse


def embed_block(url: str, title: str | None, typing: bool, active_cell: str | None) -> str:
    separator = "&" if "?" in url else "?"
    src = url + separator + "action=embedview"
    src += "&AllowTyping=True" if typing else "&wdAllowInteractivity=False"
    if active_cell:
        src += f"&ActiveCell={active_cell}"
    src += "&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True"

    head = f"::: {{.callout-tip collapse=\"true\"}}\n## {title}\n" if title else ""
    tail = ":::\n" if title else ""
    return (
        "::: {.workbook-callout}\n"
        f"{head}"
        "::: {.excel-embed}\n"
        f'<iframe width="402" height="346" frameborder="0" scrolling="no" src="{src}"></iframe>\n'
        ":::\n\n"
        f"{tail}"
        ":::\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="OneDrive/SharePoint share URL")
    ap.add_argument("--title", help="Heading for the collapsible dropdown")
    ap.add_argument("--typing", action="store_true", help="allow typing in the embed")
    ap.add_argument("--active-cell", help="e.g. 'Sheet1'!A1")
    a = ap.parse_args()

    print(embed_block(a.url, a.title, a.typing, a.active_cell))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
