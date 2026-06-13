from google import genai

try:
    client = genai.Client(api_key="AQ.Ab8RN6IXOoK5MY2AL5mqsS3GPLDe7q1SQ--wE7VUB4S_9WcaCg")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='say hi'
    )
    print("SUCCESS", response.text)
except Exception as e:
    print("FAILED", str(e))
