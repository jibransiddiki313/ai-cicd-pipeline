import requests
import sys
import os

def review_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1000,
            "messages": [{
                "role": "user",
                "content": f"Review this Python code for bugs, security issues, and improvements. Be concise:\n\n{code}"
            }]
        }
    )

    result = response.json()
    review = result['content'][0]['text']
    print("=" * 50)
    print("AI CODE REVIEW RESULT:")
    print("=" * 50)
    print(review)
    print("=" * 50)

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "app.py"
    review_code(file_path)
