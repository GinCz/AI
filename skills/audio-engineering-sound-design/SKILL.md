---
name: audio-engineering-sound-design
description: >-
  Professional audio engineering, sound design, podcast and vocal post-production, mixing, mastering, dynamic processing (compression, limiting, gating), equalization (parametric EQ), FFmpeg audio filter automation, and acoustic loudness compliance (LUFS EBU R128).
---
# Professional Audio Engineering, Sound Design & Acoustic Post-Production

A comprehensive studio reference manual for vocal recording, podcast production, acoustic sound design, spectral cleaning, mixing, mastering, dynamic processing, and automated programmatic audio workflows via FFmpeg.

---

## 1. Acoustic Signal Chain & Vocal Capture

### A. Microphone Physics & Transducer Types:
- **Dynamic Microphones (e.g., Shure SM7B, Electro-Voice RE20)**:
  - Low sensitivity, high SPL tolerance, cardioid polar pattern.
  - Ideal for untreated rooms due to superior rejection of off-axis room reverberation.
  - Requires clean high-gain preamplification (+55dB to +60dB clean gain or inline boosters like Cloudlifter/FetHead).
- **Condenser Microphones (e.g., Neumann U87, Rode NT1-A)**:
  - High sensitivity, rapid transient response, wide frequency spectrum.
  - Requires dedicated acoustic room treatment (absorption coefficients NRC >= 0.75) to prevent hollow room flutter.
- **Proximity Effect & Polar Patterns**:
  - Bass boost occurs as the vocal source moves closer to directional (cardioid) capsules. Controlled at 10–15 cm with pop-filter at 45° angle to prevent plosives ('P', 'B' air bursts).

---

## 2. Dynamic Processing & Signal Processing Pipeline

### A. Core Vocal Post-Production Chain:
1. **High-Pass Filtering (Low Cut)**:
   - 18dB/octave slope steep cut at 75–85 Hz to eliminate HVAC rumble, footstep vibrations, and sub-audible mic stand handling noise.
2. **Subtractive / Surgical Parametric EQ**:
   - Narrow Q notch cuts (Q = 5 to 10) targeting harsh room resonances, comb-filtering artifacts, or nasal boxiness (typically 300–500 Hz for boxiness, 2.5–4.5 kHz for harsh sibilance).
3. **De-Essing (Frequency-Specific Dynamic Compression)**:
   - Split-band compression focused on 5 kHz – 8 kHz to tame aggressive dental sibilance ('S', 'Sh', 'Ch') without dulling overall vocal air.
4. **Compression (Two-Stage Serial Compression)**:
   - *Stage 1 (Peak Tamer)*: Fast attack (0.5–2 ms), fast release (50–100 ms), high ratio (4:1 to 6:1) catching only the loudest sudden peaks (2–3 dB gain reduction).
   - *Stage 2 (Level Smoothing / Optical)*: Slow attack (10–30 ms), smooth auto-release (e.g., LA-2A style optical model), mild ratio (2:1 to 3:1) providing 2–4 dB of gentle RMS glue.
5. **Additive EQ (Tonal Shaping)**:
   - Broad high-shelf boost (Q = 0.7) above 10–12 kHz for high-end "air" and perceived clarity; subtle wide bell boost at 1.5–2.0 kHz for intelligibility.
6. **Limiting**:
   - Brickwall peak limiter set to True Peak ceiling of -1.0 dBTP to prevent inter-sample clipping during lossy MP3/AAC compression encoding.

---

## 3. Loudness Standards & Delivery Formats (LUFS / EBU R128)

### A. Target Loudness Metrics:
- **Streaming Platforms (Spotify, YouTube, Apple Podcasts, Tidal)**:
  - Integrated Loudness: **-14 LUFS** (music / streaming audio) or **-16 LUFS** (podcasts and spoken word).
  - Maximum True Peak: **-1.0 dBTP** (leaves headroom for codec transcoding).
  - Maximum Loudness Range (LRA): 4 to 8 LU for podcasts (tightly controlled consistency).
- **Broadcast Standards**:
  - European Television: EBU R128 (-23.0 LUFS ±0.5 LU, max True Peak -1.0 dBTP).
  - US Television: ATSC A/85 (-24.0 LUFS).

---

## 4. Automated Audio Post-Production via FFmpeg

### A. Programmatic Audio Processing Scripts:
- **Two-Pass EBU R128 Loudness Normalization**:
```bash
# Pass 1: Measure loudness statistics
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.0:LRA=7:print_format=json -f null -

# Pass 2: Apply measured normalization with exact linear parameters
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.0:LRA=7:measured_I=-22.4:measured_TP=-2.1:measured_LRA=10.2:measured_thresh=-33.0:offset=0.2 -ar 48000 -c:a pcm_s24le output_mastered.wav
```
- **Vocal Gate, EQ and Compression Filtergraph**:
```bash
ffmpeg -i raw_voice.wav -af "highpass=f=80,agate=threshold=-36dB:ratio=2:attack=10:release=100,acompressor=threshold=-20dB:ratio=3:attack=15:release=120:makeup=4dB,deesser=i=0.5:m=0.5:f=0.6" -c:a flac cleaned_voice.flac
```

