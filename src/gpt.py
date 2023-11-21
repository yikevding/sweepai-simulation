from openai import AsyncOpenAI


def chatGPT(request):
    api_key = "PUT YOUR OPEN AI KEY here"
    client = AsyncOpenAI(api_key=api_key)
    prompt = "Only reply the Python code. "+request
    completion = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content
