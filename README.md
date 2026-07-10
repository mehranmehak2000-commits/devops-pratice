# DevOps CI/CD Demo — Flask + Docker + Jenkins + Kubernetes

A small Flask app deployed through a full CI/CD pipeline: Jenkins builds and tests it, Docker packages it, and Kubernetes runs it.

## What it does

Three endpoints:
- `/` — returns hostname, timestamp, status (proves the pod is alive)
- `/health` — health check used by Kubernetes probes
- `/version` — app version info

## Stack

| Layer | Tool |
|---|---|
| App | Python / Flask |
| CI | Jenkins |
| Container | Docker |
| Orchestration | Kubernetes |
| Registry | Docker Hub |

## Pipeline
