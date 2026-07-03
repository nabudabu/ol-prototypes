# Fable Prompt — Mini-Game #06: Verbal Spelling ("Dispel the Clasp")

> Paste the block below into Fable as a single prompt. It is scoped to ONE mechanic
> (the Symbol-to-Word Verbal Spelling loop from "Dyspell verbal prototype.pdf").
> Narration + word recognition are included because this is a *verbal* mechanic —
> they are the mechanic, not extras. The book-world art overhaul and phoneme-level
> recognition are deliberately OUT of scope for this pass (see notes at the bottom).

---

Build a single self-contained HTML file (all HTML, CSS, and JavaScript inline — no
build step, no external files except web-font links and the browser's own speech
APIs). It must run by opening the file directly and work mobile-first on a phone in
portrait, using touch. This is prototype #06 in a series of dyslexia-tutoring
mini-games where **the reading skill IS the magic** — performing the reading action
and casting the spell must be one indivisible motion, never a quiz that gates a
reward.

## The skill being taught
Decoding / encoding at the symbol-to-word level: the learner conjures a word by
writing each letter's shape while saying that letter's NAME, then "dispels" a
magical clasp by tracing the letters, saying their names, underlining the whole
word, and reading the word aloud. (Letter *names* during tracing; whole-word
*reading* at the end.)

## Core loop (from the storyboard)
1. **Mentor demonstration (Instruction Sequence).** The scene opens with the
   player standing slightly behind a magical mentor. The mentor raises a wand and
   conjures a word — e.g. **CLASP** — by drawing each letter's shape in the air one
   at a time while its name is spoken aloud. The finished word glows and forms a
   magical **clasp** (a lock/binding) that seals a door or chest. The mentor flicks
   the wand to flip the word and send it into the world. The mentor then explains,
   in voice, that a cast spell can be *dispelled by someone else*.
2. **Player practice (Practice Sequence).** The clasp now blocks the player. To
   dispel it, the player must, in order:
   a. **Trace each letter** of the word on a rune-slate (finger drawing on canvas),
      and **say that letter's name** as they finish it.
   b. **Underline the whole word** with a swipe.
   c. **Read the whole word aloud.**
   When done correctly, the clasp's magic **dissipates and has no effect** — the
   letters scatter into smoke and the door/chest opens. There is no red X and no
   "wrong!" screen; failure just means the magic doesn't dissipate and the mentor
   gently re-offers the step.

## Recognition (make it real, keep it forgiving)
- **Tracing:** score each letter trace against a target letter outline and require
  a lenient accuracy threshold. On a failed trace, reveal the glowing letter
  outline for the learner to trace over (supported mode), exactly as the storyboard
  shows.
- **Speech:** use the browser Web Speech API (`webkitSpeechRecognition` /
  `SpeechRecognition`) to hear the spoken letter names and the final word. Use
  **fuzzy, lenient matching** — accept near-matches, homophones, and common
  mishearings ("see" for the letter C, "pea" for P, etc.). These learners are
  children and dyslexic; recognition must never feel punitive. If the mic is
  unavailable or denied, fall back to a tap-to-confirm "I said it" button so the
  loop is never blocked.

## Voice narration (REQUIRED — the learners are dyslexic)
- **Every instruction and prompt is spoken aloud**, not just shown as text. Use the
  browser SpeechSynthesis API for this prototype.
- A **persistent, obvious "hear it again" 🔊 button** must let the learner replay
  the current instruction at any time, as many times as they want.
- On-screen text may appear as a *support* for the audio, but the game must be fully
  playable by a non-reader listening to the narration.

## Difficulty progression (per our curriculum rules)
- **Round 1 — Supported:** letter outlines shown to trace; mentor narrates each step.
- **Round 2 — Reduced support:** outlines fade; narration shortens to reminders.
- **Round 3 — Independent:** no outlines unless a trace fails; learner drives the
  full dispel sequence themselves.
- Use short, real, decodable words appropriate to early decoding (CLASP, LAMP,
  DESK, STAMP). Keep one word per round.

## Feel & framing
- Warm, magical, storybook fantasy tone (Harry-Potter-ish wand magic). Calm, not
  frantic.
- Visuals: clean and readable is more important than fancy for THIS pass — use
  simple, tasteful shapes, soft gradients, glows, and particle effects for the
  smoke/dissipation. Leave clear seams so richer art assets can be dropped in later.
- Mobile-first: large touch targets, finger tracing, portrait orientation, no
  reliance on hover or keyboard.

## Explicitly OUT of scope for this prompt
- No phoneme-level sound detection (word-level speech only here).
- No full "scrambled book world" environment art — just the single mentor/clasp scene.
- No account, no backend, no data storage.

Deliver the finished single HTML file.

---

## Notes for Robert (not part of the Fable prompt)

**Why this scope.** One mechanic per prompt is best practice — it matches your
existing five mini-games and keeps Fable's output focused and debuggable. Narration
and word recognition are IN because a *verbal* spelling mechanic is meaningless
without them. The two big asks you raised — richer graphics and true phoneme
recognition — are deliberately deferred to their own passes:

- **Graphics:** run this prompt first to get the loop right with clean placeholder
  art, then do a dedicated art pass (import real SVG/PNG/AI-generated assets rather
  than asking Fable to hand-draw them).
- **Phoneme recognition:** the browser can't do reliable isolated-phoneme detection.
  When you're ready for phoneme-level mechanics, plan to wire in a pronunciation-
  assessment API (Azure Speech pronunciation assessment gives per-phoneme scores;
  SpeechAce is another) and give Fable the endpoint/key. Word-level recognition (as
  used here) is fine in-browser today.

**Suggested prompt sequence for this mechanic:**
1. This prompt → core loop + narration + word recognition.
2. Follow-up: "add Round 2 and Round 3 difficulty, and tighten the fuzzy speech
   matching."
3. Art pass: "replace placeholder shapes with these imported assets" (+ your art).
