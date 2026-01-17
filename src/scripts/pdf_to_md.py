from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from pathlib import Path

def pdf_to_markdown(pdf_path: str, output_dir: str):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    converter = PdfConverter(
                artifact_dict=create_model_dict(),
                )
    rendered = converter(str(pdf_path))

    markdown, metadata, images = text_from_rendered(rendered)

    md_path = output_dir/ f"{pdf_path.stem}.md"
    md_path.write_text(markdown, encoding="utf-8")

    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)

    for name, image in images.items():
        image_path = images_dir / name
        image.save(image_path)

    return md_path

if __name__ == "__main__":
    pdf_to_markdown(
        pdf_path="data/raw/handbook.pdf",
        output_dir="data/processed"
    )
