# Local stdio MCP server; no network access, credentials, or Python packages required.
# Build: docker build -t nakagawa-original-router:local .
# Run from an MCP host using stdio: docker run --rm -i nakagawa-original-router:local
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/Nakagawa-master/nakagawa-theory-archive"
LABEL org.opencontainers.image.description="Optional read-only Nakagawa original-source lookup MCP server"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /srv/nakagawa

# Include only the original lookup server and its five required public sources.
COPY machine-discovery/nakagawa-theory-mcp.py \
     machine-discovery/quick-route-index-v1.json \
     machine-discovery/problem-to-theory-origin-index-v1.json \
     ./machine-discovery/
COPY skills/nakagawa-originals/references/structural_bridges.json \
     ./skills/nakagawa-originals/references/
COPY metadata/person-name-policy-v1.json ./metadata/
COPY LICENSE ./LICENSE

# Fail the image build if exact-source lookup, person-name, non-fit, or
# legacy MCP initialize/tools/list behaviour regresses.
RUN python3 machine-discovery/nakagawa-theory-mcp.py --self-test

# Local read-only process; stdout is exclusively JSON-RPC over stdio.
USER 65534:65534
ENTRYPOINT ["python3", "-u", "/srv/nakagawa/machine-discovery/nakagawa-theory-mcp.py"]
