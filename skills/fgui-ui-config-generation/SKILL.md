---
name: fgui-ui-config-generation
description: Generate FairyGUI/FGUI UI XML config files and package.xml registrations for this UiProject. Use when creating UI from a design image, converting a Laya .scene file, editing assets package ui XML, wiring GLoader image resources, or modeling visual state differences with controllers.
---

# FGUI UI Config Generation

Use this skill to create or update FairyGUI UI configuration files in `E:\Project\bzqy_sea\develop\trunk\code\client\UiProject`. Work directly with `assets/<package>/ui/**/*.xml` and `assets/<package>/package.xml`.

## Grounding

Before generating XML:

1. Identify the target package under `assets/`. If the user does not name one, infer it from the feature name or source path; use `assets/map` as the preferred structure example.
2. Read `assets/<package>/package.xml` to get the package id and existing resource/component ids.
3. Inspect nearby XML examples in the same package, especially `assets/map/ui` and `assets/map/ui/comp`, before choosing paths, names, or component style.
4. For source designs, keep reference images under `_view`, clean image resources under `tex`, text-bearing image resources under `txt`, and generated FairyGUI XML under `ui`.

## Package Rules

- Treat one business system as one FGUI package.
- Keep every business package organized with these folders:
  - `_view`: design/reference images, not exported.
  - `tex`: clean image resources without baked text.
  - `txt`: image resources with baked text.
  - `ui`: FairyGUI XML config files.
- Do not reference resources from another business package.
- Allow shared references only from public packages such as `com` and `font`.
- Prefer existing public components from `assets/com/ui/comp` for common buttons, goods items, costs, heads, tabs, progress bars, status stamps, scroll panels, return controls, counters, and placeholders.

## ID And URL Rules

Follow the ID rules from `E:\Project\zhetian_client\trunk\.agent\skills\fgui-xml-generation\SKILL.md`.

- Package id: 8-character base36 string, equivalent to `Math.random().toString(36).substring(2, 10)`, padded/regenerated until length is 8.
- Resource/component id: unique within a package, 5-character base36 string, equivalent to `Math.random().toString(36).substring(2, 7)`.
- Object id inside a component: `n{Index}_{Prefix}`.
  - `Index` increments from `0`.
  - `Prefix` is the first 4 characters of the parent component id.
  - Example: component id `g8306a` uses object ids such as `n0_g830`, `n1_g830`.
- FGUI resource URL format: `ui://{PackageID}{ResourceID}`.
  - Read package id from `<packageDescription id="...">`.
  - Find resource id from the matching `<image>`, `<component>`, or other resource entry in `<resources>`.
  - Example: package id `x05r956a` plus image id `v8g16u` becomes `ui://x05r956av8g16u`.

When adding a new XML component, register it in the target package's `package.xml` under `<resources>`:

```xml
<component id="{newId}" name="{FileName}.xml" path="/ui/{optionalSubdir}/" exported="true"/>
```

Match the `path` to the actual XML location. For example, `assets/map/ui/comp/UI/CityHead.xml` registers with `path="/ui/comp/UI/"`.

## Component Mapping

Generate FGUI XML that is easy for art and UI developers to replace later.

- Use `<loader>` / `GLoader` for image resources instead of fixed image components.
- Keep loader `url` values as `ui://...` URLs from `package.xml`.
- Preserve meaningful source names such as `btn_close`, `list_item`, `txt_title`, `icon_cost`, and `ctrl_state`.
- Use `<text>` for dynamic labels and values instead of baked text images when possible.
- Use existing common components for standard controls rather than rebuilding them from images.
- Use `<list>` for repeated content and create a reusable item component when the row/card has multiple children.
- Use transparent placeholder/click-area components from `com` where the UI needs layout spacing or larger hit targets.
- Use relations only when the component should resize or anchor with its parent; otherwise preserve explicit `xy` and `size`.

## Controllers And States

Represent visual state differences with controllers where practical.

- Add a clear controller name such as `ctrl_state`, `ctrl_tab`, `ctrl_quality`, `ctrl_empty`, or `button`.
- Use controller pages for mutually exclusive display states, such as empty/content, selected/unselected, locked/open, enough/not enough, or normal/pressed/disabled.
- Use gear attributes (`gearColor`, `gearDisplay`, `gearXY`, `gearSize`, etc.) to bind child differences to controller pages.
- Avoid duplicating whole component trees for state variants when a controller can switch visibility, color, position, image URL, or text state.
- For buttons, follow existing FGUI button/controller patterns in the package or `com` package before inventing a new state model.

## Input Workflows

### From an image or design reference

1. Put or reference the design image under `assets/<package>/_view`.
2. Determine which visual pieces must become replaceable art resources in `tex` or `txt`.
3. Confirm each resource exists in `package.xml`; if missing, add a resource entry with a unique 5-character id and the correct path.
4. Build the UI XML under `assets/<package>/ui`, using loaders for images, text nodes for dynamic copy, common components for standard controls, and controllers for state differences.
5. Register each new component XML in `package.xml`.

### From a Laya `.scene` file

1. Parse the scene hierarchy as structured data, not as loose text.
2. Preserve useful names, coordinates, sizes, visibility, list/container hierarchy, and text values.
3. Map image-like Laya nodes to FGUI `<loader>` nodes and resolve their image resources through the target package's `package.xml`.
4. Map labels/text inputs to `<text>` unless the source is intentionally a baked text image.
5. Map buttons to existing common button components when the style matches; otherwise create a local button component with a `button` controller.
6. Map panels/repeated children to `<list>` plus item components when data is repeated.
7. Convert obvious state-layer groups to controllers instead of separate duplicated nodes.
8. Register generated components in `package.xml`.

## Final Checks

Before finishing:

- Ensure every new id is unique within the target package or component.
- Ensure every `ui://` URL resolves to a resource in an allowed package.
- Ensure no business package references another business package.
- Ensure new XML files live under `assets/<package>/ui`.
- Ensure `package.xml` paths exactly match file locations.
- Ensure image resources are loaders/GLoaders unless there is a strong project-local reason otherwise.
- Ensure state variants use controllers where practical.
- Do not generate runtime TypeScript bindings unless the user explicitly asks for code changes outside the FGUI config files.
