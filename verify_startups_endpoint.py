import requests

# Local URL for testing (using port 10001 where reload is enabled)
URL = "http://127.0.0.1:10001/startups"

def test_get_startups():
    print(f"\n--- TESTING GET ALL STARTUPS ---")
    response = requests.get(URL)
    if response.status_code == 200:
        results = response.json()
        print(f"Retrieved {len(results)} startup schemes.")
        for res in results:
            print(f"- {res['scheme_id']}: {res['scheme_name']}")
    else:
        print(f"ERROR: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_get_startups()
