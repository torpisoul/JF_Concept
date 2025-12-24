import os
import glob
from google import genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
client = None
if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
else:
    print("Warning: GEMINI_API_KEY not found in environment variables. Bot will use mock responses.")

def load_documents():
    """
    Loads text content from files in the 'documents' directory.
    """
    docs_content = ""
    docs_dir = "documents"

    if os.path.exists(docs_dir):
        files = glob.glob(os.path.join(docs_dir, "*.txt"))
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    docs_content += f"\n--- Content from {os.path.basename(file_path)} ---\n"
                    docs_content += f.read()
                    docs_content += "\n----------------------------------------\n"
                print(f"Loaded document: {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    else:
        print(f"Directory '{docs_dir}' not found. No external documents loaded.")

    return docs_content

# Base Context
BASE_CONTEXT = """
You are a helpful assistant for school staff, supporting them with Ofsted-related queries.
You must always use British English spelling (e.g., 'colour' not 'color', 'specialise' not 'specialize').
Base your answers on the provided context if available.
"""

# Load documents on startup
DOCUMENT_CONTEXT = load_documents()

# Combine context
CONTEXT = BASE_CONTEXT + "\n\n" + DOCUMENT_CONTEXT

def get_gemini_response(user_question):
    """
    Sends the user question to Gemini API and returns the response.
    """
    if not client:
        return "I am a mock bot. Please set the GEMINI_API_KEY to get real answers. (British English check: colour)"

    try:
        # Construct the prompt with context
        prompt = f"{CONTEXT}\n\nUser Question: {user_question}"

        response = client.models.generate_content(
            model='gemini-1.5-flash', contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    bot_response = get_gemini_response(user_message)

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
