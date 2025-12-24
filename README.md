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

## GitHub Pages Deployment

To host this application on GitHub Pages (which only supports static sites), use the contents of the `gh_pages/` directory.

1.  **Context**: The build process (or manual setup) must concatenate all text files from `documents/` into `gh_pages/context.txt` so the static site can load them.
    ```bash
    cat documents/*.txt > gh_pages/context.txt
    ```
2.  **Deploy**: Upload the contents of the `gh_pages/` folder to your GitHub repository (e.g., to the `main` branch or a `gh-pages` branch) and enable GitHub Pages in the repository settings.
3.  **API Key**: Since GitHub Pages is a static host, there is no secure backend to store your API Key. The user interface includes an input field for the user to enter their own API Key. **Do not hardcode your API Key in the HTML/JS files if the repository is public.**
