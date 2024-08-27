
# Luna

This is a simple chatbot interface built with Streamlit 

## Features

- **Language Selection**: Users can select their input language from a list of supported languages.
- **Real-Time Translation**: Queries entered by the user are translated to English and displayed on the screen.
- **Persistent Chat History**: The chat history is maintained across user interactions.

## Tech Stack

- **Streamlit**: For creating the web interface.
- **Google Cloud Translate API**: For translating text between languages.
- **Python-dotenv**: For managing environment variables securely.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- A Google Cloud account with access to the Google Translate API

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/translator-chatbot.git
   cd translator-chatbot
   ```

2. **Set Up Google Translate API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (or select an existing one).
   - Enable the **Google Cloud Translation API** for your project.
   - Create credentials for the API by navigating to **APIs & Services > Credentials > Create Credentials** and choose **API Key**.
   - Copy the API key.

3. **Create a `.env` File**:
   - In the root of your project directory, create a file named `.env`.
   - Add your API key to this file:

     ```plaintext
     GOOGLE_TRANSLATE_API_KEY=your_api_key_here
     ```

4. **Install Dependencies**:
   - Use the `requirements.txt` file to install all necessary dependencies:

     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Streamlit App**:
   - Start the Streamlit app with the following command:

     ```bash
     streamlit run chatbot.py
     ```

6. **Access the Chatbot**:
   - Open the URL provided by Streamlit in your web browser to interact with the chatbot.

## Supported Languages

This chatbot supports the following languages:

- English (`en`)
- Spanish (`es`)
- French (`fr`)
- German (`de`)
- Italian (`it`)
- Chinese (`zh`)
- Japanese (`ja`)
- Korean (`ko`)
- Hindi (`hi`)

You can easily add more languages by modifying the `SUPPORTED_LANGUAGES` dictionary in the `chatbot.py` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Steps Breakdown:

1. **Clone the Repository**: Explains how to clone the project repository.
2. **Set Up Google Translate API**: Guides users through setting up a Google Cloud project, enabling the Translate API, and generating an API key.
3. **Create a `.env` File**: Instructions for storing the API key securely using `python-dotenv`.
4. **Install Dependencies**: Explains how to install necessary Python packages using `requirements.txt`.
5. **Run the Streamlit App**: Provides the command to run the Streamlit app and start interacting with the chatbot.

This `README.md` should provide a clear and concise guide for anyone who wants to set up and run your language translator chatbot.
