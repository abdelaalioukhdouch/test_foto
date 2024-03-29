from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
	"""docstring for Serv"""
	def do_Get(self):
		if self.path == '/':
			self.path = '/index.html'

		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "Error"
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))
		httpd = HTTPServer(('localhost', 88), Serv)
		httpd.serve_forever()