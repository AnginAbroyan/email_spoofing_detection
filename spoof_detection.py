from emailSpoofDetection import emailSpoofDetection
import sys

if len(sys.argv) < 2:
    print("Usage: python spoof_detection.py <email_header_file>")
    sys.exit(1)

email_header_file = sys.argv[1]

try:
    with open(email_header_file, 'r') as file:
        headers = file.read()

    email_domain = input("Enter the email domain: ")

    detector = emailSpoofDetection(headers, email_domain)
    result = detector

    if 'is_spoofed' in result and result['is_spoofed']:
        print("Email is spoofed. Details:")
        print(result['details'])
    else:
        print("Email is not spoofed.")

except FileNotFoundError:
    print(f"File not found: {email_header_file}")
except Exception as e:
    print(f"An error occurred: {e}")

