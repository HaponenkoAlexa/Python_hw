def clean_html_tags(input_file, output_file="cleaned_text.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            content = infile.read()

            import re
            clean_text = re.sub(r"<.*?>", "", content)

            clean_text = "\n".join(line for line in clean_text.splitlines() if line.strip())

            with open(output_file, "w", encoding="utf-8") as outfile:
                outfile.write(clean_text)

        print(f"Очищений текст збережено у файлі: {output_file}")

    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")

clean_html_tags("draft.html", "cleaned_text.txt")
