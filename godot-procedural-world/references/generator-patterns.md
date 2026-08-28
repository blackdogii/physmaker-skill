# Generator patterns

Read this reference when designing or implementing terrain, roads, buildings, vegetation, props, landmarks, placement, or procedural meshes.

## Shared pattern

Each generator separates:

```text
Definition Resource -> deterministic Recipe/Plan -> validated runtime product
```

Definitions are authored rules. Recipes are generated data. Runtime products are ArrayMesh, MultiMesh, PackedScene instances, collisions, navigation, or lightweight agents.

## Terrain

Use one authoritative height/normal service for render mesh, road grading, building placement, collision, camera clearance, and spawning.

Compose broad shape, biome modifiers, and explicit gameplay stamps. Roads, plots, plazas, and landmarks may add flatten/grade stamps before final terrain generation. Blend or blur stamp weights so platforms do not end in hard shelves.

Use `ArrayMesh` for production terrain data. `SurfaceTool` is useful while prototyping or when its normal/index helpers save work. Avoid rebuilding `ImmediateMesh` every frame.

## Roads and paths

Generate a graph before geometry. Nodes and typed edges carry width, walking space, slope limits, connections, and stable IDs. Derive all consumers from that graph:

- road mesh and junctions;
- terrain stamps;
- plot frontage;
- traffic lanes;
- pedestrian paths;
- navigation links;
- reachability validation.

Generate carriageway, side skirts, shoulders/sidewalks, and junction geometry deliberately. Validate winding, terrain clearance, slope, intersection connectivity, and landmark reachability.

## Buildings

Prefer a small parameterized archetype library. A building definition can control footprint, floor range, roof choices, facade grammar, door/window rules, colors, accessory weights, collision policy, LOD, and complexity budget.

The generator first creates a `BuildingRecipe`, including every chosen option and socket. Validate footprint, road access, terrain fit, openings, bounds, and estimated geometry before creating Nodes or meshes.

Reuse a procedural part library for walls, roofs, windows, doors, awnings, chimneys, balconies, fences, and signs. Use shared meshes and MultiMesh where identical parts repeat; merge noninteractive static parts within a chunk when that reduces draw calls without destroying culling.

## Vegetation, rocks, and props

Definitions specify biome weights, density, size range, slope limits, spacing, palette, LOD, collision, and render strategy. Candidate placement follows:

```text
sample candidate
-> check biome/rule probability
-> query height and slope
-> check occupancy/exclusions
-> validate budget
-> reserve footprint
-> emit recipe
```

Use bounded retries. A target count is not permission for an infinite loop. Report requested, placed, rejected, and retry counts.

Tree, rock, lamp, fence, and cloud generators should expose parameters that produce families of content, not individual assets. Keep visual variation deterministic.

## Landmarks

Landmarks are authored gameplay anchors with procedural construction or PackedScene visuals. They reserve space before ordinary content, grade terrain, expose road and spawn sockets, and protect view/access corridors.

Use PackedScene for interactive or behavior-rich landmarks. A noninteractive procedural landmark may output a static ArrayMesh. Do not make landmarks random clutter.

## Spatial constraints

Centralize occupancy in a `SpatialConstraintService`. Support at least:

- spatial hash/grid for nearby candidate lookup;
- circle/sphere footprints for vegetation and props;
- oriented rectangles or polygons for buildings;
- road corridor tests;
- slope and height ranges;
- biome/build-policy zones;
- exclusion, attraction, and view-corridor zones.

Reserve only after validation succeeds. Use conservative simple footprints for broad rejection, then exact tests for close candidates.

## Spawns and NPCs

Generate stable spawn sockets/recipes separately from live NPC state. Roads should provide a directed lane/walk graph where constrained movement is sufficient; do not require a full NavigationMesh for every road-bound agent.

Use PackedScene for important interactive NPCs. Use MultiMesh or lightweight pooled agents for ambient crowds. Validate minimum spacing and valid reachable surfaces.

## Procedural mesh guidance

- `ArrayMesh`: large deterministic static surfaces and direct packed arrays.
- `SurfaceTool`: convenient construction, append/transform, normals, indexing, and early prototypes.
- Primitive Mesh resources: reusable low-cost parts.
- `MultiMesh`: many instances of the same mesh/material.
- `PackedScene`: behavior, interaction, independent lifetime, or complex collision.

Do not use runtime CSG as the default mass-production path. Do not create one Node per grass blade, fence post, leaf, or distant decoration.
