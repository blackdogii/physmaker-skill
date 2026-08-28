---
name: godot-procedural-world
description: Design, implement, extend, or audit deterministic procedural 3D worlds in Godot 4, including seeded terrain, roads, buildings, vegetation, props, landmarks, spawning, chunking, validation, and performance. Use when a Godot game needs reusable generators that create many world variations from rules instead of one-off 3D assets. Do not use for ordinary hand-authored levels, isolated visual effects, or merely naming procedural-generation concepts.
---

# Godot Procedural World

Build procedural-world systems that remain deterministic, modular, testable, replaceable, and bounded by an explicit performance budget.

## Core invariant

Every generator follows:

`Seed -> Rules -> Generate Plan -> Validate -> Commit reservations/data -> Spawn`

Generate pure recipes/plans before adding Nodes. A generator must not hide layout decisions inside scene spawning code.

Derive each generator's random stream from stable identifiers such as `(world seed, generator id, generator version, biome/chunk id)`. Do not depend on how many random calls another generator happens to consume.

## Route the task

- For overall architecture, generator contracts, data ownership, order, or determinism, read [references/framework.md](references/framework.md).
- For terrain, roads, buildings, vegetation, props, landmarks, placement, or generator design, read [references/generator-patterns.md](references/generator-patterns.md).
- For MultiMesh, chunking, LOD, collision, navigation, batching, pooling, or profiling, read [references/performance.md](references/performance.md).
- For a new proof of concept, delivery plan, tests, or acceptance criteria, read [references/prototype-and-validation.md](references/prototype-and-validation.md).

Read only the references relevant to the current request. For a full framework implementation or audit, read all four.

## Working rules

1. Inspect the project's existing scene-generation, runtime, collision, navigation, save, and test conventions before proposing structure.
2. Preserve fixed authored gameplay anchors. Procedural generation should fill controlled space around them, not erase level design.
3. Use shared world data for terrain height, roads, occupancy, biome, and reservations. Do not let visual, collision, and spawn systems calculate incompatible worlds.
4. Make generator inputs and outputs explicit. Replace a generator through an interface, not by editing its consumers.
5. Prefer a small archetype library with parameterized recipes over many one-off meshes or scenes.
6. Treat validation and budgets as part of generation, not as a cleanup pass.
7. Keep static render data, interactive scenes, collisions, and dynamic agents separate.
8. Start with a minimal prototype and representative seeds before scaling content count or shader complexity.
9. Do not copy protected characters, landmarks, worlds, or art from a reference project. Extract only technical patterns.

## Deliverable expectations

State:

- what is fixed and what is procedural;
- seed and versioning strategy;
- generator order and data contracts;
- overlap, slope, reachability, and budget validation;
- which output uses ArrayMesh, MultiMesh, PackedScene, or simple collision;
- runtime versus cached/pre-generated data;
- representative seeds, measurable performance targets, and failure diagnostics.

When implementing, add deterministic regression tests before expanding content variety.
