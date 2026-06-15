from google import genai
from PIL import Image
from io import BytesIO
import os

try:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY environment variable.")

    client = genai.Client(api_key=api_key)
    result = client.models.generate_images(
        model='imagen-3.0-generate-001',
        prompt='A simple coffee cup',
        config=dict(
            number_of_images=1,
            output_mime_type="image/jpeg",
            aspect_ratio="3:4"
        )
    )
    for generated_image in result.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.save('test_coffee.jpg')
        print("SUCCESS! Image saved.")
except Exception as e:
    print("FAILED", str(e))
