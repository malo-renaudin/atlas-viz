# Atlas Visualization

## Description

This project demonstrates the basics of using Streamlit with Docker. Streamlit is an open-source app framework for Machine Learning and Data Science teams. Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.

## Installation

### Prerequisites
 
 -   P y t h o n   3 . 7   o r   h i g h e r 
 
 -   D o c k e r 
 
 -   S t r e a m l i t 
 
 -   Matplotlib
 
 -   N u m P y   

- Nilearn
 
 
 
### Steps
 
 1 .   C l o n e   t h e   r e p o s i t o r y : 
 
         ` ` ` s h 
 
         g i t   c l o n e  https://github.com/malo-renaudin/atlas-viz
 
         c d   atlas-viz
 
         ` ` ` 
 
 
 
 
 
## Usage
 
 
### Running Streamlit App locally

 
 1 .   N a v i g a t e   t o   t h e   p r o j e c t   d i r e c t o r y : 
 
         ` ` ` s h 
 
         c d   atlas-viz
 
         ` ` ` 
 
 
 
 2 .   R u n   t h e   S t r e a m l i t   H e l l o : 
 
         ` ` ` 
 
         s t r e a m l i t   r u n   atlas_app.py
 
         ` ` ` 
 
### Running Streamlit App with Docker

 
 1 .   B u i l d   t h e   D o c k e r   i m a g e : 
 
         ` ` ` 
 
         d o c k e r   b u i l d   - t   atlas_viz   . 
 
         ` ` ` 
 
 
 
 2 .   R u n   t h e   D o c k e r   c o n t a i n e r : 
 
         ` ` ` s h 
 
         d o c k e r   r u n   - p   8 5 0 1 : 8 5 0 1   s t r e a m l i t - a p p 
 
         ` ` ` 
 
 
 
 3 .   O p e n   y o u r   b r o w s e r   a n d   g o   t o   ` h t t p : / / l o c a l h o s t : 8 5 0 1 `   t o   s e e   t h e   a p p . 
 
 
 
 4 .   I f   n e e d   b e   y o u   c a n   f i n d   t h e   d o c k e r   i m a g e   h e r e   `  https://hub.docker.com/repository/docker/malorenaudin/atlas-viz/general'
 
 
