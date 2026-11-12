from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

print("Nova AI is Online!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Nova: Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Your name is Nova. You are a friendly AI assistant."},
                {"role": "user", "content": user}
            ]
        )

        print("Nova:", response.choices[0].message.content)

    except Exception as e:
        print("Nova: Error:", e)