---
name: security-audit
description: Use when assessing a feature, service, or full repo for security risk. Maps the threat surface, walks the OWASP Top 10, and emits a finding report with severity counts. Suitable as a release-gate skill.
---

# security-audit

## 1. Threat surface mapping
List every place untrusted data enters the system: HTTP endpoints, queue
consumers, file uploads, env vars read at runtime, third-party webhooks,
client-side storage. For each, name the trust boundary it crosses.

## 2. OWASP Top 10 walk
For each of: Broken Access Control, Cryptographic Failures, Injection,
Insecure Design, Security Misconfiguration, Vulnerable Components,
Identification & Auth Failures, Software / Data Integrity Failures,
Security Logging & Monitoring Failures, SSRF — record either a finding or
"not applicable, because <reason>".

## 3. Secret hygiene
Grep for committed secrets. Verify `.env*` is in `.gitignore`. Check that
the CI logs don't echo env vars.

## 4. Dependency posture
Run the stack's audit tool (`pnpm audit`, `pip-audit`, `cargo audit`,
`govulncheck`, `dotnet list package --vulnerable`). Note severity counts.

## Output format

```
Findings: critical=N high=N medium=N low=N

[CRITICAL] <title>
  Where:    <file:line or component>
  Vector:   <how an attacker reaches it>
  Impact:   <what they get>
  Mitigation: <smallest viable fix>
```

Append the OWASP walk as an appendix so reviewers can see what was checked
even when there were no findings.
