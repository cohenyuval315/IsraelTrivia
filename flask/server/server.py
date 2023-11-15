from app import create_app
import os
from logger import logger

app = create_app()

if __name__ == "__main__":
    logger.info("Initializing app ...")
    app.run(host=os.environ.get("FLASK_SERVER_HOST", '0.0.0.0'), 
            port=os.environ.get("FLASK_SERVER_PORT", 5000), 
            debug=True)