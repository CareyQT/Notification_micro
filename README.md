The Notification Micro service is a server that waits for POST requests at app./notification.
There are a couple things that you must know about the microservice, 
You can only send emails from for oregonstate emails, which shouldn't be a problem since everyone has one
The program can send emails to other email services like gmail
You must input you ONID username and password into the microservice, If you want more sercuirty and don't want to hardcode you password you should use os.getenv

exmaple request:
payload = {
        "to": "careyq@oregonstate.edu",
        "from": "careyq@oregonstate.edu", 
        "subject": "Test Email from Microservice",
        "body": "This is a test email sent from the microservice!\n\nIf you receive this, it works!"
    }
    url = f"http://localhost:3000/send_email"
    response = requests.post(url, json=payload)

  example return:
    return jsonify({
            'status': 'success',
            'message': message,
        }), 200
