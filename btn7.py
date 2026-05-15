from openai import OpenAI
import os
client = OpenAI(
    api_key='',
    base_url="https://api.groq.com/openai/v1",
)




async def aichat(vopros):
    response = client.responses.create(
        input=vopros,
        model="openai/gpt-oss-20b",
    )
    return response.output_text