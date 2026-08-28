# Framework and determinism

Read this reference for architecture, generator contracts, stable seeds, data ownership, execution order, caching, or generator replacement.

## Recommended modules

```text
ProceduralWorld/
|- Core/
|  |- WorldGenerationController
|  |- GenerationContext
|  |- SeedService
|  |- GeneratorRegistry
|  |- SpatialConstraintService
|  |- TerrainHeightService
|  |- GenerationBudget
|  |- GenerationCache
|  `- GenerationReport
|- Data/
|  |- WorldDefinition
|  |- BiomeDefinition
|  |- RoadDefinition
|  |- BuildingDefinition
|  |- VegetationDefinition
|  |- PropDefinition
|  |- LandmarkDefinition
|  `- SpawnDefinition
|- Generators/
|- Geometry/
|- Runtime/
`- Validation/
```

Adapt names to existing project conventions. Preserve responsibilities and contracts, not this exact folder tree.

## Generator contract

A generator exposes a stable ID and version, generates a pure plan, validates it, then spawns only valid output. A C# shape can be:

```csharp
public interface IWorldGenerator<TPlan>
{
    string GeneratorId { get; }
    int Version { get; }
    TPlan GeneratePlan(GenerationContext context);
    ValidationResult Validate(TPlan plan, GenerationContext context);
    SpawnResult Spawn(TPlan plan, GenerationContext context);
}
```

Generation plans contain serializable recipes, placements, bounds, reservations, dependencies, estimated cost, and diagnostics. They do not contain live Node references.

## Stable random streams

Hash a canonical byte/string representation of:

```text
world seed
generator id
generator version
chunk coordinate or stable region id
optional item/archetype id
```

Use the result as the seed for a local `RandomNumberGenerator`. Never call `Randomize()` during deterministic generation. Avoid platform-dependent hashing and unordered Dictionary iteration when order affects output. Sort stable IDs before generation.

Record a `WorldPlanHash` over canonical plan data. Determinism means equal seed + settings + generator versions produce an equal hash, not merely a visually similar result.

## Data ownership

`GenerationContext` owns or references:

- world seed and settings;
- generator version manifest;
- biome map;
- height/normal queries;
- road graph;
- landmark anchors;
- occupancy and reservations;
- chunk coordinate and bounds;
- performance budget;
- cancellation state;
- generation report.

Generators communicate through declared plan outputs and shared services, not direct calls to sibling generator internals.

## Recommended order

```text
Base terrain plan
-> fixed landmark anchors
-> primary road graph
-> terrain stamps/flatten fields
-> final terrain
-> road mesh
-> landmark recipes
-> building plots and recipes
-> vegetation and props
-> NPC/object spawns
-> collision/navigation products
-> final validation and report
```

Anchors precede roads because roads may need to reach them. Visual landmark spawning can happen after terrain and roads are finalized.

## Fixed plus procedural

Treat fixed content as constraints:

- stable anchor or positioning rule;
- protected footprint;
- terrain stamp;
- required road socket;
- view corridor;
- spawn sockets;
- exclusion and attraction zones.

Procedural systems fill surrounding space while respecting those constraints. Fixed does not require a literal coordinate: a stable rule such as "highest valid point in the north region" is also fixed for a given world plan.

## Versioning and cache

Cache keys include world seed, settings hash, generator IDs/versions, content-catalog version, and chunk coordinate. Increment a generator version when its output semantics change. A saved seed without versions is not sufficient to reproduce an old world after algorithms change.

Cache plans or static products that are expensive and deterministic: terrain arrays, road graph, building recipes, placement manifests, static ArrayMeshes, MultiMesh buffers, and validation reports. Do not cache transient agent state as world-generation data.
