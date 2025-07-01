import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))  

def generate_story(prompt, genres, tone, word_limit):
    genre_str = ', '.join(genres)
    
    prompt_text = (
        f"Write a titled children's story of exactly around {word_limit} words. "
        f"The story should have a clear beginning, middle, and end. "
        f"It must include a title at the top, followed by the story. "
        f"Genres: {genre_str}. Tone: {tone}. Prompt: {prompt}"
    )

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt_text,
            max_tokens=min(word_limit * 2, 1000),
            temperature=0.8,
            stop_sequences=["--END--"]
        )
        story = response.generations[0].text.strip()
        return story

    except Exception as e:
        return f"An error occurred while generating the story: {str(e)}"
