# MTA Lua review practices

## Contents

- Trust boundaries
- Client and server separation
- Events and handlers
- State and synchronization
- Performance
- Resource lifecycle
- Maintainability

## Trust boundaries

- Treat every value received from a client as untrusted, including element references, prices, permissions, positions, and identifiers.
- Validate remote-event arguments on the server and check the implicit `client` variable when the event is remotely triggerable.
- Keep money, inventory, ACL, account, punishment, and authoritative gameplay decisions on the server.
- Grant ACL rights narrowly. Do not require `general.ModifyOtherObjects` when a resource-specific right is sufficient.
- Never ship secrets or privileged logic in client files; clients can inspect and modify downloaded scripts.

## Client and server separation

- Put rendering, local input, camera, GUI, and purely visual effects on the client.
- Put persistent and authoritative state transitions on the server.
- Use shared scripts only for deterministic helpers and constants that genuinely belong on both sides.
- Confirm every API is available on the side where it is called. Use `$mta-docs` to verify.

## Events and handlers

- Prefer explicit event sources over attaching broad handlers to `root` when a narrower element is available.
- Remove handlers created for temporary UI, streamed elements, or short-lived modes.
- Avoid anonymous handler functions when they must later be removed; retain the function reference.
- Set `allowRemoteTrigger` to `true` only for events intentionally callable across the network.
- Prevent event feedback loops when client and server handlers update the same state.

## State and synchronization

- Avoid using element data as a general-purpose database or high-frequency message bus.
- Synchronize only data that other clients actually need.
- Keep resource-local tables for transient server state when network synchronization is unnecessary.
- Define ownership and cleanup rules for every table keyed by players, vehicles, or elements.
- Check `isElement` before using references that may outlive streamed or destroyed elements.

## Performance

- Move invariant work out of `onClientRender`, `onClientPreRender`, and other frame handlers.
- Cache stable lookups, dimensions, colors, and parsed configuration, but invalidate caches deliberately.
- Avoid scanning all elements or players every frame.
- Prefer one managed timer over many equivalent per-element timers when behavior permits.
- Batch network updates and send compact payloads at the lowest useful frequency.
- Measure before introducing complex caching or micro-optimizations.

## Resource lifecycle

- Initialize from `onResourceStart` or `onClientResourceStart` as appropriate.
- Release timers, handlers, browsers, render targets, textures, and temporary elements on shutdown.
- Handle player quit, element destruction, and resource restart paths.
- Keep `meta.xml` exports, script sides, cache flags, and file declarations consistent with the resource.

## Maintainability

- Keep modules cohesive and expose narrow interfaces.
- Use `local` by default; reserve globals for intentional shared interfaces.
- Name event handlers and network events by domain action rather than UI implementation.
- Return or surface actionable errors instead of silently swallowing failures.
- Separate validation, authorization, mutation, and presentation in security-sensitive flows.
