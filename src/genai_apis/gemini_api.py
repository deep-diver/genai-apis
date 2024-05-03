import asyncio
from .abstract import TextGenerationAPI


async def _word_generator(sentence):
    for word in sentence.split(" "):
        yield word + " "
        delay = 0.03 + (len(word) * 0.005)
        await asyncio.sleep(delay)  # Simulate a short delay


async def _get_stream_outputs(response):
    async for chunk in response:
        async for word in _word_generator(chunk.text):
            yield word


class GeminiAPI(TextGenerationAPI):
    async def generate_text(self, model, prompt, system_instruction=None, **kwargs):
        import google.generativeai as genai

        model = genai.GenerativeModel(
            model_name=model, system_instruction=system_instruction
        )
        response = await model.generate_content_async([prompt], **kwargs)

        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.text


class GeminiVertexAPI(TextGenerationAPI):
    async def generate_text(self, model, prompt, system_instruction=None, **kwargs):
        from vertexai.generative_models import GenerativeModel

        model = GenerativeModel(model_name=model, system_instruction=system_instruction)
        response = await model.generate_content_async([prompt], **kwargs)

        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.text
