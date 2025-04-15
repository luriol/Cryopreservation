
# Project Overview

This directory contains code for the cryopreservation project

## File descriptions


- C2.ipynb 
    This file solves the capacitor voltage divider equation in the presence of an oscilloscope impedence and capacitance.  It shows the derivation (in markdown) of the solution for C given the scope impedence and capacitance, the frequency and the amplitude and then compares it with measured data  reading from the Capacitance2.csv datafile.  Data agreement looks good and gives a capacitance value of around 25 pF.
- capacitor_time_domain.ipynb
    This file tries to test if the time domain signal from a capacitor can be reverse transformed to recover the original complex impedence. In particular, do you just need the real part? 
- Capacitor_analysis_2.ipynb
- documented_fit_to_capacitance.ipynb
Leakage_resistance.ipynb 
example_jupyter_notebook_samaneh.ipynb
capacitor_calculations_sucrose_solution_measurements.ipynb
fit_capacitor_values.ipynb
capacitor_fit_Friday_March_21.ipynb
kyle_wang_data_march_31_2025.ipynb
capacitor_model.ipynb
read_capstone.ipynb
'capacitor_model_sine_wave - Copy.ipynb'
samanah_gantt_chart.ipynb
capacitor_model_sine_wave.ipynb
samaneh_data.ipynb
capacitor_model_sine_wave_with_scope_impedence.ipynb
- time_inversion_test.ipynb
    File to test the time inversion back to frequency space using a debye function.  This function tried to define a realisti
    verion of the complex dielectric constant but didn't go all the way. Was supplemented by capacitor_time_domain
capacitor_model_sine_wave_with_scope_impedence_2.ipynb

## Instructions
git add .
git commit -m "Initial commit with notebooks and supporting scripts"
git config --global core.editor "vim"
config --global user.email "llurio@niu.edu"
config --global user.name "Larry Lurio"

To see recent changes:      git log
To just see what chaged:    git show --stat
