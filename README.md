# Live Face, Motion & Air Quality Particles

A single-file browser app: your webcam feed with face detection, motion detection,
and a particle system where each pollutant (PM10, PM2.5, CO) is its own live-data-driven
color and behavior, fetched from the [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api).
Switch between cities to compare — particle count, size, and a red overlay tint all
scale with real air quality readings.

Everything runs client-side in the browser; nothing is uploaded anywhere.

## Running locally

Serve the folder over HTTP(S) — `getUserMedia` (camera access) doesn't work over `file://`:

```bash
python3 -m http.server 8791
```

Then open `http://localhost:8791/index.html`.

To access it from a phone on the same network, you'll need HTTPS (a self-signed cert
works fine for this). See `serve_https.py` for a minimal example.

## Features

- Face detection via Google's MediaPipe Tasks Vision (runs locally, model loaded from CDN)
- Motion detection via frame-differencing (no external model)
- Front/back camera flip on devices with multiple cameras
- Air quality particle system: pollutant concentration drives particle count/size/color,
  camera motion scatters them
- City switcher with live AQI fetched from Open-Meteo
