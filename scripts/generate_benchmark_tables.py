#!/usr/bin/env python3
"""Benchmark table-generation scripts for the PG denoising survey.

Regenerates the literature-reported benchmark tables that appear in the paper.
All values are literature-reported (from the FMD dataset release and the cited
self-supervised denoising surveys); no re-run is performed here.

Output: Markdown + CSV files under scripts/output/.
"""
import csv
import os

OUT = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT, exist_ok=True)


def write_md_and_csv(name, header, rows, provenance):
    """Write a table as Markdown and CSV."""
    md_path = os.path.join(OUT, name + ".md")
    csv_path = os.path.join(OUT, name + ".csv")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {name}\n\n")
        f.write(f"> {provenance}\n\n")
        f.write("| " + " | ".join(header) + " |\n")
        f.write("|" + "---|" * len(header) + "\n")
        for r in rows:
            f.write("| " + " | ".join(str(c) for c in r) + " |\n")

    print(f"wrote {md_path} and {csv_path}")


# ---------------------------------------------------------------------------
# Table: FMD mixed-test-set benchmark (literature-reported, Zhang et al. 2019)
# ---------------------------------------------------------------------------
fmd_header = [
    "Method", "1 frame", "2 frames", "4 frames", "8 frames",
    "16 frames", "Time",
]
fmd_rows = [
    ["Raw", "27.22 / 0.5442", "30.08 / 0.6800", "32.86 / 0.7981",
     "36.03 / 0.8892", "39.70 / 0.9487", "--"],
    ["VST+NLM", "31.25 / 0.7503", "32.85 / 0.8116", "34.92 / 0.8763",
     "37.09 / 0.9208", "40.04 / 0.9540", "137.10 s"],
    ["VST+BM3D", "32.71 / 0.7922", "34.09 / 0.8430", "36.05 / 0.8970",
     "38.01 / 0.9336", "40.61 / 0.9598", "5.67 s"],
    ["VST+KSVD", "32.02 / 0.7746", "33.69 / 0.8327", "35.84 / 0.8933",
     "37.79 / 0.9314", "40.36 / 0.9585", "341.21 s"],
    ["VST+KSVD(D)", "31.77 / 0.7712", "33.45 / 0.8292", "35.67 / 0.8908",
     "37.69 / 0.9300", "40.32 / 0.9579", "67.96 s"],
    ["VST+KSVD(G)", "31.98 / 0.7752", "33.64 / 0.8327", "35.83 / 0.8930",
     "37.82 / 0.9312", "40.44 / 0.9584", "58.82 s"],
    ["VST+EPLL", "32.61 / 0.7876", "34.07 / 0.8414", "36.08 / 0.8970",
     "38.12 / 0.9349", "40.83 / 0.9618", "288.63 s"],
    ["VST+WNNM", "32.52 / 0.7880", "34.04 / 0.8419", "36.04 / 0.8973",
     "37.95 / 0.9334", "40.45 / 0.9587", "451.89 s"],
    ["PURE-LET", "31.95 / 0.7664", "33.49 / 0.8270", "35.29 / 0.8814",
     "37.25 / 0.9212", "39.59 / 0.9450", "2.61 s"],
    ["DnCNN", "34.88 / 0.9063", "36.02 / 0.9257", "37.57 / 0.9460",
     "39.28 / 0.9588", "41.57 / 0.9721", "3.07 s (GPU)"],
    ["Noise2Noise", "35.40 / 0.9187", "36.40 / 0.9230", "37.59 / 0.9481",
     "39.43 / 0.9601", "41.45 / 0.9724", "2.94 s (GPU)"],
]
write_md_and_csv(
    "fmd_benchmark", fmd_header, fmd_rows,
    "Literature-reported values from the FMD dataset release (Zhang et al., "
    "CVPR 2019), FMD mixed test set. PSNR (dB) / SSIM per number of averaged "
    "raw frames; the last column lists single-image inference time.",
)

# ---------------------------------------------------------------------------
# Table: Average PG parameters (a, b) of FMD per modality (Zhang et al. 2019)
# ---------------------------------------------------------------------------
fmd_noise_header = ["Modality", "Slope a", "Intercept b"]
# NOTE: values below are representative of the ranges reported in the FMD
# release; fill in the exact per-configuration values from the paper table
# (tab:fmd-noise) before finalising.
fmd_noise_rows = [
    ["Confocal", "~1e-2", "small negative"],
    ["Two-photon", "larger", "larger negative"],
    ["Wide-field", "~1e-3", "comparable"],
]
write_md_and_csv(
    "fmd_noise_parameters", fmd_noise_header, fmd_noise_rows,
    "Average Poisson-Gaussian parameters (a, b) of the FMD dataset as reported "
    "in its release. In the survey notation, a corresponds to alpha and b to "
    "sigma^2. Negative b values are a known artefact of fitting the affine "
    "model to clipped raw data (Foi et al. 2008).",
)

print("done")
