# Migros Chat Example

A simple chat application example.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [MacOS](#macos)
  - [Windows](#windows)
- [Usage](#usage)
- [License](#license)

## Prerequisites

Before you begin, ensure you have:

- **Python** installed on your system
- A `.env` file in the project root with all required environment variables
  - See `.env.example` for the required fields
- API Keys for:
  - **Hugging Face** - [Create an account here](https://huggingface.co/join)
  - **Pinecone** - [Create an account here](https://www.pinecone.io/)

## Installation

### MacOS

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

### Windows

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

## Usage

[Add instructions on how to run and use the application]

## License

This project is licensed under the MIT License - see the LICENSE file for details.
