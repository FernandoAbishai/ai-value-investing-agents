# Public Launch Publishing Checklist

Use this checklist before publishing the launch article, social posts, video, screenshots, or a new example report.

## 1. Repository state

- [ ] `main` contains the intended release or launch changes.
- [ ] The latest CI run passes on Ubuntu, macOS, and Windows.
- [ ] `python3 scripts/repository_quality.py` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] Both generated-artifact checks pass.
- [ ] The release, README, installation guide, and examples use the current repository name.
- [ ] No temporary workflow, migration script, scratch file, or private asset remains.

## 2. Research and financial claims

- [ ] Every material number has a source, period, currency, and unit.
- [ ] Current claims were refreshed on the publication date rather than recalled from an older report.
- [ ] Point-in-time examples retain their original cutoff and are not described as current recommendations.
- [ ] GAAP and adjusted metrics are labeled separately.
- [ ] Derived calculations show inputs or link to the verification register.
- [ ] Incompatible company definitions or reporting periods are not ranked as if equivalent.
- [ ] Estimates, assumptions, scenarios, and analytical judgments are visibly labeled.
- [ ] Past performance is not presented as a guarantee or independently audited result without evidence.

## 3. Attribution and identity

- [ ] The maintained edition is identified as AI Value Investing Agents.
- [ ] Lineage to the original project is included where context requires it.
- [ ] Historical reports and performance material are attributed to the original maintainer.
- [ ] Real-person-inspired commentary is labeled as interpretation unless directly quoted from a reliable source.
- [ ] No wording implies endorsement by investors, companies, Anthropic, OpenAI, or the original maintainer.
- [ ] Product and company logos are used only when permitted; the default social card uses no official logos.

## 4. Privacy and security

- [ ] Screenshots hide bookmarks, notifications, account menus, email addresses, local usernames, shell history, and unrelated tabs.
- [ ] Terminal output uses temporary or redacted paths.
- [ ] No token, API key, private URL, cookie, credential, unpublished holding, or confidential document appears.
- [ ] Browser developer tools and network panels are closed unless required and sanitized.
- [ ] Video metadata, file names, and exported assets do not expose private directories.
- [ ] Security issues are directed to private vulnerability reporting, not public comments.

## 5. Installation demonstration

- [ ] The demo uses `--dry-run` before installation.
- [ ] Installation occurs in temporary directories or a dedicated test profile.
- [ ] `doctor --all` passes on screen.
- [ ] The video explains the external manifest and backup behavior.
- [ ] The video does not imply that the manager downloads code or runs `git pull`.
- [ ] Backward-compatible scripts are described as aliases, not separate installation systems.

## 6. Video quality

- [ ] The recording is at least 1080p and text remains legible on mobile.
- [ ] The title and thumbnail describe auditable research rather than promising returns.
- [ ] Chapters match the final edit.
- [ ] Long commands and URLs are available in the description.
- [ ] Captions correctly preserve company names, ticker symbols, currencies, and technical terms.
- [ ] Music and visual assets have appropriate rights.
- [ ] The final frame includes the repository URL and research disclaimer.

## 7. Platform-specific review

### LinkedIn

- [ ] The first two lines explain the project without requiring “see more”.
- [ ] The post contains one primary repository link and avoids excessive hashtags.
- [ ] The social preview renders correctly after the repository image update.

### X

- [ ] Every post fits the current platform limit at publication time.
- [ ] The first post states the concrete problem and links to the repository.
- [ ] The thread does not repeat the same claim without adding evidence.

### Reddit

- [ ] The selected community allows project posts and the post follows its self-promotion rules.
- [ ] The title is descriptive rather than promotional.
- [ ] The body explains limitations, attribution, and why feedback is requested.

### Hacker News

- [ ] The title begins with “Show HN” only when the project is publicly usable.
- [ ] The submission text focuses on implementation and technical trade-offs.
- [ ] Comments are answered with evidence and without arguing about investment conclusions.

### YouTube

- [ ] The description includes repository, release, examples, and disclaimer links.
- [ ] The pinned comment asks for scoped feedback and warns against posting sensitive data.
- [ ] The video does not present the point-in-time Microsoft example as a live recommendation.

## 8. Feedback readiness

- [ ] Structured issue forms are visible and render correctly.
- [ ] `SUPPORT.md` explains supported and unsupported requests.
- [ ] A public launch-feedback issue exists and links to the correct forms.
- [ ] The maintainer has a plan for duplicates, incomplete reports, unsafe disclosures, and out-of-scope advice requests.
- [ ] Feedback will be summarized into scoped issues or milestones rather than implemented directly from vague comments.

## 9. Final publication gate

Publish only when all applicable checks above are complete.

After publication, record:

```text
Platform:
URL:
Published at:
Repository commit:
Research cutoff referenced:
Follow-up date:
Known correction or limitation:
```

If a material error is discovered, correct the source repository first, document the correction, and then update or annotate each external post. Do not silently change a financially material claim.
