import requests
import json

# Local URL for testing (using port 10001 where reload is enabled)
URL = "http://127.0.0.1:10001/get-schemes"

def test_startup_discovery():
    # User from Delhi (should NOT match UP startup policy criteria)
    payload = {
        "occupation": "entrepreneur",
        "state": "Delhi",
        "startup_stage": "prototype"
    }
    print(f"\n--- TESTING STARTUP DISCOVERY (NON-MATCHING PROFILE) ---")
    response = requests.post(URL, json=payload)
    if response.status_code == 200:
        results = response.json()
        print(f"Matched {len(results)} schemes.")
        
        # Check if UP Startup Policy is present
        up_startup = next((res for res in results if "UP Startup Policy" in res['scheme_name']), None)
        if up_startup:
            print(f"FOUND: {up_startup['scheme_name']}")
            print(f"- Match Type: {up_startup['match_type']}")
            print(f"- Reason: {up_startup['match_reason']}")
        else:
            print("FAILED: UP Startup Policy not found in results.")
            
        # Check if other startups are present
        for res in results:
            if "Startup" in res['scheme_name'] or "Innovation" in res['scheme_name']:
                print(f"FOUND: {res['scheme_name']} ({res['match_type']})")
    else:
        print(f"ERROR: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_startup_discovery()
