# FastAPI Backend for Cravy Chatbot and Cravy-Med Restaurant
This repository contains the backend implementation for the Cravy Chatbot and Cravy-Med Restaurant web application using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## Installation
1. Navigate to the project backend directory:
    ```
    cd <project-folder>
    ```
2. Install the required libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```
    This will install:
     - `fastapi[all]`: FastAPI framework with all optional dependencies.
     - `mysql-connector-python`: MySQL database connector for Python.
3. [Ngork](https://ngrok.com/downloads/windows?tab=download) to expose your local server to the internet:
    - Download Ngrok from [https://ngrok.com/download].
    - Follow the installation instructions for your operating system.
    - Authenticate Ngrok by running:
        ```
        ngrok authtoken <your-auth-token>
        ```
        Replace `<your-auth-token>` with the token provided on the Ngrok dashboard [https://dashboard.ngrok.com/get-started/your-authtoken].

## Running the Application
1. Navigate to the `backend` folder:
    ```
    cd backend
    ```

2. Start the FastAPI server using **Uvicorn**:
    ```
    uvicorn main:app --reload
    ```
    - **Uvicorn** is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation for Python web applications. It is used to serve FastAPI applications because FastAPI is built on ASGI.

    - The `--reload` flag enables auto-reloading of the server whenever you make changes to your code. This is especially useful during development, as you don’t need to manually restart the server every time you update your files.

## Exposing Your Local Server with Ngrok
Since **Dialogflow** requires a secure HTTPS URL for webhooks and FastAPI runs on HTTP by default, we use **Ngrok** to create a secure tunnel to expose your local server to the internet.
1. Start your FastAPI server using Uvicorn (as shown above).
2. Open a new terminal window and run the following command to start Ngrok: 
    ```
    ngrok http 8000
    ```  
    This will create a secure HTTPS tunnel to your local server running on port 8000.
3. **Ngrok** will provide you with a public HTTPS URL (e.g., `https://<random-subdomain>.ngrok-free.app`). Use this URL as the webhook URL in your **Dialogflow** agent settings.
4. You can inspect incoming requests and responses by visiting the Ngrok web interface at `http://127.0.0.1:4040`.



### Why Use Ngrok for Dialogflow?
- **HTTPS Requirement:** Dialogflow requires webhook URLs to use HTTPS, but FastAPI runs on HTTP by default during development. Ngrok provides an HTTPS URL that forwards requests to your local HTTP server.

- **Testing Webhooks:** Ngrok allows you to test your Dialogflow webhook integration locally without deploying your backend to a live server.

- **Debugging:** Ngrok provides a detailed inspection interface to monitor incoming requests and responses, making it easier to debug issues.

## Accessing the Application
Once the server is running, you can access the following:

- **FastAPI Docs (Swagger UI):**
Open your browser and go to:
`http://127.0.0.1:8000/docs`

- **ReDoc Documentation:**
Open your browser and go to:
`http://127.0.0.1:8000/redoc`

- **API Endpoints:**
The API will be available at:
`http://127.0.0.1:8000`

- **Ngrok Public URL (for Dialogflow Webhook):**
Use the Ngrok HTTPS URL provided in the terminal (e.g., `https://<random-subdomain>.ngrok-free.app`).