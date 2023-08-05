**Chat with PDF GitHub Repository - README**

# Chat with PDF

This is a simple application that allows you to chat with a PDF file. The application is built using Streamlit and utilizes the OpenAI API for natural language processing. Before running the application, make sure you have obtained an API key from OpenAI and paste it into the `secret.py` file as instructed below.

## Prerequisites

1. You must have Python 3.x installed on your system.

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yogeshumalkar11/chat-with-pdf.git
cd chat-with-pdf
```

2. Install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

## Obtaining OpenAI API Key

Before you can use this application, you need to obtain an API key from OpenAI. Follow these steps to get your API key:

1. Go to the [OpenAI website](https://openai.com) and sign up for an account if you don't have one already.

2. Once logged in, navigate to the API section or visit the [API settings page](https://platform.openai.com/signup). Obtain your API key from there.

3. Copy your API key.

4. In the file nameed `secret.py` in the root directory of the project, paste your API key in it as follows:

```python
# secret.py

# Paste your OpenAI API key here
OPENAI_API_KEY = "YOUR_API_KEY_HERE"
```

**IMPORTANT:** Keep your API key safe and do not share it publicly.

## Running the Application

Once you have set up the API key, you can now run the application using the following command:

```bash
streamlit run main.py
```

The application will launch in your default web browser. You can now upload a PDF file (up to 200MB) and start chatting with it using natural language queries.

## Limitations

- The application only supports PDF files up to 200MB in size. Larger files may cause issues.

## Contributing

Contributions to this project are welcome. Feel free to submit a pull request if you have any improvements or bug fixes to suggest.


---

Thank you for using our Chat with PDF application! If you encounter any issues or have suggestions for improvement, please feel free to raise an issue on GitHub or contact us. We hope you find this tool helpful!