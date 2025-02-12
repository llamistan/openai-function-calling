# OpenAI Function Calling Example: Fetching Weather

This Python script demonstrates how to use OpenAI's function calling capabilities to retrieve weather data from the Open-Meteo API based on user queries. It is inspired by the example in [OpenAI's function calling documentation](https://platform.openai.com/docs/guides/function-calling). It streams responses from OpenAI's GPT-4o model and automatically executes relevant API calls to fetch weather data.

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

## 📊 Example Output

```
Streaming response:
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather
Tool Call Streaming: get_weather

API response:
{'current': {'interval': 900,
             'temperature_2m': 42.1,
             'time': '2025-02-12T19:30'},
 'current_units': {'interval': 'seconds',
                   'temperature_2m': '°F',
                   'time': 'iso8601'},
 'elevation': 36.0,
 'generationtime_ms': 0.015616416931152344,
 'latitude': 48.86,
 'longitude': 2.3599997,
 'timezone': 'GMT',
 'timezone_abbreviation': 'GMT',
 'utc_offset_seconds': 0}

Result from get_weather with arguments {'latitude': 48.8566, 'longitude': 2.3522}: The current temperature at latitude 48.8566, longitude 2.3522 is 42.1°F.

API response:
{'current': {'interval': 900,
             'temperature_2m': 49.7,
             'time': '2025-02-12T19:30'},
 'current_units': {'interval': 'seconds',
                   'temperature_2m': '°F',
                   'time': 'iso8601'},
 'elevation': 18.0,
 'generationtime_ms': 0.009775161743164062,
 'latitude': 37.763283,
 'longitude': -122.41286,
 'timezone': 'GMT',
 'timezone_abbreviation': 'GMT',
 'utc_offset_seconds': 0}

Result from get_weather with arguments {'latitude': 37.7749, 'longitude': -122.4194}: The current temperature at latitude 37.7749, longitude -122.4194 is 49.7°F.

Messages after executing tool calls:
[{'content': 'What is the weather like in Paris and San Francisco today?',
  'role': 'user'},
 {'role': 'assistant',
  'tool_calls': [ChoiceDeltaToolCall(index=0, id='call_63xV4oDmdmmS2i2Ix1TGQYdh', function=ChoiceDeltaToolCallFunction(arguments='{"latitude": 48.8566, "longitude": 2.3522}', name='get_weather'), type='function')]},
 {'content': 'The current temperature at latitude 48.8566, longitude 2.3522 is '
             '42.1°F.',
  'name': 'get_weather',
  'role': 'tool',
  'tool_call_id': 'call_63xV4oDmdmmS2i2Ix1TGQYdh'},
 {'role': 'assistant',
  'tool_calls': [ChoiceDeltaToolCall(index=1, id='call_9VWb51HhP60tRwfaudwFrsCV', function=ChoiceDeltaToolCallFunction(arguments='{"latitude": 37.7749, "longitude": -122.4194}', name='get_weather'), type='function')]},
 {'content': 'The current temperature at latitude 37.7749, longitude -122.4194 '
             'is 49.7°F.',
  'name': 'get_weather',
  'role': 'tool',
  'tool_call_id': 'call_9VWb51HhP60tRwfaudwFrsCV'}]

Final response:
The current weather is as follows:
- In Paris, the temperature is 42.1°F.
- In San Francisco, the temperature is 49.7°F.
```