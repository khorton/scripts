FasdUAS 1.101.10   ��   ��    k             l     ��  ��    ] W This applescript will set the exif keywords, name, and comments of all selected iPhoto     � 	 	 �   T h i s   a p p l e s c r i p t   w i l l   s e t   t h e   e x i f   k e y w o r d s ,   n a m e ,   a n d   c o m m e n t s   o f   a l l   s e l e c t e d   i P h o t o   
  
 l     ��  ��    8 2   images using the information current in iPhoto.     �   d       i m a g e s   u s i n g   t h e   i n f o r m a t i o n   c u r r e n t   i n   i P h o t o .      l     ��������  ��  ��        l     ��  ��    8 2 Author: Andrew Turner (http://highearthorbit.com)     �   d   A u t h o r :   A n d r e w   T u r n e r   ( h t t p : / / h i g h e a r t h o r b i t . c o m )      l     ��  ��           �           j     �� �� 0 	copyright    m        �   d C o p y r i g h t   K e v i n   H o r t o n ,   2 0 1 2 .   A l l   R i g h t s   R e s e r v e d .     !   j    �� "
�� 
url  " m     # # � $ $ 8 h t t p : / / w w w . k i l o h o t e l . c o m / r v 8 !  % & % j    �� '�� $0 exiftooloriginal exifToolOriginal ' m     ( ( � ) )  _ o r i g i n a l &  * + * l     ��������  ��  ��   +  , - , l     �� . /��   . 8 2 True retains copyright, False means Public Domain    / � 0 0 d   T r u e   r e t a i n s   c o p y r i g h t ,   F a l s e   m e a n s   P u b l i c   D o m a i n -  1 2 1 j   	 �� 3�� 0 copyrighted Copyrighted 3 m   	 
 4 4 � 5 5  T r u e 2  6 7 6 l     ��������  ��  ��   7  8 9 8 l     ��������  ��  ��   9  : ; : l   M <���� < O    M = > = k   L ? ?  @ A @ I   	������
�� .miscactvnull��� ��� null��  ��   A  B�� B Q   
L C D E C k   % F F  G H G s     I J I l    K���� K n    L M L I    �������� 0 selected_images  ��  ��   M  f    ��  ��   J o      ���� 0 these_images   H  N O N Z   0 P Q���� P G    % R S R =    T U T o    ���� 0 these_images   U m    ��
�� boovfals S =   # V W V l   ! X���� X l   ! Y���� Y I   !�� Z��
�� .corecnte****       **** Z o    ���� 0 these_images  ��  ��  ��  ��  ��   W m   ! "����   Q l 	 ( , [���� [ R   ( ,�� \��
�� .ascrerr ****      � **** \ m   * + ] ] � ^ ^ : P l e a s e   s e l e c t   a   s i n g l e   i m a g e .��  ��  ��  ��  ��   O  _ ` _ l  1 1��������  ��  ��   `  a b a Y   1 c�� d e�� c k   ? f f  g h g r   ? B i j i m   ? @ k k � l l   j l      m���� m o      ���� 0 keywordslist  ��  ��   h  n o n r   C I p q p n   C G r s r 4   D G�� t
�� 
cobj t o   E F���� 0 i   s o   C D���� 0 these_images   q o      ���� 0 
this_photo   o  u v u O   J z w x w k   N y y y  z { z r   N S | } | l  N Q ~���� ~ 1   N Q��
�� 
ipth��  ��   } l      ����  o      ���� 0 
image_file  ��  ��   {  � � � r   T Y � � � l  T W ����� � 1   T W��
�� 
titl��  ��   � l      ����� � o      ���� 0 image_title  ��  ��   �  � � � r   Z a � � � l  Z ] ����� � 1   Z ]��
�� 
filn��  ��   � l      ����� � o      ���� 0 image_filename  ��  ��   �  � � � r   b k � � � l  b g ����� � 1   b g��
�� 
pcom��  ��   � l      ����� � o      ���� 0 image_comment  ��  ��   �  ��� � r   l y � � � l  l u ����� � n   l u � � � 1   q u��
�� 
pnam � 2  l q��
�� 
ikwd��  ��   � l      ����� � o      ���� 0 assigned_keywords  ��  ��  ��   x o   J K���� 0 
this_photo   v  � � � Y   { � ��� � ��� � r   � � � � � b   � � � � � b   � � � � � o   � ����� 0 keywordslist   � m   � � � � � � �    - k e y w o r d s + = � n   � � � � � 4   � ��� �
�� 
cobj � o   � ����� 0 j   � o   � ����� 0 assigned_keywords   � l      ����� � o      ���� 0 keywordslist  ��  ��  �� 0 j   � m   ~ ����  � l   � ����� � I   ��� ���
�� .corecnte****       **** � o    ����� 0 assigned_keywords  ��  ��  ��  ��   �  � � � r   � � � � I  � �� ���
�� .sysoexecTEXT���     TEXT � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � l 	 � � ����� � m   � � � � � � � 2 / s w / b i n / e x i f t o o l   - t i t l e = '��  ��   � o   � ����� 0 image_title   � l 	 � � ����� � m   � � � � � � �  '  ��  ��   � o   � ����� 0 keywordslist   � l 	 � � ����� � m   � � � � � � �   ��  ��   � m   � � � � � � �    - c o m m e n t = ' � o   � ����� 0 image_comment   � l 	 � � ����� � m   � � � � � � �  '  ��  ��   � m   � � � � � � �    - C o p y r i g h t = ' � o   � ����� 0 	copyright   � l 	 � � ����� � m   � � � � � � �  '  ��  ��   � m   � � � � � � � &   - C o p y r i g h t N o t i c e = ' � o   � ����� 0 	copyright   � l 	 � � ���� � m   � � � � � � �  '  ��  �   � m   � � � � � � �    - R i g h t s = ' � o   � ��~�~ 0 	copyright   � l 	 � � ��}�| � m   � � � � � � �  '  �}  �|   � m   � � � � � � �    - M a r k e d = ' � o   � ��{�{ 0 copyrighted Copyrighted � l 	 � � ��z�y � m   � � � � � � �  '  �z  �y   � m   � � � � �    ' � o   � ��x�x 0 
image_file   � m   � � �  '��   � o      �w�w 
0 output   � �v I �u�t
�u .sysoexecTEXT���     TEXT b   b   b  
	
	 m   �  r m   '
 o  	�s�s 0 
