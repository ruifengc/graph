#!/usr/bin/env python3
"""graph serve — share a built page on the LAN over HTTP.

Usage:
    python3 scripts/serve.py <output.html | directory> [--port 8124]

Serves the directory containing the page (or the directory itself) with
Python's stdlib http.server — zero dependencies. Prints every reachable
LAN URL. Port defaults to 8124 and walks upward when taken. Keeps
running until interrupted; in an agent session start it with
background=true and kill the session when the user is done viewing.

Unauthenticated by design: fine on a trusted LAN for a static page,
not for anything sensitive.
"""
import argparse
import socket
import subprocess
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SKIP_IFACES = ("docker", "br-", "veth", "virbr", "vbox", "lo", "vmnet")


def lan_ips() -> list[str]:
    """Non-loopback IPv4 addresses, preferring physical interfaces."""
    ips: list[str] = []
    try:
        out = subprocess.check_output(
            ["ip", "-4", "-o", "addr", "show", "scope", "global"],
            text=True, stderr=subprocess.DEVNULL,
        )
        for line in out.splitlines():
            parts = line.split()
            if len(parts) < 4 or parts[1].startswith(SKIP_IFACES):
                continue
            ip = parts[3].split("/")[0]
            if ip and not ip.startswith("127."):
                ips.append(ip)
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    if not ips:  # fallback: default-route interface via UDP connect
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("192.0.2.1", 80))
            ips.append(s.getsockname()[0])
            s.close()
        except OSError:
            pass
    return ips


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        sys.stderr.write("[serve] %s %s\n" % (self.address_string(), format % args))
        sys.stderr.flush()


def main() -> int:
    ap = argparse.ArgumentParser(description="Serve a built graph page on the LAN")
    ap.add_argument("path", help="output.html file or directory to serve")
    ap.add_argument("--port", type=int, default=8124,
                    help="port to bind (default 8124; auto-increments when taken)")
    args = ap.parse_args()

    p = Path(args.path).resolve()
    if p.is_file():
        directory, page = p.parent, p.name
    elif p.is_dir():
        directory, page = p, None
    else:
        print(f"error: {args.path} is neither a file nor a directory", file=sys.stderr)
        return 1

    handler = partial(QuietHandler, directory=str(directory))
    port = args.port
    while True:
        try:
            httpd = ThreadingHTTPServer(("0.0.0.0", port), handler)
            break
        except OSError:
            port += 1

    ips = lan_ips() or ["127.0.0.1"]
    print(f"serving {directory}")
    for ip in ips:
        url = f"http://{ip}:{port}/" + (page if page else "")
        print(f"  {url}")
    print("(Ctrl-C to stop; unauthenticated — trusted LAN only)")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
