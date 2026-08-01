# Changelog

All notable changes per release. Versions follow [semver](https://semver.org).

## v0.2.3 — 2026-08-01

Version housekeeping. No code changed.

- The tag history had split in two. An older, unprefixed line ran up to `0.2.2` in 2024; a newer, `v`-prefixed line restarted at `v0.1.0` in 2026 and reached `v0.1.2`. Neither was unambiguously the latest, and `pyproject.toml` still declared `0.2.2` — a version no tag in the newer line matched.
- `v0.2.3` sorts above both lines and ends the ambiguity. It supersedes the unprefixed `0.2.2` and the `v0.1.x` series alike.
- `pyproject.toml` now says `0.2.3`, so the declared package version and the git tag finally agree.
- The `v`-prefixed form is the one going forward. The old unprefixed tags stay where they are as history; nothing new will be cut without the `v`.

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
