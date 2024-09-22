��#  Atlas visualization
 
 
 
 # #   D e s c r i p t i o n 
 
 T h i s   p r o j e c t   d e m o n s t r a t e s   t h e   b a s i c s   o f   u s i n g   S t r e a m l i t   w i t h   D o c k e r .   S t r e a m l i t   i s   a n   o p e n - s o u r c e   a p p   f r a m e w o r k   f o r   M a c h i n e   L e a r n i n g   a n d   D a t a   S c i e n c e   t e a m s .   D o c k e r   i s   a   s e t   o f   p l a t f o r m - a s - a - s e r v i c e   p r o d u c t s   t h a t   u s e   O S - l e v e l   v i r t u a l i z a t i o n   t o   d e l i v e r   s o f t w a r e   i n   p a c k a g e s   c a l l e d   c o n t a i n e r s . 
 
 
 
 # #   I n s t a l l a t i o n 
 
 
 
 # # #   P r e r e q u i s i t e s 
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
 # # #   S t e p s 
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
 # #   U s a g e 
 
 
 
 # # #   R u n n i n g   S t r e a m l i t   A p p   L o c a l l y 
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
         ` ` ` s h 
 
         s t r e a m l i t   r u n   atlas_app.py
 
         ` ` ` 
 
 
 
 # # #   R u n n i n g   S t r e a m l i t   A p p   w i t h   D o c k e r 
 
 1 .   B u i l d   t h e   D o c k e r   i m a g e : 
 
         ` ` ` s h 
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
