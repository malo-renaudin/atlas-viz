# Atlas Visualization

## Description

This project demonstrates the basics of using Streamlit with Docker. Streamlit is an open-source app framework for Machine Learning and Data Science teams. Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.

## Installation

### Prerequisites

- Python 3.7 or higher
- Docker
- Streamlit
- Matplotlib
- NumPy
- Nilearn

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/malo-renaudin/atlas-viz
   cd atlas-viz
   ```

## Usage

### Running Streamlit App locally

1. Navigate the project directory :
    ```sh
    cd atlas-viz
    ```
2. Rune the Streamlit atlas_app file : 
    ```sh
    streamlit run atlas_app.py
    ```


### Running Streamlit App with Docker

1. Build the Docker image :
    ```sh
    docker build -t atlas_viz
    ````
2. Run the Docker container : 
    ```sh
    docker run -p 8501:8501 streamlit-app
    ````
3. Open browser and go to 'https://localhost:8501' to see the app

4. If need be you can find the docker image here'https://hub.docker.com/repository/docker/malorenaudin/atlas-viz/general'

