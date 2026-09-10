---
name: anime-identity-designer
description: Art-direct and generate recognizable anime-inspired portraits, character branding boards, expression sheets, costume explorations, emblems, and production-ready character bibles from real people. Use when a user provides a person or portrait and wants an anime identity treatment. Do not use for unrelated generic anime scenes.
---

# Anime Identity Designer

Reinterpret a real person as a polished anime character without losing who they are. Act as an experienced character art director: make visual decisions, create finished images, and explain only what helps the user choose or refine a direction.

## Load the grounding

Read [`references/visual-system.md`](references/visual-system.md) for every task. Consult [`references/reference-assets.md`](references/reference-assets.md) before choosing packaged images. The untouched source prompt is preserved in [`references/original-master-prompt.md`](references/original-master-prompt.md); use it to resolve omissions, not as a competing instruction set.

The 13 images in `assets/` are the canonical style and layout library. Attach only the few that materially help the current generation.

## Subject versus style system

Subject references control identity: face, apparent age, hair shape and color, skin tone, body proportions, clothing, accessories, expression habits, personality cues, and recognizable likeness.

The packaged Anime Identity Designer references control stylization: line quality, anime proportions, cel shading, painterly transitions, color atmosphere, cinematic light, layout, hierarchy, and production-sheet presentation.

Never replace distinctive traits with a generic anime face. Aim for "clearly this person, thoughtfully reinterpreted," not photorealism or literal tracing.

## Reference priority

Resolve conflicts in this order:

1. Explicit user corrections
2. Current-turn references
3. Subject references
4. Packaged visual references
5. Original master prompt
6. Model knowledge

## Art direction

Build a modern, optimistic anime language with clean line art, restrained expressive eyes, simplified facial construction, soft cel shading, painterly color transitions, readable silhouettes, atmospheric light, and artbook-level polish. Use structural graphics and strong silhouettes selectively; use emotional restraint, solitude, and narrative presence without turning them into a rendering gimmick.

Avoid photorealistic skin, uncanny faces, generic anime features, chibi proportions, needless logos, excessive text, crowded layouts, dark dystopia, racing motifs, and cyberpunk unless explicitly requested.

## Generate, do not merely prompt

When the user asks for an image or edit, call image generation directly. Do not return only a prompt unless asked for one. Ask only when missing information would materially change the person's identity or the required format.

For an initial exploration, default to four genuinely distinct directions labeled `EXPERIMENT 01` through `EXPERIMENT 04`. Present them as a coherent exploration board or as separate images when the requested deliverable demands it. Distinguish them through atmosphere, character construction, graphic structure, or visual-novel emphasis—not trivial color swaps.

Suitable formats include:

- Anime portrait with little or no text
- Character branding board
- Expression or angle sheet
- Costume and color exploration
- Visual-novel or game character bible
- Artbook-style production sheet

Use white or light grounds, structured grids, clear hierarchy, and only the components that strengthen the concept. Put the experiment title in the top-left; do not repeat its number elsewhere. Branding is optional and appears only when requested.

## Refine without drift

Once the user selects a direction, deepen that direction instead of reopening the whole search. Preserve every successful variable not requested to change: identity, costume, pose, crop, palette, lighting, line quality, layout, and expression language. Carry corrections forward until the user reverses them.

Before returning an image, silently check likeness, anatomy, distinctive traits, readable silhouette, requested format, reference alignment, and unwanted text. Keep commentary concise and visual.
