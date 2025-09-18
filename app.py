from flask import Flask, request, jsonify, render_template
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
import torch
import language_tool_python # <-- IMPORT THE NEW LIBRARY

# Initialize the Flask application
app = Flask(__name__)

# --- Load the AI model and tokenizer ---
MODEL_PATH = './my_essay_grader_model'
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# --- Initialize the Grammar Checking Tool ---
# This will download the language data on its first run
tool = language_tool_python.LanguageTool('en-US')


# --- Define the routes for the web application ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])
def grade_essay():
    try:
        data = request.json
        essay = data['essay']

        # --- 1. Get the Score (Same as before) ---
        inputs = tokenizer(essay, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            score = outputs.logits.item()
        
        min_score, max_score = 2, 12
        scaled_score = 100 * (score - min_score) / (max_score - min_score)
        scaled_score = round(max(0, min(100, scaled_score)))

        # --- 2. Get Grammar Feedback (New Part) ---
        matches = tool.check(essay)
        feedback = []
        for rule in matches:
            # We'll only show a few pieces of feedback to keep it clean
            if len(feedback) < 5:
                feedback.append(rule.message)

        # --- 3. Return BOTH score and feedback ---
        return jsonify({
            'score': scaled_score,
            'feedback': feedback
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)