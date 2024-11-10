import requests
import json
import socket
import sys
import subprocess

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def check_service_status():
    try:
        result = subprocess.run(['systemctl', 'status', 'llama-api'], 
                              capture_output=True, 
                              text=True)
        return result.stdout
    except Exception as e:
        return f"Error checking service status: {e}"

def test_api():
    url = "http://localhost:5000/generate"
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a master of horror storytelling."
            },
            {
                "role": "user",
                "content": "Write a short horror story about a mysterious package."
            }
        ],
        "temperature": 0.8,
        "max_tokens": 256
    }

    print("Running API test...")
    print(f"Checking if port 5000 is open: {check_port(5000)}")
    print("\nService Status:")
    print(check_service_status())
    
    try:
        print("\nAttempting to connect to API...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("API Response:")
        print(json.dumps(response.json(), indent=2))
        return True
    except requests.exceptions.ConnectionError as e:
        print(f"\nConnection Error: {e}")
        print("\nPossible issues:")
        print("1. The service is not running")
        print("2. The service is running but not listening on the expected port")
        print("3. A firewall is blocking the connection")
        print("\nTry these commands to debug:")
        print("sudo systemctl status llama-api")
        print("sudo journalctl -u llama-api -e")
        return False
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return False

if __name__ == "__main__":
    test_api()
