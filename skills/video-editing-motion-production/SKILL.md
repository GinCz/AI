---
name: video-editing-motion-production
description: >-
  Professional video editing, motion graphics, programmatic video rendering (Remotion, FFmpeg), color grading (LUTs, ACES, Rec.709), timeline pacing, multi-camera synchronization, subtitle animation, and broadcast video codecs.
---
# Professional Video Editing, Motion Graphics & Programmatic Video Production

A master engineering manual for nonlinear video editing, motion graphics design, color grading science, subtitle animation pipelines, programmatic code-based video generation via Remotion, and high-performance FFmpeg rendering.

---

## 1. Timeline Editing Mechanics & Narrative Pacing

### A. Core Cut Taxonomy & Pacing Rules:
- **J-Cut & L-Cut**:
  - *J-Cut*: Audio of the incoming scene precedes the visual cut by 0.5–1.5 seconds. Pulls viewer curiosity forward and creates smooth conversational transitions.
  - *L-Cut*: Visual cuts to the next clip while the audio of the previous scene continues underneath. Essential for reaction shots and environmental continuity.
- **Match Cut**: Transitioning between two scenes that share similar visual compositions, geometric shapes, or directional movements.
- **Pacing to Cadence**: Edit rhythm matched to speech cadence and music beats without becoming predictable. Crucial moments require temporal breathing room (0.5s pause after impactful statements).
- **Jump Cut Elimination**: Disguising audio pauses and retakes in talking-head videos using punch-in zoom scaling (100% to 112% on key statements), B-roll overlays, or dynamic motion graphic text.

---

## 2. Color Science & Grading (LUTs, Rec.709 & HDR)

### A. Color Pipeline Stages:
1. **Normalization & Input Color Space Transform (CST)**:
   - Converting raw camera log profiles (Sony S-Log3, Canon C-Log, Apple ProRes Log, Blackmagic Film) to working intermediate space (ACEScc or DaVinci Wide Gamut).
2. **Primary Correction (Technical Balance)**:
   - Exposure adjustment using Waveform monitor (Blacks at 0 IRE, Middle Gray at 40–45 IRE, Whites peaking below 95 IRE).
   - White balance correction using RGB Parade (aligning Red, Green, and Blue channels on neutral reference whites and grays).
   - Contrast and pivot curve shaping.
3. **Secondary Correction (Selective Isolation)**:
   - Skin tone line alignment on Vectorscope (human skin pigmentation universally sits on the exact I-line regardless of ethnicity).
   - Hue vs Hue, Hue vs Saturation curves for selective sky or foliage refinement.
4. **Creative Look & Output CST**:
   - Applying creative Look-Up Tables (LUTs) with film emulation (Kodak 2383 / Fuji 3513 print stock).
   - Output transform mapped strictly to Rec.709 / Gamma 2.4 (SDR web and TV standard).

---

## 3. Programmatic Video Generation with Remotion

### A. Architecture & Core Concepts:
- Render videos programmatically using standard React components, TypeScript, and CSS.
- **Frame-based Time**: Time is calculated strictly in frames rather than seconds (`frame / fps`), guaranteeing zero audio/video desynchronization across renders.
- Interpolation functions: `interpolate(frame, [start, end], [valueA, valueB], { extrapolateRight: 'clamp' })`.
- Spring physics: `spring({ frame, fps, config: { damping: 12, mass: 0.5, stiffness: 100 } })` for organic motion graphics.

### B. Scalable Dynamic Template Architecture:
```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const AnimatedLowerThird = ({ title, subtitle }: { title: string; subtitle: string }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({ frame, fps, config: { damping: 14 } });
  const opacity = interpolate(frame, [0, 10], [0, 1]);

  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', padding: 80 }}>
      <div style={{ transform: `translateY(${(1 - entrance) * 60}px)`, opacity }}>
        <h1 style={{ color: '#FFFFFF', fontSize: 48, fontWeight: 800, margin: 0 }}>{title}</h1>
        <p style={{ color: '#00D2FF', fontSize: 24, fontWeight: 500, margin: '8px 0 0' }}>{subtitle}</p>
      </div>
    </AbsoluteFill>
  );
};
```

---

## 4. High-Performance Video Rendering via FFmpeg

### A. Broadcast-Grade Encoding Commands:
- **Ultra-Quality H.264 Web Master (Rec.709)**:
```bash
ffmpeg -i input_raw.mov -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +faststart -c:a aac -b:a 320k output_web.mp4
```
- **H.265 / HEVC 4K Archival Compression**:
```bash
ffmpeg -i master.mov -c:v libx265 -preset medium -crf 20 -tag:v hvc1 -pix_fmt yuv420p10le -c:a copy master_hevc.mp4
```
- **Automated Burn-in Subtitles with Styling**:
```bash
ffmpeg -i input.mp4 -vf "subtitles=subtitles.srt:force_style='FontName=Montserrat,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3,Outline=2,Shadow=0,MarginV=35'" -c:a copy output_subtitled.mp4
```

