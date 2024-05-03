from .abstract import TextGenerationAPI


class OpenAIAPI(TextGenerationAPI):
    def __init__(self, client):
        self.client = client

    async def generate_text(self, model, prompt, system_instruction="", **kwargs):
        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt},
        ]
        response = await self.client.chat.completions.create(
            model=model, messages=messages, **kwargs
        )
        return response.choices[0].message.content
