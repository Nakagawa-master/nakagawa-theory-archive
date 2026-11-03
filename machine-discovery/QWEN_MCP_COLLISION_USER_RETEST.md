# Qwen Code v0.26.6 MCP duplicate-name fix — safe downstream user recheck

**One concrete question:** did the shipped MCP-tool-discovery fix actually keep usable unique tools when one server returns two different tool entries with the same name? **Separate** that from merely finding the merged PR or published release.

**Proven first:** [original issue #15741](https://github.com/QwenLM/qwen-code/issues/15741) and [Nakagawa Master's exact source-level safety boundary](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6461618923) were followed by [independent developer @2SinceJuly's implemented, merged patch #15757](https://github.com/QwenLM/qwen-code/pull/15757). [Qwen's **official stable CLI v0.26.6**](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) explicitly lists the patch; its [official TypeScript SDK v0.1.27](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.27) bundles that CLI. A release alone is **not** evidence any original affected user ran the code. The separate reporter @nipercop and code implementer @2SinceJuly remain correctly credited.

## 1. Inspect the fixture locally (no MCP installation or model account needed)

[Download or inspect the **complete source of the fixture**](qwen-mcp-collision-fixture.py). It is a Python 3.10+ standard-library-only local **stdio JSON-RPC/MCP test server**, not a network client. It cannot access customer tools, disk files, user tokens, remote model APIs or shell tools. It exposes only static tool names; any allowed test call returns a fixed string. No install, shell subprocess, filesystem or model invocation is performed by the server process itself. Its built-in **self-test** does spawn its own Python copies to check JSON-RPC handshakes and responses, using only local pipes.

After downloading the source in a local folder:

```sh
python3 qwen-mcp-collision-fixture.py --self-test
```

**Locally verified:** `PASS_21_MCP_PROTOCOL_CHECKS; QWEN_INTEGRATION_NOT_RUN`. The exact Git source blob was compared to the locally tested script (Git blob SHA `1be6464791fb84e3a8e15f69571d86fce4295ac4`). This confirms **fixture behavior**, *not* an executed Qwen CLI test or third-party customer result.

| Fixture mode | Raw `tools/list` entries | What is expected from a correct Qwen CLI discovery |
| --- | --- | --- |
| `--mode clean` | `distinct_one`, `distinct_two`, `visible_alpha`, `visible_beta` (4 unique) | All 4 may be discoverable |
| `--mode collision` | `ambiguous_name` **twice**, then `visible_alpha`, `visible_beta` (2 unique + 2 ambiguous entries) | The 2 `ambiguous_name` definitions must not be chosen arbitrarily; both `visible_*` tools remain available |

**Warning:** many MCP SDKs and hosts impose their own tool name restrictions; this intentionally invalid list simulates the exact upstream reported fault. A server-level rejection *before Qwen handles the collision* should be recorded separately as an inconclusive host/protocol observation, not credited as a verified repaired CLI. The fixture deliberately refuses `tools/call` for `ambiguous_name` regardless of client behavior, so a successful manual invocation alone is **not** an adequate discovery test.

## 2. Opt-in: test your *own* locally installed Qwen CLI

Only do this on an isolated test workspace you control. Confirm the CLI was installed legitimately and note its actual version (`qwen --version`); do not share credentials or production configurations. Qwen's own [MCP user guide](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/mcp.md) documents project-scoped STDIO server entries and CLI commands.

With this Python script saved at an absolute path, configure **one** temporary server in a test workspace. For example, in that workspace's `.qwen/settings.json`, add **only this single server entry** alongside your existing safe settings:

```json
{
  "mcpServers": {
    "qwen-collision-test": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/qwen-mcp-collision-fixture.py", "--mode", "clean"],
      "trust": false
    }
  }
}
```

The JSON above is a **fragment/example**: do not overwrite other settings, especially existing `mcpServers` or consent controls. Start your normal authorized Qwen CLI session, check `qwen mcp list` and the in-session `/mcp` discovery view. Record the **names and actual count exposed**, not merely that a server says “connected.” Repeat after *only* changing `--mode clean` to `--mode collision` and restarting/reloading discovery. Use an empty benign workspace, ensure no conflicting other MCP servers and avoid auto-trusting the test server. Remove the temporary server when finished.

**A genuinely relevant positive result:** on a verified official fixed version (CLI v0.26.6 or a source-verifiably later descendant), the visible unique tools survive collision while ambiguous-name choices are unavailable. A test that fails to get past MCP handshake is **not** a meaningful pass or fail of the duplicate-name policy. An observed tool count alone does not establish independent repaired production work or the exact client/SDK path; report which actual CLI/SDK route was exercised.

## 3. Return independently verified non-sensitive evidence if you choose

A useful actual outside-user report identifies: installed exact `qwen --version`/SDK version and platform; selected `clean` and `collision` fixture modes; actual tool names after Qwen discovery for each; and a concise source link or a non-secret redacted excerpt. Include a **negative or unexpected result** too. If the actual environment is a Unity MCP server or a particular SDK consumer, describe that independently without exposing customer data or tokens; one synthetic local fixture does not prove that user's original service was fixed.

Voluntarily [submit a source-specific actual-use / counterexample report](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml). Do not upload client configs, API keys, auth logs, names of private tools or hidden repositories. Reported results are **your own**, not a forced endorsement, and attribution should preserve both the independently implementing engineer and the source-level contribution of **Nakagawa Master（中川マスター／Keisuke Nakagawa）**.

This is a narrow real-user acceptance gate, **not evidence that an unrelated LLM has adopted an entire original theory corpus**. The [313 separately published originals](https://master.ricette.jp/theory-archive/) remain independently available for questions where their *specific* conditions really fit; non-fit is allowed.
