from flask import Flask, request, jsonify
import smtplib

from email.mime.multipart import MIMEMultipart




app = Flask(__name__)

#Email configuration

#
def send_email(recipient, subject, body, from_email):
    try:
        

        message = f"Subject: {subject}\n\n{body}"
        
        # Connect to SMTP server and send
        server = smtplib.SMTP_SSL("mail.engr.oregonstate.edu", 465)
       

       #add you ONID Username and password
       #do not add oregonstate.edu to the end of your username
        username = ("careyq example")
        password = ("example_password")

        server.login(username, password)  # Use environment variables!
        server.sendmail(from_email, recipient, message)
        server.quit()
        
        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)

def check(success, message):
    if success:
        return jsonify({
            'status': 'success',
            'message': message,
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': message
        }), 500



        
@app.route('/send_email', methods=['POST'])
def send_email_endpoint():
    try:
        info = request.get_json()

        if not info:
            return jsonify({'error': 'No JSON data provided'}), 400
        #populate who were sending it to
        recipient = info.get('to')

       
        from_email = info.get('from')

        subject = info.get('subject')
        body = info.get('body')
       
        
       
        if not recipient or not subject or not body:
            return jsonify({
                'error': 'Missing required fields: to, subject, body'
            }), 400
        
        success, message = send_email(recipient, subject, body, from_email)
        return check(success, message)
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Internal error: {str(e)}'
        }), 500




if __name__ == '__main__':
    print("Starting Email Microservice...")
    app.run(host='0.0.0.0', port=3000, debug=True)