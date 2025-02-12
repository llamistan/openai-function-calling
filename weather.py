import json
import pprint
import requests

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Function tool definition
# This tool specifies a function that takes latitude and longitude as input
# and returns the current temperature in Fahrenheit.
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates in Fahrenheit.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {
                        "type": "number",
                        "description": "Latitude of the location",
                    },
                    "longitude": {
                        "type": "number",
                        "description": "Longitude of the location",
                    },
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]


def get_weather(latitude, longitude):
    """Fetch current weather data for given coordinates using Open-Meteo API (Fahrenheit)."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&temperature_unit=fahrenheit"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("\nAPI response:")
        pprint.pprint(data)
        temperature = data.get("current", {}).get("temperature_2m", "N/A")
        return f"The current temperature at latitude {latitude}, longitude {longitude} is {temperature}°F."
    except requests.RequestException as e:
        return f"Error fetching weather data: {str(e)}"


# Function to handle streaming response from OpenAI API
def process_streaming_response(stream):
    """Process streaming response from OpenAI API."""
    final_tool_calls = {}
    print("Streaming response:")

    for chunk in stream:
        delta = chunk.choices[0].delta

        # Check if tool calls are in the response
        if delta.tool_calls:
            for tool_call in delta.tool_calls or []:
                index = tool_call.index

                if index not in final_tool_calls:
                    final_tool_calls[index] = tool_call
                    final_tool_calls[index].function.arguments = ""

                # Append function arguments as they stream in
                final_tool_calls[
                    index
                ].function.arguments += tool_call.function.arguments
                print(
                    f"Tool Call Streaming: {final_tool_calls[
                    index
                ].function.name}"
                )

    return final_tool_calls


# Function to execute tool calls after processing the streaming response
def execute_tool_calls(final_tool_calls):
    """Execute tool calls after streaming is complete."""
    for index, tool_call in final_tool_calls.items():
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        # If the function name matches "get_weather", fetch the weather data
        if function_name == "get_weather":
            result = get_weather(arguments["latitude"], arguments["longitude"])
            print(f"\nResult from get_weather with arguments {arguments}: {result}")

            messages.append({"role": "assistant", "tool_calls": [tool_call]})
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": "get_weather",
                    "content": result,
                }
            )

    return messages


if __name__ == "__main__":
    # Initial user query about the weather
    weather_query = "What is the weather like in Paris and San Francisco today?"
    messages = [
        {
            "role": "user",
            "content": weather_query,
        }
    ]

    # Get streaming response from OpenAI API
    stream = client.chat.completions.create(
        model="gpt-4o", messages=messages, tools=tools, stream=True
    )

    # Process the streamed response to extract tool calls
    final_tool_calls = process_streaming_response(stream)

    # Execute the extracted tool calls
    messages = execute_tool_calls(final_tool_calls)
    print("\nMessages after executing tool calls:")
    pprint.pprint(messages)

    # Get final response from OpenAI after tool execution
    completion = client.chat.completions.create(
        model="gpt-4o", messages=messages, tools=tools
    )

    print("\nFinal response:")
    print(completion.choices[0].message.content)
