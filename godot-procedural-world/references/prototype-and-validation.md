# Prototype, validation, and delivery

Read this reference for a new prototype, implementation sequence, acceptance tests, audit, or handoff.

## Minimal procedural cartoon village

A useful first proof contains:

- one user-visible seed;
- one procedural terrain patch;
- one main road and a few optional branches;
- one fixed central plaza;
- 10-30 generated houses from two archetypes;
- generated trees and rocks;
- 1-3 original fixed landmarks;
- a basic toon shader;
- camera and simple collision;
- FPS, draw calls, triangles, generation time, loaded chunks, and instance counts;
- regeneration and determinism checks.

It must run without external 3D assets using primitive meshes and programmatic ArrayMesh/SurfaceTool geometry. Keep art original and generic; never reproduce protected reference worlds or characters.

## Suggested sequence

1. SeedService and canonical stable hash.
2. GenerationContext, generator contract, and plan types.
3. Same-seed plan-hash regression.
4. Height field and terrain mesh.
5. Spatial constraints and reservations.
6. Fixed plaza/landmark anchors.
7. Road graph, terrain stamps, and road mesh.
8. Building plots and two building archetypes.
9. Tree and rock recipes with chunked MultiMesh.
10. Collision policy and camera.
11. Toon shader.
12. Performance HUD and budgets.
13. Chunk streaming/cache only after the complete small world is correct.

Do not begin by maximizing world size, content count, shader passes, or archetype count.

## Required validation

- Same seed, settings, and versions produce the same canonical plan hash.
- Different seeds produce meaningful differences without invalid layouts.
- Changing one generator version does not perturb unrelated generators' plans.
- Landmarks retain protected footprints, access, and view corridors.
- Buildings do not overlap roads, landmarks, or each other.
- All building entrances and required landmarks are reachable.
- Terrain, visual placement, collision, and spawn heights agree.
- Roads respect maximum slope, turn, and connection rules.
- Placement loops have bounded retries and explain shortfalls.
- The world stays within draw-call, triangle, memory, collision, and generation-time budgets.
- Invalid plans fail before partial spawning or cleanly roll back their own output.

Use several named representative seeds: baseline, dense, sparse, steep, boundary-heavy, and a previously failing regression seed.

## Audit questions

For an existing implementation, report:

- which content is fixed versus procedural;
- whether random streams are isolated and stable;
- whether generation plans exist before spawning;
- shared-data ownership and generator coupling;
- overlap, slope, reachability, and budget validation;
- runtime Nodes versus ArrayMesh/MultiMesh/PackedScene;
- chunk and culling granularity;
- collision/navigation excess;
- cache/version strategy;
- tests and observable diagnostics;
- highest-risk scaling bottleneck.

## AI extension handoff

Every new generator or archetype work package states:

```text
GeneratorId and Version
Definition Resource/schema
Inputs and outputs
Stable seed namespace
Rules and recipe fields
Validation and reservations
Spawn/render/collision strategy
LOD/MultiMesh/chunk policy
Performance budget
Representative seeds
Determinism and regression tests
Failure diagnostics
```

AI should add a reusable rule/archetype and its tests, not a pile of untracked one-off variants. Prefer narrow corrections based on observed failures over accumulating universal rules.
