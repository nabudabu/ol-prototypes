# OL Prototypes — Vision

## One-Liner

Learn to read by learning magic — an adventure RPG that adapts evidence-based dyslexia tutoring into 3D video game mechanics.

## The Core Belief

**The reading skill IS the magic — not a means to earn it.**

This is the single idea the whole project turns on. The reading system and the magic system are not two things bolted together; they are *the same system seen from two angles*. The learning is the gameplay, and the gameplay is the learning.

When a child recognizes a rhyming pattern, the act of recognition *is* the incantation. When they blend phonemes into a word, the blending *is* the summoning. When they trace a letter, the stroke *is* the spell taking form. The power doesn't come *after* the skill as a reward — the power comes *from* the skill, in the same motion.

This is the line we refuse to cross: **these are not workbook exercises in a fantasy costume.** A drill that pauses the game to quiz the child, then hands back control once they answer "correctly," has failed — no matter how nice it looks. If you can remove the magic and still have a worksheet, it isn't done. The test for every mechanic is simple: *does performing the reading skill and performing the magic feel like one indivisible act?*

## The Concept

Reading skills are not *reframed* as magic skills — they are *built as* magic skills from the start. Phoneme awareness is incantation. Decoding is spell-casting. Fluency is mastery of the arcane. The learner is a young mage progressing through a magical world, and the reading skills they acquire are literally the abilities they wield, the rooms they open, and the regions they reach.

### The World Is Made of Words — And the Books Have Been Scrambled

The entire game takes place **inside books**. The player is transported into the pages themselves and moves through a world woven from words, letters, and sounds. But this world is broken: an **evil spell has scrambled the books**, jumbling the letters, words, and sentences into chaos. Paths that were once readable sentences have collapsed; words that named real things have been shattered into loose, drifting letters; meaning has been torn out of the pages.

The player's quest is to **restore the books by reading** — to un-scramble the world one skill at a time. Every act of decoding puts a letter back in its place, re-forms a broken word, or rebuilds a sentence-bridge. The antagonist's scrambling spell is the source of every obstacle, and the player's growing reading ability is the only thing that can reverse it. This gives the whole game a single, legible motivation: **the world is disordered language, and reading is what puts it back in order.**

This framing isn't decoration; it's what makes every mechanic make sense. In the book world:

- **Letters are physical things** — they can be drawn, broken, lit, stacked, and assembled.
- **Sounds have force** — a spoken phoneme is wind, fire, or light; the wrong sound does nothing, the right one moves the world.
- **Words are objects and spells** — to read a word correctly is to make the thing it names *real*, or to make the spell it encodes *fire*.
- **Sentences are paths and structures** — bridges, doors, and incantations that only hold together when read in order.

Because the world is literally built from the units of reading, there is never a moment where "the reading part" and "the game part" come apart. Decoding a word to open a sealed door isn't a quiz gating a reward — the word *is* the lock and the reading *is* the key turning.

### The Narrative Ties It Together

These mini-games are not a disconnected arcade. A single story threads through all of them: the player is an **up-and-coming mage — a reader on the rise** — who grows in power by learning to read. Each skill mastered is a step from apprentice toward adept. The curriculum sequence *is* the hero's arc: you begin barely able to perceive the letters shimmering in the book world, and you end able to speak whole sentences that reshape it.

