# syntax=docker/dockerfile:1
# Build from the repository root:
# docker build --file Business/Marketing/gavin_schilling_marketing/Dockerfile --tag gavin-marketing:dev .

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r /tmp/requirements.txt

# Preserve the repository-relative path used by Django settings without
# copying unrelated websites, client assets, or other repository folders.
COPY --chown=10001:10001 Business/Marketing/gavin_schilling_marketing/ /app/Business/Marketing/gavin_schilling_marketing/

USER 10001:10001
WORKDIR /app/Business/Marketing/gavin_schilling_marketing

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
