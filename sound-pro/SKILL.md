---
name: sound-pro
description: |
  Higher-quality, bespoke sound-effect generation via paid AI text-to-audio APIs (ElevenLabs Sound Effects, Stable Audio) for a game or site's signature/hero moments — not for every UI blip. Costs real money (per-generation API credits), the user's time (one-time API key setup), and more Claude tokens (prompt engineering + verification round-trips) than the quick-source path. Requires the user's own API key in their environment — Claude never holds or spends payment credentials on the user's behalf. Use when `sound-quick`'s CC0 packs don't have anything close, or the moment matters enough to be worth the cost (a game's title sting, a boss reveal, this project's own popper-pop/fortune-reveal chimes).
---

# Sound Pro

The resource-intensive counterpart to `sound-quick`: spend money + time + tokens to get a sound custom-made for the exact creative moment, via a hosted text-to-audio model, instead of picking the closest pre-made CC0 file.

## Hard boundary — API keys and money

Claude does not acquire, hold, or pay for API access on the user's behalf. This skill only works if the user has:
1. Created their own account with the chosen provider,
2. Generated an API key there themselves,
3. Put it in their own environment (a `.env` file, shell env var, or secret manager) — **never pasted into chat**, and Claude never writes the literal key value into any project file or memory.

If the key isn't present in the environment when this skill is invoked, stop and tell the user which env var name is needed and where to get the key — don't proceed, and don't ask them to paste the raw key into the conversation.

**Before every paid call**, state the estimated cost (see pricing below) and get explicit confirmation — this is a real-money action, same bar as any other consequential action Claude takes.

## Primary provider: ElevenLabs Sound Effects

**Verified working end-to-end 2026-08-23** (generated the wedding-website project's party-popper sound effect with this exact call):

- Endpoint: `POST https://api.elevenlabs.io/v1/sound-generation`
- Auth: `xi-api-key` header, value = the user's own key (see the "hard boundary" above — read it via an env var, never hardcode).
- JSON body fields (confirmed working, not the guessed names from this skill's first draft):
  - `text` — the English sound-design prompt (**not** `prompt` — a naive first guess got this wrong).
  - `duration_seconds` — 0.5–30 (not 0.1–30 as first assumed; the API's actual minimum is 0.5).
  - `prompt_influence` — a **number 0–1** (default 0.3), not the "High"/"Low" strings guessed in this skill's first draft. 0.7 worked well for a fairly literal, not-too-creative interpretation.
- `output_format` is a **query string parameter**, not a body field — e.g. `?output_format=mp3_44100_128`.
- Response body is the raw audio bytes directly (not JSON) — save the response body straight to a file.
- Docs: https://elevenlabs.io/docs/overview/capabilities/sound-effects — still worth a skim for prompt-writing tips, but don't trust its parameter names over the verified list above.
- **Pricing (as researched 2026-08-23, re-verify against https://elevenlabs.io/pricing before relying on it)**: roughly $0.12/minute of generated audio, or ~200 credits per generation on the subscription-credit system. A single 2-3 second sound effect is cheap in absolute terms, but state the number before calling anyway.

Reference implementation (PowerShell, since that's what worked in a Windows environment without a Node/curl multipart setup — adapt syntax for other shells, the request shape itself is what matters):

```powershell
$key = [System.Environment]::GetEnvironmentVariable('ELEVENLABS_API_KEY','User') # or however the key is stored in this environment
$body = @{ text = "<prompt>"; duration_seconds = 2; prompt_influence = 0.7 } | ConvertTo-Json
$headers = @{ 'xi-api-key' = $key; 'Content-Type' = 'application/json' }
Invoke-WebRequest -Uri "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_128" -Method Post -Headers $headers -Body $body -OutFile "raw_output.mp3"
```

## Alternative provider: Stable Audio (Stability AI)

Better suited for longer ambient/music-adjacent textures than short punchy SFX. Repo: https://github.com/Stability-AI/stable-audio-tools (self-hostable, needs a GPU, not a hosted API by default — only worth it if the user wants to run it locally rather than pay per-call). If Stability AI offers a hosted API for it, verify current terms before using; don't assume free-tier availability.

## Prompt crafting (Chinese request → English sound-design prompt)

The user will usually describe the sound in Chinese, colloquially ("喜慶的鑼鼓聲", "溫暖的鈴聲"). Translate and expand it into an English sound-design prompt with concrete, literal descriptors — vague prompts produce vague/generic results:
- **Material/source**: what's making the sound (brass bell, wooden block, paper, synth pad, gong).
- **Action**: the physical gesture (a single struck hit, a sustained swell, a quick pluck, a rolling tremolo).
- **Character/emotion**: the tone this project needs (warm, festive, bright, tense, comedic) — this is usually the part of the Chinese request most worth preserving literally.
- **Envelope shape**: fast attack vs. soft swell, short decay vs. long tail — matters a lot for whether it reads as an "impact" vs. an "ambience".
- **Explicit exclusions** when relevant ("no reverb", "dry", "no vocal elements") — text-to-audio models tend to over-add atmosphere unless told not to.

Example: "喜慶的輪盤轉動聲" → `A wooden roulette wheel spinning with rhythmic clicking ratchet ticks, warm and festive tone, no background music, dry recording, 2-3 seconds`.

## Post-processing (do this for every generated file, cheap and worth it)

Run this locally with `ffmpeg` before dropping the file into the project — normalizing loudness and trimming silence noticeably improves how a generated clip sits next to hand-picked CC0 assets or the project's existing synthesized `sfx.ts` sounds:

```bash
ffmpeg -i raw_output.mp3 -af "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 44100 output.mp3
```

(Trims leading/trailing silence via the reverse-silenceremove-reverse trick, then normalizes to -16 LUFS integrated loudness, -1.5dB true peak — a reasonable target for a short game/UI SFX sitting next to other short sounds, not a music-mastering target.)

## Workflow

1. Confirm the API key is present in env; if not, stop and tell the user how to get one.
2. Turn the user's request into an English sound-design prompt (above); show it to the user before calling if the interpretation is non-obvious.
3. State the estimated cost, get confirmation.
4. Call the API, save the raw output.
5. Run the ffmpeg normalize/trim pass.
6. Copy into the project's real audio asset directory, tell the user exactly what was generated, from what prompt, and what it cost.
7. If it doesn't sound right, don't just re-roll blindly and burn more budget — ask the user what's off (too harsh / wrong material / wrong length) and adjust the *prompt* accordingly before retrying.
