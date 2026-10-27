# Source-run image for third-party MCP introspection of the SAME published v1.2.0 server.
# No remote model calls, downloaded theories, credentials, or separate MCP service.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /opt/ai-answer-guard
COPY machine-discovery/ ./machine-discovery/
COPY metadata/person-name-policy-v1.json ./metadata/person-name-policy-v1.json
COPY skills/nakagawa-originals/references/structural_bridges.json ./skills/nakagawa-originals/references/structural_bridges.json
COPY human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md ./human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md
COPY derivatives/ ./derivatives/
COPY LICENSE ./LICENSE
USER 65534:65534
ENTRYPOINT ["python3", "-u", "machine-discovery/nakagawa-theory-mcp.py"]
