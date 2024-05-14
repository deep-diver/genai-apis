from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="genai_apis",
    version="0.0.8",
    description="GenAI APIs provides a unified API callers to Gemini API, OpenAI API, and Anthropic API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="chansung park",
    author_email="deep.diver.csp@gmail.com",
    url="https://github.com/deep-diver/genai-apis",
    install_requires=["asyncio"],
    extras_require={
        "openai": ["openai"],
        "gemini": ["google-generativeai"],
        "gemini-vertex": ["google-cloud-aiplatform"],
        "anthropic": ["anthropic"],
        "anthropic-bedrock": ["anthropic[bedrock]"],
        "anthropic-vertex": ["anthropic[vertex]"],
    },
    packages=["genai_apis"],
    package_dir={"": "src"},
    keywords=["genai"],
    python_requires=">=3.10",
    package_data={},
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
)
