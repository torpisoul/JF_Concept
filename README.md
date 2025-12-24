# Ofsted Support Bot

This is a web portal for answering Ofsted-related questions using the Gemini API.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **API Key**:
    You need a Google Gemini API key. You can set it as an environment variable:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```
    Or create a `.env` file in the root directory:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

3.  **Run the Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://localhost:5000`.

## Documents and Context

To add context (e.g., Ofsted framework, school policies):

1.  Place your `.txt` files in the `documents/` directory.
2.  Restart the application (`python app.py`).

The bot will automatically load all text files in that directory and use them as context for answering questions.

## British English

The bot is instructed to use British English spelling via the system prompt.
