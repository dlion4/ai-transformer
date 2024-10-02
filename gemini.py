import environ
import google.generativeai as genai

env = environ.Env()

env.read_env(".env")


genai.configure(api_key=env.str("GEMINI_API_KEY"))


para = """
Elara, a girl with a tangle of wild, red hair and eyes the colour of storm clouds, found the backpack tucked away in the back of her grandmother's attic. It was a plain canvas bag, faded and dusty, with a single, tarnished silver buckle. But when Elara touched the buckle, a spark of warmth ran up her arm, and she felt a strange pull, a whisper of magic.
She was a curious girl, Elara, and curiosity always got the better of her. She slung the bag over her shoulder, a sense of adventure bubbling in her chest. As she walked home, she noticed things changing. The sunset, normally a fiery orange, was now a swirling nebula of greens and purples. The wind carried the scent of cinnamon and distant waterfalls.
When she reached her room, she emptied the bag. Inside, she found a single, wrinkled paper. Unfolding it, she saw a hand-drawn map, depicting an island shrouded in fog and dotted with strange symbols. A thrill shot through her. This wasn't just a backpack; it was a portal, a gateway to somewhere unknown.
The next morning, she packed a few essentials - a compass, a canteen, and a journal. With a deep breath, she touched the buckle again. The room shimmered, and the walls dissolved into a swirling mist. Then, she was on the island.
The air was thick with the scent of pine and salt, and the ground was covered in a carpet of emerald moss. The map, however, was useless. The symbols were all jumbled, the paths unreadable. Elara felt a pang of fear, but she pushed it down. This was an adventure, and she wouldn't let fear win.
She walked for hours, following the sound of a gurgling stream. As she walked, the backpack felt lighter, almost empty. Yet, whenever she needed something, it always provided. A warm blanket when the sun dipped below the horizon, a flashlight when darkness descended, even a steaming cup of hot cocoa when she felt chilled.
Finally, she stumbled upon a clearing, where a magnificent tree stood, its branches laden with glowing fruit. The map symbols suddenly clicked, the final piece of the puzzle. This was the heart of the island, the source of its magic.
Elara ate one of the fruits, and a rush of energy surged through her. She understood now; the backpack wasn't just a magic bag, it was a conduit. It drew magic from the world around her, providing for her needs, and it was fueled by her own sense of wonder.
From that day on, Elara knew she wasn't just a girl with a backpack; she was a girl with a heart full of magic, a girl who could find adventure in every corner of the world. And as she walked away from the island, the backpack felt heavy again, full of the promise of new journeys, new wonders, and new stories to be told.
"""
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"Extract the a one word topic from this {para}")
print(response.text)
