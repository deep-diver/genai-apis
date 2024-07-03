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

        stream = False
        safety_settings = None
        if "stream" in kwargs:
            stream = kwargs.pop("stream")

        if "safety_settings" in kwargs:
            safety_settings = kwargs.pop("safety_settings")

        generation_config = genai.types.GenerationConfig(**kwargs)
        model = genai.GenerativeModel(
            model_name=model, system_instruction=system_instruction
        )
        response = await model.generate_content_async(
            [prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=stream,
        )

        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.text


class GeminiVertexAPI(TextGenerationAPI):
    async def generate_text(self, model, prompt, system_instruction=None, **kwargs):
        from vertexai.generative_models import GenerativeModel
        from vertexai import generative_models

        DEFAULT_SAFETY_SETTINGS = {
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }

        stream = False
        safety_settings = DEFAULT_SAFETY_SETTINGS

        if "stream" in kwargs:
            stream = kwargs.pop("stream")

        if "safety_settings" in kwargs:
            safety_settings = kwargs.pop("safety_settings")

        generation_config = generative_models.GenerationConfig(**kwargs)
        model = GenerativeModel(model_name=model, system_instruction=system_instruction)
        response = await model.generate_content_async(
            [prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=stream,
        )

        if "stream" in kwargs and kwargs["stream"] is True:
            return _get_stream_outputs(response)
        else:
            return response.text
