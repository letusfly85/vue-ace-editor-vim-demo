# Web Server Gateway Interface

from app.server import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, use_reloader=True)