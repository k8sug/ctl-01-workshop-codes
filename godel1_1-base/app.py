import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)
CORS(app) 

# Get environment variables
pod_name = os.getenv('HOSTNAME')
node_name = os.getenv('NODE_NAME')

# Configure logging
logging_level = os.getenv('LOGGING_LEVEL', 'DEBUG').upper()
logging.basicConfig(level=getattr(logging, logging_level))

# Load the tokenizer and model
try:
    logging.info("Loading tokenizer and model...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
    model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
    logging.info("Tokenizer and model loaded successfully.")
except Exception as e:
    logging.error("Error loading tokenizer and model: %s", str(e))
    raise e

def generate(instruction, knowledge, dialog):
    max_length = int(os.getenv('MAX_LENGTH', 128))
    min_length = int(os.getenv('MIN_LENGTH', 8))
    top_p = float(os.getenv('TOP_P', 0.9))
    do_sample = os.getenv('DO_SAMPLE', 'True') == 'True'

    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=max_length, min_length=min_length, top_p=top_p, do_sample=do_sample)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        dialog = data.get('dialog', [])
        if not isinstance(dialog, list):
            return jsonify({"error": "Dialog must be a list of strings"}), 400
        response = generate(instruction, knowledge, dialog)
        return jsonify({
            "response": response,
            "podName": pod_name,
            "nodeName": node_name
        })
    except Exception as e:
        logging.error("Error in /chat endpoint: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    instruction = os.getenv('INSTRUCTION', 'Instruction: given a dialog context, you need to respond empathically.')
    knowledge = os.getenv('KNOWLEDGE', '')
    app.run(host='0.0.0.0', port=5000)
