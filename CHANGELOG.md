# Changelog

All notable changes per release. Versions follow [semver](https://semver.org).

## v0.1.2 — 2026-08-01

CI/infrastructure only. No code in this repo changed — the whole diff since v0.1.1 is under `.github/workflows/`.

- Split the pipeline: building and publishing stay in `pipeline.yml`, everything that leaves the host now lives in its own file beside it.
- The repo is mirrored to Codeberg as well as GitLab.
- The repo is archived to the Wayback Machine, Software Heritage and archive.org.
- Issues opened on either mirror are copied back to GitHub every six hours, and closed here when the original closes.
- Pull requests are switched off on both mirrors — they are force-pushed from GitHub, so anything merged there would be destroyed by the next sync. Issues and forking stay enabled.

## v0.1.1 — 2026-07-27

- Added a GitHub Actions CI status badge to the README.

## v0.1.0 — 2026-07-27

Add README status badges.

- Added self-hosted version and license badges (rendered as SVGs on the `badges` branch by the `create-badges` CI job, no third-party render service). Wired a badges job into pipeline.yml.
