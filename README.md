
# Project Overview

This directory contains code for the cryopreservation project.

## File descriptions

- **sine_transform_test.ibynb** This file executes the sine tranform using only odd harmonics on both a test data set and on real experimental data.  Seems to work 
- **capacitor_time_domain.ipynb**  
  This file tests whether the time-domain signal from a capacitor can be reverse-transformed to recover the original complex impedance. In particular, it explores whether only the real part is needed.

- **C2.ipynb**  
  Solves the capacitor voltage divider equation in the presence of oscilloscope impedance and capacitance. Includes a markdown derivation for solving \( C \) and compares it with measured data from `Capacitance2.csv`. The fit suggests a capacitance around 25 pF.

- **capacitor_model_sine_wave.ipynb**
  This is an analysis of the frequency response for our capacitor when stimulated with a sine wave from the frequency generator and fit with the oscilloscope.  There are markdown sections which give the derivations.  Rather than trying to solve for C, this uses C as a fitting parameter and fits the shape of the curve.  We get good agreement with the fit for the empty capacitor cell which gives a capacitance of 38 pF using fixed probe capacitance of 8 pF and 10 M Ohm (from the probe itself, not varied).  This analysis supports the observation that there is an issue with the Pasco 550 impedence

- **Capacitor_analysis_2.ipynb**

- **documented_fit_to_capacitance.ipynb**

- **Leakage_resistance.ipynb**  
  Calculates the leakage resistance through water for the capacitor geometry.

- **example_jupyter_notebook_samaneh.ipynb**

- **capacitor_calculations_sucrose_solution_measurements.ipynb**

- **fit_capacitor_values.ipynb**

- **capacitor_fit_Friday_March_21.ipynb**

- **kyle_wang_data_march_31_2025.ipynb**

- **capacitor_model.ipynb**

- **read_capstone.ipynb**

- **capacitor_model_sine_wave - Copy.ipynb**

- **samanah_gantt_chart.ipynb**

- **samaneh_data.ipynb**

- **capacitor_model_sine_wave_with_scope_impedence.ipynb**

- **time_inversion_test.ipynb**  
  File to test the time inversion back to frequency space using a Debye function. Attempts to define a realistic version of the complex dielectric constant but didn't go all the way. Later supplemented by `capacitor_time_domain.ipynb`.

- **capacitor_model_sine_wave_with_scope_impedence_2.ipynb**

## Todo items

- Make a separate directory for data files and figures
- Make a separate directory for documentation
- Delete unneeded files

## Instructions

- `git add .`
- `git commit -m "Initial commit with notebooks and supporting scripts"`
- `git commit -m "Summarize main change" -m "Added dielectric recovery and signal prep"`
- `git config --global core.editor "vim"`
- `git config --global user.email "llurio@niu.edu"`
- `git config --global user.name "Larry Lurio"`

- *(To see recent changes)*: `git log`  
- *(To just see what changed)*: `git show --stat`
- *(To update to githup)*: `git push`
