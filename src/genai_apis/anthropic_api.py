from .abstract import TextGenerationAPI


async def _get_stream_outputs(response):
    async for chunk in response:
        if chunk.type == "content_block_delta":
            yield chunk.delta.text


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

        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.content[0].text
