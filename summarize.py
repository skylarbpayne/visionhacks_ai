from mirascope import llm, prompt_template
from dotenv import load_dotenv
import argparse
from docling.document_converter import DocumentConverter
import os


load_dotenv()


@llm.call(provider='google', model='gemini-2.5-flash')
@prompt_template("""
Summarize the following article into 5 bullet points.
                 
<article>
{article}
</article>
""")
def summarize(article: str): ...


def get_article_content(url: str) -> str:
    """Uses docling to convert the article to markdown"""
    converter = DocumentConverter()
    result = converter.convert(url)
    return result.document.export_to_markdown()


def main():
    parser = argparse.ArgumentParser('Article Summarizer')
    parser.add_argument('--url', type=str, required=True)
    args = parser.parse_args()
    assert os.getenv('GOOGLE_API_KEY'), "GOOGLE_API_KEY is not set"
    article = get_article_content(args.url)
    summary = summarize(article)
    print(summary.content)


if __name__ == "__main__":
    main()