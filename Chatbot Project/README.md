# Cravy Med Chatbot Project
This project is a **Fast Food Restaurant Chatbot** built using **Dialogflow** for natural language processing, **FastAPI** for the backend, **MySQL** for the database, and a **static HTML/CSS** frontend. The chatbot allows users to place orders, check order status, and interact with the restaurant's menu.

## Project Structure
The project is organized into four main folders:
1. `backend`: Contains the FastAPI backend code.
2. `frontend`: Contains the static website (HTML and CSS files).
3. `db`: Contains the MySQL database schema and setup files.
4. `dialogflow`: Contains exported Dialogflow intents and entities in .txt and .json files.

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **MySQL Workbench**
- **Dialogflow Account**

## Setup Instructions
### 1. Dialogflow Setup
 1. Go to the [Dialogflow Console](https://dialogflow.cloud.google.com/).
 2. Create a new agent.
 3. Import the intents and entities from the `dialogflow` folder:
    - Navigate to **Intents** and click **Import**.
    - Upload the `.json` files from the `dialogflow/intents/` folder.
    - Repeat the same for **Entities** using the files in the `dialogflow/entities/` folder.
 4. Enable the **Webhook** Fulfilment:
    - Place the URL that you will get from `ngrok` after running backend.
 5. Enable the **Dialogflow Web Demo** integration:
    - Go to **Integrations → Web Demo**.
    - Copy the embed code and paste it into the **frontend/index.html** file.

### 2. Database Setup
 1. Create a MySQL database:
    ```
    CREATE DATABASE cravy_med;
    ```
 2. Import the database schema:
    - Navigate to the `db` folder.
    - Run the following command to import the schema:
        ```
        mysql -u <username> -p cravy_med < database_schema.sql
        ```
 3. Create a `.env` file in the `backend` folder with the following content:
    ```
    DB_HOST=localhost
    DB_USER=<your_mysql_username>
    DB_PASSWORD=<your_mysql_password>
    DB_NAME=cravy_med
    ```

### 3. Backend Setup
 1. Navigate to the `backend` folder:
    ```
    cd backend
    ```
 2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
 3. Run the FastAPI server:
    ```
    uvicorn main:app --reload
    ```
 4. The backend will be available at `http://127.0.0.1:8000`.
 5. Run the ngrok server to get https protcol url for dialogflow.
    ```
    ngrok http 8000
    ```
    ngrok will give you the random url every time you run the ngrok.

### 4. Frontend Setup
 1. Navigate to the `frontend` folder:
    ```
    cd frontend
    ```
 2. Open the `index.html` file in your browser:
    - You can use a live server extension in VS Code or simply double-click the file.
 3. The chatbot will be embedded on the website.

## How to Use the Chatbot
1. Open the `index.html` file in your browser.
2. Interact with the chatbot using the following commands:
    - **Place an order**: "I want to order 2 kebabs and 1 falafel."
    - **Check order status**: "What is the status of my order?"
    - **Start a new order**: "Start a new order."
    - **Remove items**: "Remove kebabs from my order."
    - **Store hours**: "Are you open?"
3. The chatbot will guide you through the ordering process.

## Running the Project
1. Start the backend server
    ```
    cd backend
    uvicorn main:app --reload
    ```
2. Open the other terminal and run ngrok.
    ```
    ngrok http 8000
    ```
2. Open the frontend in your browser:
    - Navigate to `frontend/index.html`.
3. Interact with the chatbot on the website.

---
Enjoy using the **Cravy Med Chatbot!** 🍔🤖