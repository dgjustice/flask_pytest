"""Run the development server."""
from src.app import create_app

def main():
    """Kick the tires, light the fires."""
    app = create_app()
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()
