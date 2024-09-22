import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import nilearn.plotting as plotting
from nilearn import datasets

# Set Matplotlib backend
import matplotlib
matplotlib.use('Agg')

# Title of the app
st.title("Brain Atlas Visualization")

# Fetch available atlases from Nilearn
atlases = {
    "Harvard-Oxford": datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm'),
    "AAL": datasets.fetch_atlas_aal(),
    "Schaeffer 400": datasets.fetch_atlas_schaefer_2018()
}

# Dropdown for atlas selection
selected_atlas = st.selectbox("Select Atlas", list(atlases.keys()))

try:
    # Fetch the selected atlas
    atlas_data = atlases[selected_atlas]

    # Visualization
    st.write(f"Visualizing: {selected_atlas}")
    fig, ax = plt.subplots()
    
    # Adjust this line based on the structure of your atlas data
    map_data = atlas_data.maps if hasattr(atlas_data, 'maps') else atlas_data['maps']
    
    display = plotting.plot_roi(map_data, title=selected_atlas, display_mode='ortho', cut_coords=(0, 0, 0), draw_cross=False, axes=ax)
    st.pyplot(fig)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Optionally, allow users to close the visualization
if st.button("Close Visualization"):
    plt.close('all')
    st.empty()
