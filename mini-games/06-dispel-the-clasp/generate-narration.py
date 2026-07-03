#!/usr/bin/env python3
"""Regenerate the mentor narration for Dispel the Clasp.

Usage:  pip3 install --user edge-tts && python3 generate-narration.py

Voice: en-US-Christopher (mature, clear American male) — chosen because the
learners are beginning readers; a non-US accent can confuse early sound-letter
mapping. Keep ids in sync with VOICE_IDS in index.html.
"""
import asyncio
import edge_tts

VOICE = "en-US-ChristopherNeural"
PITCH = "-4Hz"          # a touch older/deeper
RATE = "-12%"           # unhurried, clear for young listeners
RATE_SLOW = "-22%"      # letter names and the dramatic word-shout

FIXED = {
    "demo-intro":  (RATE, "Watch closely, young mage. I will cast a binding spell — by spelling."),
    "demo-word":   (RATE_SLOW, "Clasp!"),
    "demo-sealed": (RATE, "There. The word is the lock, and the door is sealed. But a spell cast by one mage can be dispelled by another. Trace each letter and say its name. Then underline the word, and read it aloud. The clasp will let go."),
    "round-1":     (RATE, "Another door, another clasp. Trace the letters, say their names, underline, and read."),
    "round-2":     (RATE, "The last seal. This one is yours alone, young mage."),
    "trace-first-2-C": (RATE, "Let us dispel it together. Trace the letter C on the rune slate, and when it is drawn, say its name."),
    "trace-first-1-L": (RATE, "Trace each letter and say its name. Start with L."),
    "trace-first-0-D": (RATE, "Dispel the clasp. It starts with D."),
    "say-first":   (RATE, "Well traced! Now say its name out loud."),
    "say-again":   (RATE, "Say its name."),
    "read-miss":   (RATE, "So close — read the word on the clasp."),
    "under-2":     (RATE, "Every letter is loosened! Now underline the whole word — swipe beneath it, left to right."),
    "under-1":     (RATE, "Now underline the word."),
    "under-0":     (RATE, "Underline it."),
    "under-retry": (RATE, "Sweep all the way under the word, left to right."),
    "read-2":      (RATE, "The clasp trembles! Read the whole word aloud, and its magic will let go."),
    "read-1":      (RATE, "Now read the word aloud."),
    "read-0":      (RATE, "Read it."),
    "praise-0":    (RATE, "Clasp. The clasp is dispelled. You unwrote my spell, letter by letter!"),
    "praise-1":    (RATE, "Lamp. Undone! The letters could not hold you."),
    "praise-2":    (RATE, "Desk. Dispelled — no seal can stand against a mage who can spell."),
    "finish":      (RATE, "Every clasp undone. You are a true dispeller of words, young mage."),
}

LETTERS = "ACDEKLMPST"


def all_lines():
    lines = dict(FIXED)
    for ch in LETTERS:
        lines[f"letter-{ch}"] = (RATE_SLOW, f"{ch}.")
        lines[f"trace-{ch}"] = (RATE, f"Now trace the letter {ch}.")
        lines[f"glow-{ch}"] = (RATE, f"Here — the shape of {ch} glows for you. Trace over it.")
        lines[f"miss-{ch}"] = (RATE, f"Hmm — say the name of the letter {ch}.")
    return lines


async def main():
    lines = all_lines()
    for lid, (rate, text) in lines.items():
        tts = edge_tts.Communicate(text, VOICE, rate=rate, pitch=PITCH)
        await tts.save(f"audio/{lid}.mp3")
        print(lid)
    print("TOTAL:", len(lines))


if __name__ == "__main__":
    asyncio.run(main())
