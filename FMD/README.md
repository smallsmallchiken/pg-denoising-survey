# FMD — Fluorescence Microscopy Denoising Dataset

> **This directory intentionally contains no data.** The FMD dataset is **not hosted** in this repository (it is ~8.4 GB of raw microscopy images and should be downloaded from the official source).

## Download

**Official source:** https://github.com/yinhaoz/denoising-fluorescence

```bash
git clone https://github.com/yinhaoz/denoising-fluorescence.git
```

## About the dataset

- **Size**: 12,000 real fluorescence microscopy images
- **Modalities**: confocal, two-photon, and wide-field
- **Structure**: each configuration has repeated exposures enabling ground-truth estimation by temporal averaging
- **Noise model**: per-configuration Poisson–Gaussian parameters (slope `a`, intercept `b`) fitted to every raw frame

## Reference

Zhang, Y. et al. *A Poisson–Gaussian Denoising Dataset with Real Fluorescence Microscopy Images*. CVPR 2019.

In the notation of this survey, the slope `a` corresponds to `α` and the intercept `b` to `σ²` under the affine variance profile `Var(y) = α x + σ²`.

## Usage in this repository

The bundled `methods/` (VST-BM3D, VST-NLM, etc.) can be evaluated on FMD by downloading the data above and adapting the benchmark driver scripts in `benchmarks/`. See `docs/protocols.md` for the evaluation protocol.