image_file   m  
 �  ' o  �r�r $0 exiftooloriginal exifToolOriginal�t  �v  �� 0 i   d m   4 5�q�q  e l  5 :�p�o I  5 :�n�m
�n .corecnte****       **** o   5 6�l�l 0 these_images  �m  �p  �o  ��   b  l �k�j�i�k  �j  �i   �h I %�g�f
�g .sysodlogaskr        TEXT m  ! � , E x i f   w r i t i n g   c o m p l e t e .�f  �h   D R      �e
�e .ascrerr ****      � **** o      �d�d 0 error_message   �c�b
�c 
errn o      �a�a 0 error_number  �b   E Z  -L�`�_ > -2 l -.�^�] o  -.�\�\ 0 error_number  �^  �]   m  .1�[�[�� I 5H�Z 
�Z .sysodlogaskr        TEXT o  56�Y�Y 0 error_message    �X!"
�X 
btns! J  9>## $�W$ m  9<%% �&&  C a n c e l�W  " �V'�U
�V 
dflt' m  AB�T�T �U  �`  �_  ��   > m     ((�                                                                                  iPho  alis    N  Macintosh HD               �VUFH+  ��{
iPhoto.app                                                      �a�� �        ����  	                Applications    �V��      ��9    ��{  %Macintosh HD:Applications: iPhoto.app    
 i P h o t o . a p p    M a c i n t o s h   H D  Applications/iPhoto.app   / ��  ��  ��   ; )*) l     �S�R�Q�S  �R  �Q  * +,+ l     �P�O�N�P  �O  �N  , -�M- i    ./. I      �L�K�J�L 0 selected_images  �K  �J  / O     .010 Q    -2342 k    #55 676 l   �I89�I  8   get selection   9 �::    g e t   s e l e c t i o n7 ;<; r    =>= l   
?�H�G? 1    
�F
�F 
selc�H  �G  > o      �E�E 0 these_items  < @A@ l   �DBC�D  B &   check for single album selected   C �DD @   c h e c k   f o r   s i n g l e   a l b u m   s e l e c t e dA EFE Z    GH�C�BG =   IJI l   K�A�@K n    LML 1    �?
�? 
pclsM n    NON 4    �>P
�> 
cobjP m    �=�= O o    �<�< 0 these_items  �A  �@  J m    �;
�; 
ipalH R    �:�9�8
�: .ascrerr ****      � ****�9  �8  �C  �B  F QRQ l  ! !�7ST�7  S ) # return the list of selected photos   T �UU F   r e t u r n   t h e   l i s t   o f   s e l e c t e d   p h o t o sR V�6V L   ! #WW o   ! "�5�5 0 these_items  �6  3 R      �4�3�2
�4 .ascrerr ****      � ****�3  �2  4 L   + -XX m   + ,�1
�1 boovfals1 m     YY�                                                                                  iPho  alis    N  Macintosh HD               �VUFH+  ��{
iPhoto.app                                                      �a�� �        ����  	                Applications    �V��      ��9    ��{  %Macintosh HD:Applications: iPhoto.app    
 i P h o t o . a p p    M a c i n t o s h   H D  Applications/iPhoto.app   / ��  �M       �0Z  # ( 4[\] k^_`abcd�/�.�-�,�+�*�)�(�'�0  Z �&�%�$�#�"�!� ������������������& 0 	copyright  
�% 
url �$ $0 exiftooloriginal exifToolOriginal�# 0 copyrighted Copyrighted�" 0 selected_images  
�! .aevtoappnull  �   � ****�  0 these_images  � 0 keywordslist  � 0 
this_photo  � 0 
image_file  � 0 image_title  � 0 image_filename  � 0 image_comment  � 0 assigned_keywords  � 
0 output  �  �  �  �  �  �  �  �  �  [ �/��ef�� 0 selected_images  �  �  e �
�
 0 these_items  f Y�	�����
�	 
selc
� 
cobj
� 
pcls
� 
ipal�  �  � /� + !*�,E�O��k/�,�  	)jhY hO�W 	X  fU\ �g��hi� 
� .aevtoappnull  �   � ****g k    Mjj  :����  �  �  h ���������� 0 i  �� 0 j  �� 0 error_message  �� 0 error_number  i 3(���������� ] k���������������������������� � � � � � � � � � � � � � � ���������k����%����
�� .miscactvnull��� ��� null�� 0 selected_images  �� 0 these_images  
�� .corecnte****       ****
�� 
bool�� 0 keywordslist  
�� 
cobj�� 0 
this_photo  
�� 
ipth�� 0 
image_file  
�� 
titl�� 0 image_title  
�� 
filn�� 0 image_filename  
�� 
pcom�� 0 image_comment  
�� 
ikwd
�� 
pnam�� 0 assigned_keywords  
�� .sysoexecTEXT���     TEXT�� 
0 output  
�� .sysodlogaskr        TEXT�� 0 error_message  k ������
�� 
errn�� 0 error_number  ��  ����
�� 
btns
�� 
dflt�� � N�J*j O)j+ EQ�O�f 
 �j j �& 	)j�Y hO �k�j kh  �E�O��/E�O� -*�,E�O*�,E�O*�,E` O*a ,E` O*a -a ,E` UO "k_ j kh �a %_ �/%E�[OY��Oa �%a %�%a %a %_ %a %a %b   %a %a %b   %a %a  %b   %a !%a "%b  %a #%a $%�%a %%j &E` 'Oa (�%a )%b  %j &[OY�!Oa *j +W &X , -�a . �a /a 0kva 1ka 2 +Y hU] ��l�� l  ^^ mm Y��n��
�� 
ipmrn A� �  
�� kfrmID  _ �oo � / U s e r s / k w h / P i c t u r e s / i P h o t o   L i b r a r y / M a s t e r s / 2 0 1 2 / 0 6 / 0 9 / 2 0 1 2 0 6 0 9 - 1 5 1 7 4 7 / I M G _ 1 3 2 2 . J P G` �pp  I M G _ 1 3 2 2a �qq  I M G _ 1 3 2 2 . J P Gb �rr  c ��s��  s   d �tt 2         1   i m a g e   f i l e s   u p d a t e d�/  �.  �-  �,  �+  �*  �)  �(  �'   ascr  ��ޭ