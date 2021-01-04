from core.common.app import create_app
from core.app import configure_routes

if __name__ == '__main__':
    app = create_app()
    configure_routes(app)
    app.run(debug=True)

