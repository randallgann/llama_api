import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.api import app

if __name__ == "__main__":
    print("Starting debug server...")
    print("API will be available at http://localhost:5000")
    app.run(host='localhost', port=5000, debug=True)
