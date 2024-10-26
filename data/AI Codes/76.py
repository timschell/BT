def markdown_to_html(markdown_text):
    html_text = markdown_text.replace("# ", "<h1>").replace("\n", "</h1>\n")
    html_text = html_text.replace("**", "<b>").replace("__", "<b>")
    html_text = html_text.replace("<b><b>", "<b>").replace("</b></b>", "</b>")
    return html_text

def main():
    print("Markdown to HTML Converter")
    markdown_text = input("Enter markdown text:\n")
    html_text = markdown_to_html(markdown_text)
    print("\nConverted HTML:\n")
    print(html_text)

if __name__ == "__main__":
    main()
