# Performance strategy

Read this reference for MultiMesh, batching, chunks, LOD, visibility, collisions, navigation, pooling, streaming, threading, or budgets.

## First principle

Optimize the representation, not only the object count. Track CPU generation time, runtime CPU time, vertices/triangles, draw calls, buffer memory, collision shapes, navigation cost, loaded chunks, and live Nodes.

Every generator estimates and reports cost before spawn. A budget overflow must reduce optional density, select cheaper recipes/LOD, defer chunks, or fail with diagnostics. Do not silently build a smaller world without reporting it.

## Representation matrix

Use `MultiMesh` for many instances that share mesh and material: grass, repeated tree/rock variants, lamp posts, fence posts, small props, distant simplified houses, clouds, or simple crowds.

Split MultiMeshes by chunk, mesh type, material, and LOD. Godot culls a MultiMesh as one unit, not per instance, so one world-sized MultiMesh harms visibility culling.

Use `PackedScene` for interactive buildings, doors, shops, quests, destructibles, important NPCs, or objects needing their own script and lifetime.

Use chunked `ArrayMesh` batches for noninteractive static geometry that benefits from fewer draw calls. Avoid one giant world mesh; it prevents useful culling and makes updates expensive.

## Chunks and streaming

Choose a chunk size from gameplay visibility and content density, commonly 64-128 world units for a village prototype. Derive chunk seeds from stable coordinates. A chunk owns static mesh groups, MultiMeshes, collisions, spawn manifest, bounds, LOD state, and generation hash.

Generate pure plan/array data off the main thread where Godot APIs permit, then create Resources/Nodes and attach them on the main thread. Support cancellation when the player moves away or the world is regenerated.

Use distance bands with hysteresis:

- near: interaction, collisions, NPC simulation, full detail;
- mid: simplified mesh and low-frequency simulation;
- far: HLOD/very low detail or no object;
- unloaded: plan/cache only or absent.

Avoid repeated create/free churn at a threshold. Pool dynamic objects and retain static chunk products when memory permits.

## LOD and visibility

Provide explicit low-detail recipes for generated geometry; automatic mesh LOD may supplement them. Use `visibility_range_begin/end` for HLOD or disappearance of small props. Test frustum and occlusion behavior with representative camera paths.

Occlusion culling helps dense villages with solid occluders but has setup and runtime cost. Do not assume it benefits open terrain. Profile with and without it.

## Collision

Use simple primitive shapes or coarse generated collision. Collide terrain, major landmarks, interactive buildings, large rocks, trunks, and gameplay boundaries. Usually omit collision for grass, leaves, clouds, tiny rocks, window trim, roof decoration, distant buildings, and purely visual props.

Keep visual and collision recipes separate. Do not generate trimesh collision from every visual mesh. Enable detailed collision only in near chunks when gameplay allows.

## Navigation

Use road/lane graphs for constrained vehicles and pedestrians. Use NavigationRegion3D for free movement where required, divided by region/chunk. Avoid one huge frequently rebuilt navigation mesh. Far agents can use abstract or low-frequency simulation.

## Draw-call and shader policy

Share materials and mesh resources. Encode deterministic variation through instance color/custom data or vertex attributes where practical. Keep surface/material count low; each ArrayMesh surface has a material and draw cost.

Begin with a simple toon shader: quantized diffuse, hemisphere/ambient contribution, rim light, and optional world-space noise. Add screen-space outlines and multi-pass post effects only after geometry, culling, and target hardware budgets pass.

## Profiling gates

Set project-specific thresholds for:

- 1080p FPS/frame time;
- generation milliseconds;
- draw calls;
- visible triangles;
- total/live Node count;
- MultiMesh instances;
- buffer memory estimate;
- collision shape count;
- navigation bake/update time;
- steady-state allocations.

Profile representative seeds, dense and sparse camera positions, regeneration, chunk crossings, and worst supported settings. Average-case success does not replace a worst-case budget test.
