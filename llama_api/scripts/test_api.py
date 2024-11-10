import requests
import json

def test_api():
    url = "http://localhost:5000/generate"
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a master of horror storytelling, specializing in creating suspenseful and dark narratives."
            },
            {
                "role": "user",
                "content": "Write a short horror story about a mysterious package."
            }
        ],
        "temperature": 0.8,
        "max_tokens": 256
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("API Response:")
        print(json.dumps(response.json(), indent=2))
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error testing API: {e}")
        return False

if __name__ == "__main__":
    test_api()
