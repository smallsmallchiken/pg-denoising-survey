# Poisson–Gaussian Image Denoising: A Unified Survey — Official Companion Repository

> Official implementation, benchmark suite, and evaluation protocols for the paper
> **"Poisson–Gaussian Image Denoising: A Unified Survey from Statistical Inference to Deep Learning Benchmarks"**
> *Submitted to* **The Visual Computer**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24468008.svg)](https://doi.org/10.5281/zenodo.24468008)

This repository accompanies the survey and provides (i) reference implementations of the classical Poisson–Gaussian (PG) denoising methods reviewed in the paper, (ii) the benchmark table-generation scripts and evaluation protocols, (iii) the two-axis taxonomy figure, and (iv) curated dataset links.

If you use the code, data, benchmark protocol, or any figure provided here, please cite the associated paper.

---

## Overview

Poisson–Gaussian (PG) noise is a central challenge in low-photon and sensor-limited imaging, where signal-dependent photon (shot) noise is coupled with signal-independent electronic noise. This survey provides a unified review of PG image denoising from the perspective of statistical inference and modern deep learning, organising methods by their estimation objective (variance-stabilizing transforms, MAP/MMSE estimation, unbiased risk minimization, plug-and-play priors, self-supervised learning, and diffusion-based posterior sampling).

This repository contains the reference implementations and reproducible evaluation tooling that support the survey. It is designed to let readers reproduce the classical-method results and to provide the protocols and scripts needed to generate the benchmark tables reported in the manuscript.

---

## Repository Structure

```text
├── figures/                    # Two-axis taxonomy of the surveyed methods
│   └── taxonomy.pdf            #   (estimation objective × supervision regime, by year)
├── methods/                    # Classical denoising method implementations (MATLAB)
│   ├── VST_BM3D/               #   Stabilised-Anscombe + BM3D
│   ├── VST_NLM/                #   Stabilised-Anscombe + Non-local means
│   ├── VST_KSVD/               #   Stabilised-Anscombe + K-SVD
│   ├── VST_KSVDD/              #   Stabilised-Anscombe + K-SVD (dictionary variant)
│   ├── VST_KSVDG/              #   Stabilised-Anscombe + K-SVD (group variant)
│   ├── VST_EPLL/               #   Stabilised-Anscombe + EPLL
│   ├── VST_WNNM/               #   Stabilised-Anscombe + WNNM
│   └── PURE_LET/               #   Poisson unbiased risk estimate + linear expansion of thresholds
├── benchmarks/                 # Per-method benchmark driver scripts
├── utils/                      # Shared utilities (Anscombe transforms, noise estimation)
├── examples/                   # End-to-end demos
├── scripts/                    # Benchmark table-generation scripts
├── docs/
│   ├── datasets.md             # Dataset download links and licenses
│   └── protocols.md            # Evaluation protocols and noise parameterisation
├── BSD100/  BSD500/  BSD68/    # Grayscale reference image sets (test data)
├── Set12/                      # Classic 12-image set
├── FMD/README.md               # FMD dataset download link (data not hosted)
├── LICENSE
└── README.md
```

> **Note.** The original data-heavy `FDM/` directory is **not** tracked in this repository. Fluorescence Microscopy Denoising (FMD) data must be downloaded from the official source; see `docs/datasets.md`.

---

## Noise Model

The survey uses the affine variance parameterisation of Foi et al. (2008) and of the FMD release, written as

```
y_i = α p_i + n_i,   p_i ~ Poisson(x_i / α),   n_i ~ N(0, σ²),
```

which yields the affine variance profile `Var(y_i) = α x_i + σ²`. Here `α` is the signal-dependent variance slope and `σ²` the additive read-noise variance; both can be read directly off the variance–mean relation. Throughout the repository, `(α, σ²)` follow this convention.

---

## Installation

### Prerequisites

- MATLAB R2016b+ (for the classical methods)
- Python 3.8+ (for the benchmark table-generation scripts)

### Setup

```bash
git clone https://github.com/smallsmallchiken/pg-denoising-survey.git
cd pg-denoising-survey
```

For the classical MATLAB methods:

```matlab
addpath(genpath('methods'));
addpath(genpath('utils'));
addpath(genpath('benchmarks'));
```

---

## Quick Start

### MATLAB — run a classical method on an image

```matlab
addpath(genpath('utils')); addpath(genpath('methods'));

img_raw = im2double(imread('examples/noisy_image.tif'));

% Estimate Poisson–Gaussian noise parameters (α, σ²) from the noisy image
[alpha, sigma2] = estimate_noise(img_raw);

% Denoise with stabilised-Anscombe + BM3D
img_denoised = denoise_VST_BM3D(img_raw, alpha, sigma2);

figure; subplot(1,2,1); imshow(img_raw, []); title('Noisy');
       subplot(1,2,2); imshow(img_denoised, []); title('Denoised');
```

### MATLAB — run the full classical benchmark

```matlab
addpath(genpath('benchmarks')); addpath(genpath('methods')); addpath(genpath('utils'));
run_benchmark;   % runs the VST-family methods on BSD68 / Set12 with synthetic PG noise
```

---

## Benchmark Tables

The benchmark tables in the paper report **literature-reported values** with explicit per-entry provenance (source, dataset split, noise setting, training protocol). To regenerate the tables from the bundled data and scripts:

```bash
python scripts/generate_benchmark_tables.py
```

The generated tables are written to `scripts/output/` as CSV/Markdown. See `docs/protocols.md` for the exact noise parameterisations and metric definitions used.

---

## Evaluation Protocols

The survey highlights four benchmarking gaps that this repository is designed to address:

1. **Provenance** — every benchmark entry should carry its source, split, noise setting, and training protocol. All tables in the paper are labelled as literature-reported values for this reason.
2. **Protocol harmonisation** — synthetic PG evaluation must use a single `(α, σ²)` parameterisation (the affine variance profile above) so that cross-paper comparisons are meaningful.
3. **Task-aware endpoints** — pixel-level PSNR/SSIM are complemented by perceptual and uncertainty-aware criteria (see `docs/protocols.md`).
4. **Real-sensor generalisation** — real-noise test sets (FMD, RENOIR, SIDD) are treated as device-specific, not as universal ground truth.

Full details are in `docs/protocols.md`.

---

## Datasets

The grayscale reference sets bundled here (`BSD68`, `BSD100`, `BSD500`, `Set12`) are standard test images used by the classical methods. Larger real-noise benchmarks are **linked, not hosted**:

| Dataset | Domain | Source |
|---|---|---|
| FMD | Fluorescence microscopy | https://github.com/yinhaoz/denoising-fluorescence |
| SIDD | Smartphone photography | https://www.eecs.yorku.ca/~kamel/sidd/ |
| RENOIR | Real low-light photography | http://ani.stat.fsu.edu/~abarbu/Renoir.html |

See `docs/datasets.md` for full download instructions and licenses.

---

## Citation

If you use this repository, benchmark, or associated methods, please cite the paper and repository as follows.

### Paper

```bibtex
@article{peng2025poisson,
  title={Poisson--Gaussian Image Denoising: A Unified Survey from Statistical Inference to Deep Learning Benchmarks},
  author={Peng, Pai and Ma, Chongya and Chen, Hechan and Li, Chenglong and Xiaokaiti, Aizimaiti},
  journal={The Visual Computer},
  year={2025},
  publisher={Springer},
  note={submitted}
}
```

### Repository

```bibtex
@misc{peng2025pg_survey_repo,
  title={Poisson--Gaussian Image Denoising: A Unified Survey — Companion Repository},
  author={Peng, Pai and Ma, Chongya and Chen, Hechan and Li, Chenglong and Xiaokaiti, Aizimaiti},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.24468008},
  howpublished={\url{https://github.com/smallsmallchiken/pg-denoising-survey}}
}
```

---

## License

This project is released under the **MIT License**. See the `LICENSE` file for details.

---

## Acknowledgments

This work was supported by the Finance Science and Technology Project of Xinjiang Uygur Autonomous Region (**2023B01029-1**, **2023B01029-2**).

We thank the authors and maintainers of the datasets and methods referenced in this benchmark, including FMD, SIDD, RENOIR, and the broader computational imaging and image restoration community.

---

## Contact

- **Corresponding Author**: Aizimaiti Xiaokaiti
- **Email**: azmtxkt@xju.edu.cn
- **Issues**: Please use GitHub Issues for bug reports and implementation questions.
