# Datasets

This document lists the datasets referenced by the survey, with download instructions and licenses. The repository intentionally **links** to large real-noise datasets rather than hosting them.

## Bundled reference image sets

The following grayscale reference sets are bundled under the repository root and are used as test data by the classical methods in `methods/`:

| Set | Images | Source |
|---|---|---|
| `BSD68` | 68 | Berkeley Segmentation Dataset (test split commonly used for denoising) |
| `BSD100` | 100 | Berkeley Segmentation Dataset (extended test split) |
| `BSD500` | 500 | Full Berkeley Segmentation Dataset |
| `Set12` | 12 | Classic 12-image set (Cameraman, Lena, Peppers, etc.) |

## Real-noise benchmarks (linked, not hosted)

### FMD — Fluorescence Microscopy Denoising

- **Description**: 12,000 real fluorescence microscopy images across confocal, two-photon, and wide-field modalities, with repeated exposures for ground-truth averaging and per-configuration Poisson–Gaussian parameter fits.
- **Download**: https://github.com/yinhaoz/denoising-fluorescence
- **Reference**: Zhang, Y. et al. *A Poisson–Gaussian Denoising Dataset with Real Fluorescence Microscopy Images*. CVPR 2019.

### SIDD — Smartphone Image Denoising Dataset

- **Description**: Real smartphone images with RAW/sRGB pairs, captured under varying lighting and ISO, with ground-truth mean images.
- **Download**: https://www.eecs.yorku.ca/~kamel/sidd/
- **Reference**: Abdelhamed, A. et al. *A High-Quality Denoising Dataset for Smartphone Cameras*. CVPR 2018.

### RENOIR — Real Low-Light Image Noise Reduction

- **Description**: Real low-light photographs with paired reference images captured with long exposure and controlled alignment.
- **Download**: http://ani.stat.fsu.edu/~abarbu/Renoir.html
- **Reference**: Anaya, J. & Barbu, A. *RENOIR — A Dataset for Real Low-Light Image Noise Reduction*. JVCIR 2018.

## Noise parameterisation

All `(α, σ²)` values in this repository follow the affine variance profile

```
Var(y) = α x + σ²,
```

with `y = α p + n`, `p ~ Poisson(x/α)`, `n ~ N(0, σ²)`. This matches the convention of Foi et al. (2008) and the FMD release, and is the same parameterisation used throughout the survey.
