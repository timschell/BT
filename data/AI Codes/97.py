def generate_html_form(fields):
    form = "<!DOCTYPE html>\n<html>\n<head>\n<title>Form</title>\n</head>\n<body>\n<form>\n"
    for field in fields:
        form += f'<label for="{field}">{field.capitalize()}:</label>\n<input type="text" id="{field}" name="{field}"><br>\n'
    form += '<input type="submit" value="Submit">\n</form>\n</body>\n</html>'
    return form

def main():
    print("HTML Form Generator")
    fields = input("Enter form fields (comma separated): ").split(", ")
    html_form = generate_html_form(fields)
    print("\nGenerated HTML Form:\n")
    print(html_form)

if __name__ == "__main__":
    main()
