# Source And Safety Notes

## Official Status

This repository is not an official government API and is not affiliated with the Korea Office of Civil Aviation or the Korea AIM service.

It is an open-source interoperability layer built around publicly reachable NOTAM-related workflows and response formats.

## What The Project Provides

The repository provides:

- collection and normalization code
- local persistence patterns
- monitoring and change detection flows
- a self-hostable reference API
- synthetic samples for testing and documentation

## What The Project Does Not Promise

The repository does not promise:

- uninterrupted access to upstream systems
- stable response formats from source systems
- complete or authoritative operational coverage
- suitability as the sole input for safety-critical flight decisions

Always verify against official aviation briefing and operational sources before real-world use.

## Sample Data Policy

Prefer synthetic or clearly safe sample fixtures in the repository.

Avoid committing:

- secrets or access credentials
- large operational dumps
- private or restricted data exports
- material with unclear redistribution rights

## Contribution Notes

When proposing parser or schema changes, include enough context for others to verify the change without needing private datasets.

When reporting source-system changes, include:

- the affected component
- the observed behavior change
- a minimal reproducible example when possible
- any uncertainty about field meaning or operational interpretation

## Maintainer Boundary

This repository is meant to lower integration friction for Korean NOTAM-related tooling.

It is not a substitute for official briefings, operational validation, or regulatory review.
