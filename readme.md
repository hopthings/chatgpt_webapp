# ChatGPT Web Application

This is a simple web application that uses OpenAI's ChatGPT to generate responses based on user input. The application is built using Flask (Python) as the backend and JavaScript for the frontend.


## Requirements

- Python 3.7 or higher
- Flask
- OpenAI Python library


## Installation

1. Clone the repository:

        git clone https://github.com/hopthings/chatgpt_webapp.git
        cd chatgpt_webapp


2. Install the required packages:

        pip install -r requirements.txt


## API Key

Before running the application, you need to set up your OpenAI API key as an environment variable. Replace `your_api_key_here` with your actual OpenAI API key.

For Unix-based systems (Linux and macOS):

    ```bash
    export OPENAI_API_KEY="your_api_key_here"

## System card

You can modify the behaviour of chatGPT with a system card. It sets the context, tone, or behavior for the AI assistant throughout the conversation. By providing a system card at the beginning of a conversation, users can give high-level guidance to the AI model about how they want the interaction to proceed.

e.g.

    You are a helpful assistant that speaks like Shakespeare.

The example used in the source code is for "chatSEO" a digital marketing expert.  Feel free to modify as meets your own needs. (Note you should also change the title/H1 header in the templates/index.html to match your needs)

To modify the system card, simply change the contents of "system_card.txt"

## Running the Application

After setting the API key environment variable, run the application using the following command:

    python app.py

The application will start on http://0.0.0.0:8080/. Open the link in your browser to interact with the ChatGPT web application.


## Deployment on a Unix server

To deploy the application on a Unix server and make sure it loads on boot, follow these steps:

1. Set up a virtual environment and install the required packages:

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

2. Create a systemd service file:

        sudo nano /etc/systemd/system/chatgpt_webapp.service

3. Add the following content to the service file, replacing your_api_key_here with your actual OpenAI API key and /path/to/chatgpt-webapp with the absolute path to the application directory:

        [Unit]
        Description=ChatGPT Web Application
        After=network.target

        [Service]
        User=your_unix_username
        Environment=OPENAI_API_KEY="your_api_key_here"
        WorkingDirectory=/path/to/chatgpt_webapp
        ExecStart=/path/to/chatgpt_webapp/venv/bin/python app.py
        Restart=always

        [Install]
        WantedBy=multi-user.target

4. Save and close the file.
5. Reload the systemd manager configuration:

        sudo systemctl daemon-reload

6. Enable and start the service:

        sudo systemctl enable chatgpt_webapp
        sudo systemctl start chatgpt_webapp


The ChatGPT web application is now running as a service on your Unix server and will automatically start on boot.