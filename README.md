# Migros Chat Example

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A simple chat application example that demonstrates how to build an interactive AI-powered chat interface.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [MacOS](#macos)
  - [Windows](#windows)
- [Usage](#usage)
- [Features](#features)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## 🔍 Overview {#overview}

This application provides a user-friendly chat interface powered by AI models from Hugging Face and vector storage from Pinecone. Use it to experiment with conversational AI or as a starting point for your own projects.

## 🛠️ Prerequisites {#prerequisites}

Before you begin, ensure you have:

- **Python 3.7+** installed on your system
- A `.env` file in the project root with all required environment variables
  - See `.env.example` for the required fields
- API Keys for:
  - **Hugging Face** - [Create an account here](https://huggingface.co/join)
    - **User permissions** - Set following permissions:
      - Make calls to Inference Providers
      - Make calls to your Inference Endpoints
  - **Pinecone** - [Create an account here](https://www.pinecone.io/)

## 💻 Installation {#installation}

Ensure your terminal is set to the root of this project e.g. if you have copied it to C:/Documents/development/migros-chat-example your terminal should be pointed at that path.

```bash
cd C:/Documents/development/migros-chat-example
```

### MacOS {#macos}

1. Create a local virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

3. Verify the virtual environment is activated:

   ```bash
   which python
   ```

   You should see a path like: `migros-chat-example/.venv/bin/python`

4. Install required dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

### Windows {#windows}

1. Create a local virtual environment:

   ```bash
   py -m venv .venv
   ```

2. Activate the virtual environment:

   ```bash
   .venv\Scripts\activate
   ```

3. Verify the virtual environment is activated:

   ```bash
   where python
   ```

   You should see a path like: `migros-chat-example\.venv\Scripts\python.exe`

4. Install required dependencies:

   ```bash
   py -m pip install -r requirements.txt
   ```

## 🚀 Usage {#usage}

Run the following command in your terminal:

```bash
streamlit run streamlit.py
```

Then open your browser and navigate to `http://localhost:8501` to see the application in action.

## ✨ Features {#features}

- Interactive chat interface built with Streamlit
- AI-powered responses using Hugging Face models
- Persistent conversation history
- Vector storage with Pinecone for efficient retrieval

## ❓ Troubleshooting {#troubleshooting}

**API Key Issues**

- Ensure your API keys are correctly set in the `.env` file
- Check that your Hugging Face account has the necessary permissions enabled

**Installation Problems**

- Make sure you're using Python 3.7 or higher
- Try reinstalling dependencies with `pip install -r requirements.txt --force-reinstall`

**Application Errors**

- Check the console output for specific error messages
- Ensure all required services (Hugging Face, Pinecone) are accessible

## 📄 License {#license}

This project is licensed under the MIT License - see the LICENSE file for details.
