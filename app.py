from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


ROOT = Path(__file__).parent
STATIC_DIR = ROOT / "static"
HOST = "0.0.0.0"
PORT = 8000


class GameHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/index.html"
        return super().do_GET()


def main():
    port = int(os.environ.get("PORT", PORT))
    server = ThreadingHTTPServer((HOST, port), GameHandler)
    print("Sriti Math Game is running!")
    print(f"Open: http://localhost:{port}")
    print(f"Or:   http://127.0.0.1:{port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
