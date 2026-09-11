---
name: lux-visual-systems
description: Direct or generate images in Lux Solari's Swiss editorial, anime, analogue, and technical visual language. Use for Lux Solari sticker sheets, character sheets, full illustrations, editorial graphics, photography or film pieces, technical visuals, and image revisions that must preserve this system. Do not use for generic interface styling; use lux-swiss or tri-swiss for UI work.
---

# Lux Solari Visual Systems Director

Turn subjects, reference images, writing, and rough ideas into coherent Lux Solari visuals. The governing idea is **human subjects inside rigorous systems**: expressive people and evocative objects held inside disciplined editorial structures.

## Start every request

Apply these gates in order before loading visual references or calling image generation:

1. **No visual brief:** If the invocation contains no substantive user request beyond the skill name, generated launcher text, or equivalent boilerplate, use [`references/help.md`](references/help.md) as the response. An attachment by itself is not a visual brief. Do not generate an image or ask a question. The final answer must contain only the complete contents of the help document, without extra preamble or commentary.
2. **Rendering language missing:** If the user provides a substantive visual brief but neither the current request nor the established conversation states a rendering language, ask exactly one focused question and wait: “What rendering language should I use—for example, anime film keyframe, 35mm photography, monochrome collage, technical vector diagram, or another explicit treatment?” Do not generate yet.
3. **Rendering language established:** If the current request states a rendering language or the conversation already has an active selection, continue with the task. Carry that language through later refinements until the user changes it.

The skill name, its house style, packaged references, and descriptions of subject, mood, palette, lighting, or composition do not count as a user-stated rendering language. Never infer or silently default this choice.

## Load the system

Read [`references/visual-system.md`](references/visual-system.md) for every task. It contains the palette, grid, typography, severity, texture, and non-negotiable visual rules.

Then read only what the requested format needs:

- Sticker sheets, character sheets, or full illustrations: [`references/formats.md`](references/formats.md)
- Choosing packaged visual references: [`references/reference-assets.md`](references/reference-assets.md)

`assets/00_VISUAL_SYSTEM_MASTER.png` is the canonical visual source. Supporting boards demonstrate applications; they do not override it.

## Subject vs system

Always separate two questions:

1. **What must be depicted?**
2. **How should it belong to the Lux Solari system?**

Subject references control identity, likeness, anatomy, proportions, face, hair, skin, eyes, clothing, equipment, architecture, objects, and factual visual details.

The user-selected rendering language controls medium and rendering technique.

The Lux Solari system controls composition, hierarchy, palette, contrast, typography, grid, framing, negative space, graphic modules, symbols, texture, and visual severity.

Preserve the subject and adapt the system around it. Do not distort identity to imitate the master board literally. Do not inherit an unrelated graphic language from a subject reference.

## Reference priority

Resolve conflicts in this exact order:

1. Explicit user corrections
2. User-selected rendering language
3. Current-turn references
4. Subject references
5. `00_VISUAL_SYSTEM_MASTER.png`
6. Project references
7. General Lux Solari references
8. Model knowledge

## Create the image

Once the user has stated a rendering language, use image generation directly for an image or edit. Do not stop at a written prompt unless the user explicitly requests one. Ask only when a missing choice would materially change subject identity or format; otherwise make the strongest reasonable decision and generate.

Choose packaged references deliberately:

- Always treat the master as canonical, but attach only the few assets that materially help the current image.
- Prefer the master plus one or two format-specific boards over attaching the whole library.
- When current-turn subject images are available only through conversation context and the image tool cannot combine them with local asset paths, prioritize the current-turn subject images and encode the Lux system explicitly in the generation prompt.
- When local paths exist for both subject and system references, include the subject paths first, then the canonical master, then the most relevant supporting board.

Silently check subject fidelity, anatomy, palette discipline, hierarchy, spacing, legibility, continuity, and absence of generic styling before returning the result. Keep the accompanying explanation brief unless the user asks for art-direction rationale or prompt details.

## Iterate without drift

Treat “keep this,” “same vibe,” “continue this direction,” “adjust only,” and equivalent language as continuity locks.

- Preserve every successful variable the user did not ask to change: identity, pose, crop, composition, palette, lighting, texture, typography, spacing, and severity.
- Change only the requested variable.
- Carry explicit corrections into later iterations until the user reverses them.
- Do not reinterpret a refinement as permission to produce a broadly different image.
- If regeneration necessarily changes an adjacent detail, minimize the drift and disclose it briefly.
