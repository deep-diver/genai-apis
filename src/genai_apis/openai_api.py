from .abstract import TextGenerationAPI


async def _get_stream_outputs(response):
    async for chunk in response:
        yield chunk.choices[0].delta.content


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
        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.choices[0].message.content
