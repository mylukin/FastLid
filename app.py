from flask import Flask, request, jsonify
import fasttext

app = Flask(__name__)

# 加载fastText模型
model = fasttext.load_model("lid.176.bin")

@app.route('/detect_language', methods=['POST'])
def detect_language():
    text = request.json.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # 预测语言
    predictions = model.predict(text, k=1)  # 只返回最有可能的语言
    language = predictions[0][0].replace('__label__', '')
    
    return jsonify({"language": language})

if __name__ == '__main__':
    app.run()

