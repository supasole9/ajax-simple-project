from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/greetings":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            my_data = {
                "Samoan": "Talofa",
                "Tongan": "Malo e lelei",
                "Tahitian": "Ia orana",
                "Fijian": "Bula vinaka",
                "Hawaiian": "Aloha",
                "Maori": "Kia ora"
            }
            my_datajson = json.dumps(my_data)
            self.wfile.write(bytes(my_datajson, "utf-8"))
            return
        if self.path == "/farewells":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            my_data = {
                "Samoan": "Ia Fa",
                "Tongan": "Nofo 'alu au'",
                "Tahitian": "Nana",
                "Fijian": "Moce",
                "Hawaiian": "Aloha",
                "Maori": "Ka Kite"
            }
            my_datajson = json.dumps(my_data)
            self.wfile.write(bytes(my_datajson, "utf-8"))
            return
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<strong>Dont entertain any funny ideas!</strong>", "utf-8"))
            return

    def do_POST(self):
        if self.path == "/greetings":
            self.send_response(201)
            return
        else:
            self.send_response(404)
            self.end_headers()
            return

def main():
    listen = ("127.0.0.1", 8000)
    server = HTTPServer(listen, Handler)
    server.serve_forever()
    print("server is running");

main()
