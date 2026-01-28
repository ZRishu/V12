import os
import sys
import argparse
from openai import OpenAI

# Initialize client (Ensure OPENAI_API_KEY is set in your environment variables)
client = OpenAI()

def get_system_prompt():
    """
    This is the 'Compiler' logic. We instruct the LLM to behave 
    strictly as a code translator, not a chatbot.
    """
    return (
        "You are a C to JavaScript transpiler. \n"
        "Rules:\n"
        "1. Receive C code and output EQUIVALENT modern JavaScript (ES6+).\n"
        "2. Do NOT add explanations, markdown formatting, or triple backticks.\n"
        "3. Handle memory management logic by converting it to JS logic (e.g., arrays/objects).\n"
        "4. If a standard C library is used, implement a simple JS polyfill or equivalent logic.\n"
        "5. Output PURE code only."
    )

def transpile_code(c_code):
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Or gpt-3.5-turbo / other models
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": c_code}
            ],
            temperature=0.0 # Keep temperature low for deterministic code generation
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during API call: {e}")
        sys.exit(1)

def main():
    # 1. Parse Arguments
    parser = argparse.ArgumentParser(description="LLM-based C to JS Transpiler")
    parser.add_argument("input_file", help="Path to the .c file")
    args = parser.parse_args()

    # 2. Read C File
    if not os.path.exists(args.input_file):
        print(f"Error: File {args.input_file} not found.")
        sys.exit(1)

    with open(args.input_file, "r") as f:
        c_code = f.read()

    print(f"Compiling {args.input_file} to JavaScript...")

    # 3. Transpile via LLM
    js_code = transpile_code(c_code)

    # 4. Clean up output (Safety measure in case LLM adds markdown)
    # Sometimes LLMs ignore the 'no markdown' rule, so we strip it manually.
    js_code = js_code.replace("```javascript", "").replace("```", "").strip()

    # 5. Write JS File
    output_filename = args.input_file.replace(".c", ".js")
    with open(output_filename, "w") as f:
        f.write(js_code)

    print(f"Success! Output saved to: {output_filename}")

if __name__ == "__main__":
    main()