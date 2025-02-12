# OpenAI Function Calling Example: Fetching Weather

This Python script is based on the example in [OpenAI's function calling documentation](https://platform.openai.com/docs/guides/function-calling); it demonstrates how to use OpenAI's function calling capabilities to retrieve weather data from the Open-Meteo API based on a natural language query. It streams responses from OpenAI's GPT-4o model and automatically executes relevant API calls to fetch weather data.

## How Function Calling Works

OpenAI's function calling allows the model to recognize when an API call is needed and generate structured arguments automatically. Here's how it works in this script:

1. User Query: The user asks a question like:
     ```"What is the weather like in Paris and San Francisco today?"```

1. Function Definition: The script defines a function (get_weather) and registers it with OpenAI.

1. Streaming Response: GPT-4o processes the input and, if needed, indicates the need to execute function calls.

1. Executing API Call: The script extracts the required parameters, calls the Open-Meteo API, and retrieves the weather data.

1. Final Response: The assistant returns a user-friendly message with the temperature information.

## 🏗️ Setup

1. Clone [this](https://github.com/llamistan/openai-function-calling/tree/main) repo.
     ``` bash
     git clone https://github.com/llamistan/openai-function-calling.git
     ```

1. Navigate inside this repo
     ``` bash
     cd langchain-rag-tutorial
     ```

1. Create a new Python virtual environment.
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

1. Install the packages required for this python envirnoment in `requirements.txt`.
     ``` bash
     pip install -r requirements.txt
     ```

1. Add a `.env` file by copying the `.env.sample` file. Replace the `YOUR_KEY_HERE` in your `.env` file with your OpenAI Key and save the file.
     ```bash
     OPENAI_API_KEY=sk-proj-1ka3d...
     ```

## 🚀 Running the Script

1. Run the command below to ask the LLM fetch the weather for Paris and San Francisco (as defined in `weather_query`).

    ```python
    python weather.py
    ```
