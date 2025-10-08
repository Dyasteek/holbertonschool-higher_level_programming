import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data: dict, status_code: int = 200) -> None:
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, text: str, status_code: int = 200) -> None:
        body = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")
            return

        if self.path == "/data":
            self._send_json({
                "name": "John",
                "age": 30,
                "city": "New York",
            })
            return

        if self.path == "/status":
            self._send_text("OK")
            return

        self._send_text("Endpoint not found", status_code=404)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port: int = 8000) -> None:
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run(port=8000)



