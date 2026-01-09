import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import SYS_prompt

from available_functions import available_functions
from functions.call_functions import call_function



def main():


    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=SYS_prompt),
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    if response.function_calls is None:
        print(response.text)
    else:
        response_list=[]
        for element in response.function_calls:
            function_call_result=call_function(element, verbose)
            if function_call_result.parts ==[]:
                raise Exception("The .parts of the function call response should be a non empty list")
            if function_call_result.parts[0].function_response ==None:
                raise Exception(".parts[0].function_response should not be None")
            if function_call_result.parts[0].function_response.response ==None:
                raise Exception(".parts[0].function_response.response should not be None")
            response_list.append(function_call_result.parts[0])
            if verbose==True:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        


    
    



if __name__ == "__main__":
    main()
