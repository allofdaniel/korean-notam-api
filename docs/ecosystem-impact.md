# Ecosystem Impact

## Problem

Korean NOTAM data is important for aviation software, research, airport operations, and emerging drone or UAM products.

In practice, independent developers and small teams still lack an easy public developer-facing API for this data.

That creates avoidable friction:

- manual lookup workflows do not compose well into software
- downstream tooling has to rebuild the same collection layer
- small teams cannot easily prototype Korean aviation data products

## What This Repository Contributes

This repository is meant to be an open-source infrastructure layer.

It provides:

- collection code for Korean NOTAM sources
- normalization and local persistence patterns
- monitoring and change-detection workflows
- a self-hostable FastAPI reference implementation
- synthetic fixtures and tests so the interface can be reused safely

## Who Can Build On Top Of It

- aviation research groups
- flight-planning prototypes
- drone and UAM briefing tools
- airport operations dashboards
- alerting, summarization, or analytics systems

## Why This Matters Even Without Large Public Metrics

Infrastructure repositories are often valuable before they accumulate stars.

This project targets a specific gap:

- Korean NOTAM data access is operationally useful
- the integration burden is higher than it should be
- reusable open-source building blocks reduce that burden for the next team

The expected value is downstream enablement, not only direct end-user traffic.

## Open-Source And Hosted Service Can Coexist

This repository is the open-source core.

A separate hosted or commercial API can exist on top of the same code without reducing the OSS value. The reusable part is the collector, schema, monitoring logic, and reference API surface that others can self-host or adapt.
