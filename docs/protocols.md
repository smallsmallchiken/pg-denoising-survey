# Evaluation Protocols

This document specifies the evaluation protocols used to generate the benchmark tables in the survey. It is intended to make the reported results reproducible and cross-comparable.

## 1. Noise parameterisation

A single affine variance profile is used throughout:

```
Var(y) = α x + σ²,    y = α p + n,   p ~ Poisson(x/α),   n ~ N(0, σ²)
```

- `α` — signal-dependent variance slope (conversion factor from counts to intensity units).
- `σ²` — additive read-noise variance.

Synthetic PG evaluation must report `(α, σ²)` explicitly and use this convention. Papers that parameterise the Poisson mean differently (e.g. `Poisson(α x)`) must be converted before comparison, otherwise the same `α` denotes different physical quantities.

## 2. Metrics

### Standard fidelity metrics

| Metric | Definition | Notes |
|---|---|---|
| PSNR | `10 log10(MAX² / MSE)` | Default for benchmark comparability |
| SSIM | Structural similarity index | Complement to PSNR |

### Perceptual and uncertainty-aware metrics

| Metric | Purpose |
|---|---|
| LPIPS | Learned perceptual similarity |
| PG-URE | Poisson–Gaussian unbiased risk estimate, for blind/no-reference evaluation |
| Spatially weighted PSNR | Accounts for heteroscedastic noise (weight by local variance) |
| Coverage / calibration | Uncertainty-aware criteria (e.g. posterior band coverage) |

The survey argues (Section on evaluation) that pixel-level PSNR/SSIM under-represent dark-region failures because bright regions dominate the MSE. Task-aware and uncertainty-aware endpoints are recommended for applied pipelines.

## 3. Benchmark table provenance

Every entry in the benchmark tables carries provenance metadata:

- **Source** — the publication or release from which the value is taken.
- **Split** — which test split was used (e.g. BSD68, FMD mixed test set).
- **Noise** — the `(α, σ²)` or noise level used.
- **Training protocol** — for learned methods, the training data and schedule.

All benchmark tables in the survey are explicitly labelled as **literature-reported values**, not as re-runs, precisely because published tables frequently mix values reproduced under differing conditions.

## 4. Classical-method protocol (this repository)

The bundled `methods/` (VST-BM3D, VST-NLM, VST-KSVD, VST-EPLL, VST-WNNM, PURE-LET) follow the stabilise-then-denoise pipeline:

1. Apply the generalised Anscombe transform (forward) to the noisy image `y`.
2. Denoise with the base method (BM3D, NLM, K-SVD, EPLL, WNNM, or the PURE-LET linear expansion).
3. Apply the exact unbiased inverse Anscombe transform.

Noise parameters `(α, σ²)` are estimated from the noisy image using `utils/estimate_noise.m` unless ground-truth values are provided.

## 5. Reproducing the tables

```bash
python scripts/generate_benchmark_tables.py
```

Outputs are written to `scripts/output/` in CSV and Markdown.
