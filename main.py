import streamlit as st

st.set_page_config(page_title="Tarot Archetype Generator", layout="centered")
st.title("🔮 Custom Tarot Card Prompt Generator")

st.markdown("Fill in the details below to generate your custom tarot prompt:")

name = st.text_input("Name (optional)")
birthdate = st.text_input("Birthdate (DD-MM-YYYY)")
mbti = st.text_input("MBTI Type")
enneagram = st.text_input("Enneagram Type (with wing)")
love_language = st.text_input("Love Language")
attachment_style = st.text_input("Attachment Style")
core_desire = st.text_area("Core Desire in Life")
core_fear = st.text_area("Core Fear or Anxiety")
fuel = st.text_area("What gives you energy (fuel)?")
drain = st.text_area("What drains or destroys you?")
dream_life = st.text_area("Describe your dream life in one sentence")
music = st.text_area("Favorite music genre(s) and one favorite lyric")
favorite_media = st.text_area("Favorite books/games/movies and why")
symbols = st.text_area("Aesthetic or symbolic elements you strongly connect to")
response_to_pain = st.text_area("How do you respond to pain, failure, or betrayal?")
pressure_behavior = st.text_area("How do you act under pressure?")
process_emotion = st.text_area("How do you process strong emotion?")
belief = st.text_area("Spiritual or philosophical beliefs")
contradiction = st.text_area("Biggest emotional contradiction in yourself")
shadow = st.text_area("What is your shadow side like?")
fear_of_becoming = st.text_area("What do you fear becoming?")

if st.button("Generate Prompt"):
    st.markdown("---")
    st.subheader("🎴 Full Tarot Card Prompt")

    prompt = f"""
You are a symbolic interpreter, narrative psychologist, and tarot archetype creator. Based on the full psychological, emotional, symbolic, aesthetic, and personality input below, create a custom tarot identity for the user, including:

1. Their primary classic tarot card(s) (e.g., The Chariot, The Tower) with clear rationale  
2. Their shadow card and what it reveals about their inner world  
3. Their custom one-of-a-kind archetype card, including:  
    - A poetic card title  
    - Symbolic visual description for illustration  
    - Upright meanings  
    - Reversed meanings  
    - Keywords  
    - Who pulls this card and why  
    - A poetic caption or mantra for the card  
4. Link the card to the user’s numerological birth card (calculated by adding their birthdate digits)  
5. At the end, generate a natural language prompt for image generation of the tarot card, designed using the universal template below. You must infer the bracketed parts ([...]) automatically based on the user's full psychological and symbolic profile.

---
### UNIVERSAL IMAGE GENERATOR PROMPT TEMPLATE:

Tarot card illustration in high-resolution, Art Nouveau hand-painted style, designed as part of a mystical tarot deck.

The card depicts a central figure titled "[CARD TITLE]".
The character stands in a symbolic environment based on their inner world: [SCENE DESCRIPTION]
Their appearance, pose, and expression reflect their essence: [APPEARANCE & BODY LANGUAGE]
They hold or interact with symbolic objects such as [SYMBOLIC OBJECT 1], [SYMBOLIC OBJECT 2], each representing aspects of their personality or psychological tension (e.g., power, fear, memory, destiny, etc.).

The environment behind them should evoke the emotional tone of the card: [MOOD & LIGHTING] (e.g., glowing firelight and deep shadows for a conflicted soul; radiant golden dawn for an enlightened seeker; swirling mists for introspective or mystical themes).

Include engraved stone or platform with 1–2 keywords reflecting the user's core struggle or gift, such as "[KEYWORD 1]" and "[KEYWORD 2]".

The border should be elegant, gold-accented, and in tarot Art Nouveau style—framing the scene like a collectible card.

Style: clean, balanced composition with detailed anatomy, flowing fabric, glowing effects, and expressive symbolism.

Do not use surreal distortions. Maintain realistic human structure with mystical or dreamlike elements.

This card should reflect the inner archetype of someone who is [ARCHETYPE KEYWORDS] (e.g., a visionary, a survivor, a seeker, a ruler, a destroyer, a healer, etc.).

---
### User Input:

Name: {name}  
Birthdate: {birthdate}  
MBTI Type: {mbti}  
Enneagram Type: {enneagram}  
Love Language: {love_language}  
Attachment Style: {attachment_style}  
Core Desire in Life: {core_desire}  
Core Fear or Anxiety: {core_fear}  
What gives you energy: {fuel}  
What drains you: {drain}  
Dream life: {dream_life}  
Favorite music & lyric: {music}  
Favorite media: {favorite_media}  
Symbolic elements: {symbols}  
Response to pain: {response_to_pain}  
Under pressure: {pressure_behavior}  
Processing emotion: {process_emotion}  
Beliefs: {belief}  
Emotional contradiction: {contradiction}  
Shadow side: {shadow}  
Fear of becoming: {fear_of_becoming}
"""

    st.code(prompt, language="markdown")
    st.success("Prompt ready! Copy and paste into GPT-4 or your backend script.")
