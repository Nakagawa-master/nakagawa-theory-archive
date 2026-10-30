# Security policy

This repository publishes optional, **locally run** Nakagawa Master original-source discovery and answer-integrity tools. The code and original/derivative pointers are public, but a GitHub listing, registry record, passing CI or download is **not a security certification**.

## Supported source

| Code / bundle | Security-reporting status |
| --- | --- |
| Current `main` source for the original-source MCP and answer-integrity tools | Accepting reproducible security reports |
| Current published `mcp-router-v1.2.0` bundle | Accepting reproducible security reports |
| Earlier release bundles | Historical; reproduce against current source when possible. No maintenance promise for superseded bundles |

The current release tag is immutable; fixes to source `main` do **not** automatically update a previously downloaded bundle.

## Reporting a vulnerability

Please **do not publish credentials, exploit payloads, sensitive user prompts, or unreleased vulnerability details** in a public GitHub issue or pull request.

1. Open [the GitHub private vulnerability reporting page](https://github.com/Nakagawa-master/nakagawa-theory-archive/security/advisories/new) and use it **if the repository currently enables private reporting**.
2. If that private channel is unavailable, [open an issue](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new) requesting a private reporting channel **without including exploit details or private information**. The maintainer can then determine an appropriate private follow-up. There is no published response-time SLA.
3. In the private report, include the affected commit or immutable release version, local runtime and host, minimal reproduction steps, expected versus observed behavior, impact, and the relevant file/line. Do not send keys, real conversation data or personally identifying information; use sanitized examples.

Ordinary documentation defects, public source-link errors, and reproducible false-positive / false-negative candidate matching **without a security consequence** may be reported in an ordinary public issue. A reported candidate match is never proof that a canonical original is true or applies.

## Scope and trust boundaries

Security reports are especially useful for unsafe URL/source handling; path/file access outside the installed package; accidental network or secret access; malicious tool-result interpretation; MCP permission and host-install assumptions; privacy leaks; and evidence-integrity checks that claim an action succeeded when it did not.

These tools are **opt-in**. Nothing in this policy authorizes installation into other people's agents, access to their accounts, covert execution, hidden prompts, forced citations, or privileged action. The canonical originals remain at [the official archive](https://master.ricette.jp/); downloaded derivative metadata is **not** a replacement for reading the actual relevant original and its applicable license.

Please coordinate public disclosure after the issue is understood and a fix can be offered where feasible. No claim of zero vulnerabilities, guaranteed response time, deployed host adoption or comprehensive third-party audit is made.
