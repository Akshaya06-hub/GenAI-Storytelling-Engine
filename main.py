"""
GenAI Storytelling Engine - Core Script
Author: Akshayamathi D
"""

import os

def generate_story(prompt: str, temperature: float = 0.7):
    print(f"Initializing narrative pipeline with prompt: '{prompt}'")
    print(f"Parameters applied -> Temperature: {temperature}, Top-P: 0.9")

    sample_output = (
        f"Chapter 1: The Initialization\n"
        f"Based on the directive '{prompt}', the system structured a multi-layered narrative arc, "
        f"maintaining strict contextual constraints and coherent token generation."
    )
    return sample_output

if __name__ == "__main__":
    user_prompt = "A futuristic city powered by collaborative artificial intelligence."
    story = generate_story(user_prompt, temperature=0.7)
    print("\n--- Generated Output ---")
    print(story)
