import requests
import sys
import os

def review_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1000,
            "messages": [{
                "role": "user",
                "content": f"Review this Python code briefly:\n\n{code}"
            }]
        }
    )

    result = response.json()
    print("API Response Status:", response.status_code)
    
    if 'error' in result:
        print("API Error:", result['error'])
        sys.exit(1)
    
    review = result['content'][0]['text']
    print("=" * 50)
    print("AI CODE REVIEW RESULT:")
    print("=" * 50)
    print(review)
    print("=" * 50)

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "app.py"
    review_code(file_path)
