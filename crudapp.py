from app import app
if __name__ == '__main__':
	app.run(debug=True)
if __name__ == '__main__':
	app.debug= True
	from livereload import Server
	server = Server()
	server = Server(app.wsgi_app)
	server.serve()