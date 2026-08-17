#!/usr/bin/env python3
"""Turn a OneDrive/SharePoint share URL into a Quarto embed block.

Usage:
    python3 tools/sharepoint_embed.py "<share-url>" [--typing] [--title "Heading"]

The share URL is the one from OneDrive's "Copy link" (looks like
https://<tenant>-my.sharepoint.com/:x:/g/personal/<user>/IQ...?e=xxxx).
The document GUID is encoded (little-endian) at byte offset 2 of the
base64url token, which is what this extracts.
"""
import argparse, base64, re, sys, uuid

BASE = ("https://usaskca1-my.sharepoint.com/personal/pjs998_usask_ca/"
        "_layouts/15/Doc.aspx?sourcedoc=%7B{guid}%7D")


def guid_from_share_url(url: str) -> str:
    token = url.split("/")[-1].split("?")[0]
    raw = base64.urlsafe_b64decode(token + "=" * (-len(token) % 4))
    return str(uuid.UUID(bytes_le=raw[2:18]))


def embed_block(guid: str, title: str | None, typing: bool, active_cell: str | None) -> str:
    src = BASE.format(guid=guid) + "&action=embedview"
    src += "&AllowTyping=True" if typing else "&wdAllowInteractivity=False"
    if active_cell:
        src += f"&ActiveCell={active_cell}"
    src += "&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True"
    copy_url = BASE.format(guid=guid) + "&action=default&Copy=1"

    head = f"::: {{.callout-tip collapse=\"true\"}}\n## {title}\n" if title else ""
    tail = ":::\n" if title else ""
    return (
        "::: {.workbook-callout}\n"
        f"{head}"
        "::: {.excel-embed}\n"
        f'<iframe width="402" height="346" frameborder="0" scrolling="no" src="{src}"></iframe>\n'
        ":::\n\n"
        f"[Open an editable copy]({copy_url}) — opens your own editable copy in "
        "Excel for the web (Microsoft sign-in required).\n"
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

    guid = guid_from_share_url(a.url)
    print(f"# GUID: {guid}\n", file=sys.stderr)
    print(embed_block(guid, a.title, a.typing, a.active_cell))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