This narrative frame does real work. It gives the progression emotional stakes (you are *becoming* something), it justifies why skills arrive in a researched order (a young mage can't summon storms before they can light a candle), and it lets every standalone prototype belong to the same world — the same rising mage, the same book, the same magic being discovered one reading skill at a time.

The tonal and mechanical inspirations:

| Inspiration | What We Take From It |
|---|---|
| **Harry Potter** | Wand magic, spoken spells, potions, the fantasy of learning magic at school |
| **Breath of the Wild** | Open-world adventure, emergent mechanics, exploration-driven progression |
| **Indiana Jones** | Environmental puzzles, discovery, the thrill of figuring things out |
| **Sky: Children of the Light** | Mobile-first design, expressive world, social warmth, accessible controls |
| **Wario Ware** | Bite-sized mini-games, rapid mechanic variety, playful experimentation |

## The Three-Phase Roadmap

### Phase 1 — Mini-Games (Current Phase)

**~20 standalone mini-games**, each prototyping a different novel mechanic that adapts a specific activity from evidence-based dyslexia tutoring programs (Orton-Gillingham, Lindamood-Bell, Wilson Reading, etc.) into playable game interactions.

Goals:
- Explore the design space rapidly
- Test which mechanics are fun, effective, and retainable
- Build a library of proven interactions
- String the games together with a **curriculum backbone** so learners progress through skills in a researched sequence

Think Wario Ware: short, varied, surprising — but underneath, each game targets a real skill.

### Phase 2 — Escape Rooms

A **closed-world escape room game** that sequences the best mini-game mechanics into a structured progression. Each room requires the player to:

1. **Learn** a new magic/reading skill
2. **Practice** it through guided repetition
3. **Demonstrate mastery** to unlock the next room

This phase tests whether the mechanics hold up in a connected experience with narrative context, pacing, and skill-gating.

### Phase 3 — The Open World

The final form: a **3D world inspired by Sky: Children of the Light** where the player/learner can explore, build, interact with NPCs, and shape the environment using magic. The best mechanics from Phases 1 and 2 are embedded naturally into this world — not as disconnected mini-games, but as the way magic works.

## Design Principles

- **The skill is the magic.** Reading system mirrors magic system. The act of reading and the act of casting must be one indivisible motion — never a quiz that gates a reward. If you can strip away the magic and still have a worksheet underneath, it isn't done.
- **Evidence-based first.** Every mechanic maps to a real activity from proven dyslexia intervention programs. Fun is the delivery vehicle, not a replacement for rigor.
- **Mobile-first.** Designed for the devices learners actually have. Touch, voice, and tilt before keyboard and mouse.
- **Mastery through play.** No worksheets in disguise. If it doesn't feel like a game, it's not ready.
- **Curriculum-sequenced.** Games aren't random — they follow a progression that builds skills systematically, from phonemic awareness through fluency. The sequence is also the mage's arc: candle before storm.
- **One world, one mage.** Every prototype belongs to the same book world and the same rising-mage story. The narrative is what makes a pile of mini-games feel like one game.

## Production Quality & Core Technology

These are cross-cutting requirements that every prototype and every phase must honor. They are not polish for "later" — for a dyslexic learner, they are load-bearing.

### Audio-First, Because the Learners Can't Rely on Reading

Our learners are dyslexic. **We cannot deliver instructions as written text and assume they'll be read.** Every instruction, prompt, and piece of feedback must be delivered as **high-quality spoken voice narration**, and the learner must be able to **replay any instruction on demand** (a clearly visible, always-available "hear it again" control). Text on screen is a support for the audio, never a replacement for it.

For prototypes, browser speech synthesis with a replay button is acceptable as a stand-in. For anything we put in front of real learners, we want **warm, natural, pre-recorded neural TTS or human voice-over** — robotic narration undermines trust and comprehension for exactly the kids we serve. Narration is a first-class asset, budgeted and produced deliberately.

### Legitimate Speech & Symbol Recognition

The magic only works if the game can actually tell what the learner did. We need real recognition across three levels, and we should be honest about how hard each one is:

- **Grapheme / letter tracing (solid today).** Recognizing whether a learner drew the correct letter shape is done on-device with canvas stroke-tracing and an accuracy score. Our existing prototypes already do this reliably. Low risk.
- **Word recognition (good enough for prototypes).** When a learner reads a whole word aloud, the browser Web Speech API can transcribe it. Usable now with forgiving, fuzzy matching — but it is imperfect for children and for dyslexic speech, so thresholds must be lenient and failure must never feel punitive.
- **Phoneme recognition (the hard problem — needs real tech).** Detecting individual sounds (isolated /s/, /a/, blends) is **not** something the browser Web Speech API does well; it is built for words, not phonemes. Doing this legitimately requires dedicated speech technology — a pronunciation-assessment service that returns **per-phoneme accuracy scores** (e.g., Azure Speech pronunciation assessment, SpeechAce, or a hosted phoneme-level model such as wav2vec2/allosaurus), or forced-alignment tooling. A prototype tool can *wire up* such an API if we supply keys/endpoints, but it cannot invent reliable phoneme detection from scratch in the browser. **Plan: prototype with Web Speech + Web Audio heuristics; commit to a pronunciation-assessment API before phoneme-level mechanics ship.**

### Graphics Quality

Our current prototypes render with basic canvas shapes, and it shows. We want a meaningfully higher visual bar. The realistic path in a browser prototype is an **asset pipeline, not hand-coded shapes**: produce real art (backgrounds, characters, letter-creatures, effects) as SVG/PNG/AI-generated image assets, then have the prototype compose and animate them, optionally with a lightweight WebGL/Three.js layer for depth and particles. We should treat art as something authored separately and imported — asking a code generator to "draw beautiful graphics" from primitives will stay crude. Build the mechanic first with clean placeholder art, then run a dedicated art pass.

## Target Audience

Tweens with dyslexia (or at risk), their tutors, and their families. The game should be playable independently but also fit into structured tutoring sessions.
