from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

# Load the Model and Tokenizer
print("Loading AI model... please wait.")
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Conversation history stored in memory (shared for this simple version)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    global conversation_history
    
    # Read prompt from HTTP request body
    data = request.get_json()
    if not data or "prompt" not in data:
        return "Error: No prompt provided", 400
        
    input_text = data["prompt"]

    # Keep only the recent conversation (sliding window of 6 turns)
    conversation_history[:] = conversation_history[-6:]

    # Create conversation history string
    history = "\n".join(conversation_history)
    prompt = history + f"\nUser: {input_text}\nBot:"

    # Tokenize the input
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Generate the response
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        no_repeat_ngram_size=3,
        repetition_penalty=1.3,
        do_sample=True,
        temperature=0.6,
        top_p=0.85
    )

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(f"User: {input_text}")
    conversation_history.append(f"Bot: {response}")

    return response

if __name__ == '__main__':
    # Use port 5000 for local development
    app.run(host='0.0.0.0', port=5000, debug=True)
