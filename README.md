# Unnecessary C to JavaScript V12 Engine: No one asked for

> _"Why write a lexer, parser, AST generator, semantic analyzer, and code generator when you can just vibe check the code with a glorified autocorrect?"_

Welcome to the **V12 Engine**. It is 4 versions better than V8 because I skipped the hard parts.

### The "Innovation"

Traditional JavaScript engines like Google's V8 or Mozilla's SpiderMonkey are bloated with "necessary features" like:

- **Just-In-Time (JIT) Compilation:** Fast but difficult.
- **Garbage Collection:** Useful but mathematically complex.
- **Abstract Syntax Trees (AST):** Who has the time?
- **Correctness:** Overrated.

**V12 solves this by removing the engine entirely.**

Instead of parsing code, V12 reads your C file, hallucinates what it might look like in JavaScript, and saves the file. It turns the deterministic art of compiler design into a probabilistic roll of the dice. If your pointer arithmetic doesn't translate, that's not a bug; it's a creative interpretation by the AI.

### Development Philosophy: 100% Vibecoded

**This project is fully vibecoded and will always be vibecoded.**

I did not write this code. I merely prompted it into existence.
**Contribution Policy:**

- **Do NOT** send PRs with manual code.
- **Do NOT** use your brain to optimize the logic.
- If I see a variable name that makes sense or a comment that was clearly written by a human who understands the software lifecycle, **I will close the PR.**

We only accept code that looks like it was hallucinated by a GPU at 3 AM. If you didn't Cmd+C / Cmd+V it from a chatbot, we don't want it. Keep the vibes artificial.

### How it works

1. **Input:** Your perfectly good C code.
2. **Black Box:** We text the code to a data center in Virginia.
3. **Output:** JavaScript that probably works.

### Installation

You don't need a build system. You don't need `make`. You just need Python and faith.

```bash
# Get the dependencies (literally just openai)
pip install -r requirements.txt

```

### Usage

To transpile your C code into "modern" ES6+:

```bash
# The pinnacle of engineering
python main.py input.c

```

_Note: If the output code doesn't run, try asking the engine nicely again._

### Roadmap: The "Ollama" Dilemma

I am currently debating adding **Ollama** support to run a local LLM.

Why?

- So you can transpile C code while camping without WiFi.
- To heat up your laptop so it acts as a hand warmer while you code.
- To avoid paying API fees for a tool that is objectively worse than `emscripten`.

**Should I do it?** Open an issue and tell me if you want your CPU fans to sound like a jet engine for the sake of privacy.

---

**License:** MIT (Maybe It Transpiles)
