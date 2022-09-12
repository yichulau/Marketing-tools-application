
import os
from urllib import response
import openai
import pandas
import argparse
import re
from dotenv import load_dotenv

load_dotenv()
MAX_INPUT_LENGTH=64

def main():
    print("Running a Main function")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")

    if validate_length(user_input):
        generate_branding_snippet(user_input, OPENAI_API_KEY)   
        generate_keywords(user_input, OPENAI_API_KEY)

    else:
        raise ValueError(f"Input length is too long, must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")    
    # if validate_length(user_input):
    #     branding_result = generate_branding_snippet(user_input, OPENAI_API_KEY)


    # openai_init(user_input)
    # pass


def validate_length(prompt: str):
    return len(prompt) <= MAX_INPUT_LENGTH

def generate_keywords(prompt: str, openai_key):
    openai.api_key = openai_key
    enriched_prompt = f"Generate related branding keywords for {prompt}"
    response = openai.Completion.create(  
                model="davinci-instruct-beta-v3",
                prompt=enriched_prompt,
                temperature=0.6,
                max_tokens=32
                )
    keywords_text : str = response["choices"][0]['text']

    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-",keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    print(f"Genertate keywords {keywords_array}")
    return keywords_array



def generate_branding_snippet(prompt: str,openai_key ):
    openai.api_key = openai_key
    enriched_prompt = f"Generate related branding keywords for {prompt}"
    response = openai.Completion.create(  
                model="davinci-instruct-beta-v3",
                prompt=enriched_prompt,
                temperature=0.6,
                max_tokens=64
                )
    # dasdsds
    # extract output text
    branding_text = response['choices'][0]['text']
    branding_text = branding_text.strip()
    last_char = branding_text[-1]

    # add ... to truncated the statements
    if last_char not in (".","!","?"):
        branding_text += "..."
    print(f"Result {branding_text}")
    return branding_text




if __name__ == "__main__":
    main()