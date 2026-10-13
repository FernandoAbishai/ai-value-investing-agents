# Upstream review — October 2026

This document records the selective upstream review of [`xbtlin/ai-berkshire`](https://github.com/xbtlin/ai-berkshire) performed for this independently maintained English-first edition.

## Review boundary

- Last previously incorporated upstream framework point: `fd83d06347c6e3ee50133cda6962f40e226b5252` (`era-alpha`, August 29, 2026).
- Upstream head reviewed: `ab56abcb31ef8e3a92d925f1b18fb339341ac9d3` (October 12, 2026).
- The review distinguishes reusable framework/tooling changes from upstream-specific research output, portfolio records, publishing material, and generated media.

This repository is not intended to mirror every upstream commit. Upstream research reports remain source material and are synchronized selectively when they are useful and compatible with this edition's attribution, language, privacy, and maintenance boundaries.

## Reusable changes incorporated

### Hardened report indexing

Initially ported in PR #22 as commit `eb7b76eaacd06c38ad8d6306d7f368667dc445a1`, then adapted for this fork's verified-example taxonomy and bootstrapped in follow-up PRs.

The completed integration includes:

- `tools/reports_index.py` for deterministic human- and machine-readable report inventories;
- `reports/_index/config.json` and `reports/_index/README.md` for archive classification and maintenance rules;
- fail-closed publication behavior so untracked, ignored, and intent-to-add drafts are excluded;
- Unicode-stable Git history handling;
- explicit UTF-8 console behavior for Windows;
- cross-platform regression tests using real temporary Git repositories;
- `reports/README.md` and `reports/index.json` generated from this fork's exact tracked archive;
- fork-specific classification of `reports/examples/` under `Verified English examples`;
- a permanent full-history, read-only report-index drift check in GitHub Actions.

The implementation is a semantic port rather than a direct cherry-pick. The first cross-platform validation exposed Windows-specific encoding and file-system assumptions that were corrected before merge.

## Upstream changes reviewed but not copied

### Codex generated-file drift CI

Upstream added a narrower generated-file synchronization check. This fork already validates canonical/generated Codex parity as part of a broader Ubuntu, macOS, and Windows CI matrix, including installation lifecycle tests. No additional port is required.

### Research reports, articles, PDFs, figures, and portfolio records

Most post-August upstream commits add or revise research output rather than framework capabilities. They are intentionally not bulk-imported. A bulk sync would increase repository size and maintenance noise without improving the reusable workflows.

### Upstream README and maintainer instructions

Upstream documentation changes around report indexing are conceptually incorporated through this edition's report-index documentation. Upstream-specific branding, publication channels, personal portfolio material, and Chinese operational instructions are not copied into maintained English-first surfaces.

### Upstream `.gitignore` additions

The fork already protects local material and common credential files through `/local/`, `.env*`, `*_token.txt`, `*.token`, and related rules. An upstream-specific ignored report directory that does not exist in this fork is not relevant.

## Current synchronization policy

For future upstream reviews:

1. Prefer reusable methodology, tooling, correctness fixes, and security/privacy hardening.
2. Adapt changes to the English canonical sources first; regenerate Codex surfaces from those sources.
3. Do not import upstream personal performance claims or portfolio records as maintainer results.
4. Do not bulk-copy historical research merely to reduce commit divergence.
5. Keep each port small, reviewable, reversible, and covered by the existing validation matrix.
6. Record the upstream commit boundary after each completed review.

## Report index bootstrap status

Complete. The generated report index was produced by executing the real generator against a full-history checkout of this fork, then immediately verified with `python3 tools/reports_index.py --check`.

The committed inventory contains 2,203 tracked reports across 109 company groups and 16 themes as of this review. A permanent read-only GitHub Actions workflow now runs the full-history `--check` gate on pull requests and `main` pushes so index drift is detected before release.
