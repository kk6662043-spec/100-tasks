import re
import requests

def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        emails = set(re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            response.text
        ))

        return emails

    except Exception as e:
        print("Error:", e)
        return set()


def extract_emails_from_text(text):
    return set(re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    ))


if __name__ == "__main__":
    print("1. Extract emails from Website")
    print("2. Extract emails from Text")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        url = input("Enter website URL: ")
        emails = extract_emails_from_url(url)

    elif choice == "2":
        text = input("Enter text: ")
        emails = extract_emails_from_text(text)

    else:
        print("Invalid option")
        exit()

    print("\nFound Emails:")
    for email in emails:
        print(email)