from flask import Flask, request, jsonify
import fasttext
import re
import html

app = Flask(__name__)

# Load FastText model
try:
    model = fasttext.load_model("lid.176.bin")
except Exception as e:
    print(f"Model loading error: {e}")
    model = None

def clean_text(text):
    """
    Clean text by removing HTML tags and normalizing whitespace
    """
    if not text:
        return ""
    
    # Unescape HTML entities and Unicode escapes
    text = html.unescape(text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

@app.route('/detect_language', methods=['POST'])
def detect_language():
    try:
        if not model:
            return jsonify({"error": "Language detection model failed to load"}), 500

        if not request.is_json:
            return jsonify({"error": "Request must be JSON format"}), 400

        text = request.json.get('text')
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Clean text
        cleaned_text = clean_text(text)
        if not cleaned_text:
            return jsonify({"error": "Cleaned text is empty"}), 400

        # Predict language
        predictions = model.predict(cleaned_text, k=1)
        language = predictions[0][0].replace('__label__', '')
        confidence = float(predictions[1][0])

        return jsonify({
            "language": language,
            "confidence": confidence,
            "processed_text": cleaned_text,
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": f"An error occurred during processing: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()