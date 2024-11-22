#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import modules
from pathlib import Path
import numpy as np


# Define data load function
def load_data(fname):
    # Construct file path
    data_dir = Path.home() / "miniature-happiness" / "data" / "NIFS" / fname
    # Specify columns to read
    usecols = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14]
    # Define data types for each column
    dtype = [
        ("Line", "i4"),
        ("Station", "i4"),
        ("Date", "datetime64[D]"),
        ("Latitude", "f4"),
        ("Longitude", "f4"),
        ("Depth", "i4"),
        ("Water_Temperature", "f4"),
        ("T_QC", "i4"),
        ("Salinity", "f4"),
        ("S_QC", "i4"),
        ("DO", "f4"),
        ("D_QC", "i4"),
        ("QC_LEVEL", "i4"),
    ]
    # Load data
    data = np.genfromtxt(
        data_dir, usecols=usecols, dtype=dtype, delimiter="\t", skip_header=1
    )
    return data


# Define main function
def main():
    accumulated_data = None  # Use None initially
    periods = np.arange(1968, 2024, 1)  # from 1968 to 2023

    for period in periods:
        fname = f"NIFS_Data_{period}.txt"
        data = load_data(fname)

        # Check if accumulated_data is None, set it to the first data array
        if accumulated_data is None:
            accumulated_data = data
        else:
            # Concatenate the new data along the first axis
            accumulated_data = np.concatenate((accumulated_data, data), axis=0)

    # Create the save path
    save_path = (
        Path.home()
        / "miniature-happiness"
        / "data"
        / "processed"
        / "accumulated_data.npy"
    )
    # Save the accumulated data
    np.save(save_path, accumulated_data)


if __name__ == "__main__":
    main()
