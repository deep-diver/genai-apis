from .abstract import TextGenerationAPI


class AnthropicAPI(TextGenerationAPI):
    def __init__(self, client):
        self.client = client

    async def generate_text(self, model, prompt, system_instruction="", **kwargs):
        messages = [{"role": "user", "content": prompt}]
        response = await self.client.messages.create(
            model=model,
            system=system_instruction,
            messages=messages,
            max_tokens=256,
            **kwargs,
        )
        return response.content[0].text
