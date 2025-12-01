import requests
import json

# Microservice URL
BASE_URL = "http://localhost:3000"

def test_send_email():
    """Test sending a single email"""
    print("\n" + "="*50)
    print("TEST 1: Send Single Email")
    print("="*50)
    
    url = f"{BASE_URL}/send_email"
    
    payload = {
        "to": "careyq@oregonstate.edu",
        "from": "careyq@oregonstate.edu", 
        "subject": "Test Email from Microservice",
        "body": "This is a test email sent from the microservice!\n\nIf you receive this, it works!"
    }
    
    try:
        print(f"Sending request to: {url}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(url, json=payload)
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("SUCCESS: Email sent successfully!")
        else:
            print("❌ FAILED: Email was not sent")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to microservice")
        print("Make sure the microservice is running on port 3000")
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    print("Starting Email Microservice Tests...")
    print("Make sure your microservice is running on http://localhost:3000")
    
    # Run all tests
    test_send_email()