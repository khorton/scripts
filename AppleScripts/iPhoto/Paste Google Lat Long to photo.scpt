FasdUAS 1.101.10   ��   ��    k             l   M ����  O    M  	  k   L 
 
     I   	������
�� .miscactvnull��� ��� null��  ��     ��  Q   
L     k   �       r        I   ������
�� .JonsgClp****    ��� null��  ��    o      ���� 0 clip_in        l   ��  ��    $ display dialog clip_in as text     �   < d i s p l a y   d i a l o g   c l i p _ i n   a s   t e x t      l   ��������  ��  ��        l   ��   ��    2 , Split clipboard into items with : delimiter      � ! ! X   S p l i t   c l i p b o a r d   i n t o   i t e m s   w i t h   :   d e l i m i t e r   " # " r     $ % $ J     & &  '�� ' m     ( ( � ) )  ,��   % n      * + * 1    ��
�� 
txdl + 1    ��
�� 
ascr #  , - , r    " . / . n      0 1 0 2    ��
�� 
citm 1 o    ���� 0 clip_in   / o      ���� 0 
clip_items   -  2 3 2 r   # * 4 5 4 l  # ( 6���� 6 I  # (�� 7��
�� .corecnte****       **** 7 o   # $���� 0 
clip_items  ��  ��  ��   5 o      ���� 0 	num_items   3  8 9 8 l  + +�� : ;��   : I Cdisplay dialog "There are " & num_items & " items in the clipboard"    ; � < < � d i s p l a y   d i a l o g   " T h e r e   a r e   "   &   n u m _ i t e m s   &   "   i t e m s   i n   t h e   c l i p b o a r d " 9  = > = Z   + N ? @ A�� ? A   + . B C B o   + ,���� 0 	num_items   C m   , -����  @ k   1 9 D D  E F E l  1 1�� G H��   G s mdisplay dialog "The clipboard does not have enough items" buttons {"OK"} with icon caution with title "ERROR"    H � I I � d i s p l a y   d i a l o g   " T h e   c l i p b o a r d   d o e s   n o t   h a v e   e n o u g h   i t e m s "   b u t t o n s   { " O K " }   w i t h   i c o n   c a u t i o n   w i t h   t i t l e   " E R R O R " F  J K J R   1 7�� L M
�� .ascrerr ****      � **** L m   5 6 N N � O O > C i p b o a r d   h a s   l e s s   t h a n   2   i t e m s . M �� P��
�� 
errn P m   3 4����#,��   K  Q�� Q l  8 8��������  ��  ��  ��   A  R S R ?  < ? T U T o   < =���� 0 	num_items   U m   = >����  S  V�� V k   B J W W  X Y X l  B B�� Z [��   Z k edisplay dialog "The clipboard has too many items" buttons {"OK"} with icon caution with title "ERROR"    [ � \ \ � d i s p l a y   d i a l o g   " T h e   c l i p b o a r d   h a s   t o o   m a n y   i t e m s "   b u t t o n s   { " O K " }   w i t h   i c o n   c a u t i o n   w i t h   t i t l e   " E R R O R " Y  ] ^ ] R   B H�� _ `
�� .ascrerr ****      � **** _ m   F G a a � b b > C i p b o a r d   h a s   m o r e   t h a n   2   i t e m s . ` �� c��
�� 
errn c m   D E����#-��   ^  d e d l  I I�� f g��   f 
 else    g � h h  e l s e e  i�� i l  I I�� j k��   j 3 -display dialog "Number of clipboard items OK"    k � l l Z d i s p l a y   d i a l o g   " N u m b e r   o f   c l i p b o a r d   i t e m s   O K "��  ��  ��   >  m n m r   O X o p o J   O T q q  r�� r m   O R s s � t t  ��   p n      u v u 1   U W��
�� 
txdl v 1   T U��
�� 
ascr n  w x w l  Y Y��������  ��  ��   x  y z y l  Y Y�� { |��   {   Parse clipboard items    | � } } ,   P a r s e   c l i p b o a r d   i t e m s z  ~  ~ r   Y g � � � c   Y c � � � n   Y _ � � � 4   Z _�� �
�� 
cobj � m   ] ^����  � o   Y Z���� 0 
clip_items   � m   _ b��
�� 
doub � o      ���� 0 lat     � � � l  h h�� � ���   � ( "display dialog "Latitude = " & lat    � � � � D d i s p l a y   d i a l o g   " L a t i t u d e   =   "   &   l a t �  � � � r   h v � � � c   h r � � � n   h n � � � 4   i n�� �
�� 
cobj � m   l m����  � o   h i���� 0 
clip_items   � m   n q��
�� 
doub � o      ���� 0 long   �  � � � l  w w�� � ���   � * $display dialog "Longitude = " & long    � � � � H d i s p l a y   d i a l o g   " L o n g i t u d e   =   "   &   l o n g �  � � � l  w w�� � ���   �  set alt to 0    � � � �  s e t   a l t   t o   0 �  � � � l  w w�� � ���   � ( "display dialog "Altitude = " & alt    � � � � D d i s p l a y   d i a l o g   " A l t i t u d e   =   "   &   a l t �  � � � l  w w��������  ��  ��   �  � � � l  w w�� � ���   �   confirm items in range    � � � � .   c o n f i r m   i t e m s   i n   r a n g e �  � � � Z   w � � ����� � l  w � ����� � G   w � � � � A   w ~ � � � o   w z���� 0 lat   � m   z }������ � ?   � � � � � o   � ����� 0 lat   � m   � ����� Z��  ��   � k   � � � �  � � � R   � ��� � �
�� .ascrerr ****      � **** � m   � � � � � � � * L a t i t u d e   o u t   o f   r a n g e � �� ���
�� 
errn � m   � �����#(��   �  � � � l  � ��� � ���   � 
 else    � � � �  e l s e �  ��� � l  � ��� � ���   � 1 +display dialog "Latitude in range:  " & lat    � � � � V d i s p l a y   d i a l o g   " L a t i t u d e   i n   r a n g e :     "   &   l a t��  ��  ��   �  � � � l  � ���������  ��  ��   �  � � � Z   � � � ����� � l  � � ����� � G   � � � � � A   � � � � � o   � ����� 0 long   � m   � ������L � ?   � � � � � o   � ����� 0 long   � m   � ����� ���  ��   � k   � � � �  � � � R   � ��� � �
�� .ascrerr ****      � **** � m   � � � � � � � , L o n g i t u d e   o u t   o f   r a n g e � �� ���
�� 
errn � m   � �����#)��   �  � � � l  � ��� � ���   � 
 else    � � � �  e l s e �  ��� � l  � ��� � ���   � 2 ,display dialog "Longitude in range: " & long    � � � � X d i s p l a y   d i a l o g   " L o n g i t u d e   i n   r a n g e :   "   &   l o n g��  ��  ��   �  � � � l  � ���������  ��  ��   �  � � � Q   � � � � � k   � � �  � � � r   �  � � � I  � ��� � �
�� .sysodlogaskr        TEXT � b   � � � � � b   � � � � � b   � � � � � m   � � � � � � � ` P a s t e   t h e   f o l l o w i n g   d a t a   i n t o   p h o t o ? 
 
 L a t i t u d e :   � o   � ����� 0 lat   � m   � � � � � � �  
 L o n g i t u d e :   � o   � ����� 0 long   � �� � �
�� 
appr � m   � � � � �    C o n f i r m   P a s t e � ��
�� 
btns J   � �  m   � � �  C a n c e l �� m   � �		 �

 
 P a s t e��   ��
�� 
dflt m   � � � 
 P a s t e ����
�� 
disp m   � ����� ��   � o      ���� 0 dialogresult dialogResult � �� l ��������  ��  ��  ��   � R      ��~
� .ascrerr ****      � ****�~   �}�|
�} 
errn d       m      �{�{ ��|   � k  
  l 

�z�z   - ' user pressed "Cancel" button, so abort    � N   u s e r   p r e s s e d   " C a n c e l "   b u t t o n ,   s o   a b o r t �y L  
�x�x  �y   �  l �w�v�u�w  �v  �u    s    l !�t�s! n "#" I  �r�q�p�r 0 selected_images  �q  �p  #  f  �t  �s    o      �o�o 0 these_images   $�n$ Z  �%&�m'% G  -()( = *+* o  �l�l 0 these_images  + m  �k
�k boovfals) =  ),-, l  '.�j�i. l  '/�h�g/ I  '�f0�e
�f .corecnte****       ****0 o   #�d�d 0 these_images  �e  �h  �g  �j  �i  - m  '(�c�c  & k  0:11 232 l 00�b45�b  4 M Gdisplay dialog "Please select a single image." buttons "OK" with icon 0   5 �66 � d i s p l a y   d i a l o g   " P l e a s e   s e l e c t   a   s i n g l e   i m a g e . "   b u t t o n s   " O K "   w i t h   i c o n   03 787 l 00�a9:�a  9 0 *display dialog the (count of these_images)   : �;; T d i s p l a y   d i a l o g   t h e   ( c o u n t   o f   t h e s e _ i m a g e s )8 <�`< R  0:�_=>
�_ .ascrerr ****      � ****= m  69?? �@@ B P l e a s e   s e l e c t   o n e   o r   m o r e   i m a g e s .> �^A�]
�^ 
errnA m  25�\�\#2�]  �`  �m  ' k  =�BB CDC l ==�[EF�[  E ) #display dialog "Selection accepted"   F �GG F d i s p l a y   d i a l o g   " S e l e c t i o n   a c c e p t e d "D HIH Y  ={J�ZKL�YJ k  MvMM NON l MM�XPQ�X  P   set the keywordslist to ""   Q �RR 4 s e t   t h e   k e y w o r d s l i s t   t o   " "O STS r  MYUVU n  MUWXW 4  PU�WY
�W 
cobjY o  ST�V�V 0 i  X o  MP�U�U 0 these_images  V o      �T�T 0 
this_photo  T Z�SZ O  Zv[\[ k  `u]] ^_^ r  `i`a` o  `c�R�R 0 lat  a l     b�Q�Pb 1  ch�O
�O 
lati�Q  �P  _ cdc r  jsefe o  jm�N�N 0 long  f l     g�M�Lg 1  mr�K
�K 
lngt�M  �L  d h�Jh l tt�Iij�I  i  set the altitude to alt   j �kk . s e t   t h e   a l t i t u d e   t o   a l t�J  \ o  Z]�H�H 0 
this_photo  �S  �Z 0 i  K m  @A�G�G L l AHl�F�El I AH�Dm�C
�D .corecnte****       ****m o  AD�B�B 0 these_images  �C  �F  �E  �Y  I non I |��Ap�@
�A .sysodlogaskr        TEXTp m  |qq �rr  D o n e�@  o sts l ���?uv�?  u E ?set image_path to image path of item 1 of these_images -- works   v �ww ~ s e t   i m a g e _ p a t h   t o   i m a g e   p a t h   o f   i t e m   1   o f   t h e s e _ i m a g e s   - -   w o r k st xyx l ���>z{�>  z B <set image_path to image path of these_images -- doesn't work   { �|| x s e t   i m a g e _ p a t h   t o   i m a g e   p a t h   o f   t h e s e _ i m a g e s   - -   d o e s n ' t   w o r ky }~} l ���=��=    display dialog image_path   � ��� 2 d i s p l a y   d i a l o g   i m a g e _ p a t h~ ��<� l ���;���;  �  return image_path   � ��� " r e t u r n   i m a g e _ p a t h�<  �n    R      �:��
�: .ascrerr ****      � ****� o      �9�9 0 errstr errStr� �8��7
�8 
errn� o      �6�6 0 errornumber errorNumber�7    k  �L�� ��� l ���5���5  � = 7 If our own error number, warn about out of range data.   � ��� n   I f   o u r   o w n   e r r o r   n u m b e r ,   w a r n   a b o u t   o u t   o f   r a n g e   d a t a .� ��4� Z  �L����� = ����� l ����3�2� o  ���1�1 0 errornumber errorNumber�3  �2  � m  ���0�0#(� k  ���� ��� I ���/��
�/ .sysodlogaskr        TEXT� m  ���� ��� � L a t i t u d e   v a l u e   o u t   o f   r a n g e .   L a t i t u d e   m u s t   b e   b e t w e e n   - 9 0   a n d   + 9 0� �.��
�. 
btns� J  ���� ��-� m  ���� ��� 
 C l o s e�-  � �,��+
�, 
disp� m  ���*�*  �+  � ��)� l ������ L  ���� m  ���(�(  � $  Return the default value (0).   � ��� <   R e t u r n   t h e   d e f a u l t   v a l u e   ( 0 ) .�)  � ��� = ����� l ����'�&� o  ���%�% 0 errornumber errorNumber�'  �&  � m  ���$�$#)� ��� k  ���� ��� I ���#��
�# .sysodlogaskr        TEXT� m  ���� ��� � L o n g i t u d e   v a l u e   o u t   o f   r a n g e .   L o n g i t u d e   m u s t   b e   b e t w e e n   - 1 8 0   a n d   + 1 8 0� �"��
�" 
btns� J  ���� ��!� m  ���� ��� 
 C l o s e�!  � � ��
�  
disp� m  ����  �  � ��� l ������ L  ���� m  ����  � $  Return the default value (0).   � ��� <   R e t u r n   t h e   d e f a u l t   v a l u e   ( 0 ) .�  � ��� = ����� l ������ o  ���� 0 errornumber errorNumber�  �  � m  ����#,� ��� k  ���� ��� I �����
� .sysodlogaskr        TEXT� m  ���� ��� � T h e   c l i p b o a r d   h a d   t o o   f e w   i t e m s !   T r y   c o p y i n g   t h e   l o c a t i o n   d a t a   a g a i n .� ���
� 
btns� J  ���� ��� m  ���� ��� 
 C l o s e�  � ���
� 
disp� m  ����  �  � ��� l ������ L  ���� m  ����  � $  Return the default value (0).   � ��� <   R e t u r n   t h e   d e f a u l t   v a l u e   ( 0 ) .�  � ��� = ����� l ������ o  ���� 0 errornumber errorNumber�  �  � m  ����#-� ��� k  ��� ��� I ����
� .sysodlogaskr        TEXT� m  ���� ��� � T h e   c l i p b o a r d   h a d   t o o   m a n y   i t e m s !   T r y   c o p y i n g   t h e   l o c a t i o n   d a t a   a g a i n .� �
��
�
 
btns� J   �� ��	� m   �� ��� 
 C l o s e�	  � ���
� 
disp� m  	��  �  � ��� l ���� L  �� m  ��  � $  Return the default value (0).   � ��� <   R e t u r n   t h e   d e f a u l t   v a l u e   ( 0 ) .�  � ��� = ��� l  ��  o  �� 0 errornumber errorNumber�  �  � m  � � #2� �� k  5  I 2��
�� .sysodlogaskr        TEXT m    � B P l e a s e   s e l e c t   o n e   o r   m o r e   i m a g e s . ��	

�� 
btns	 J  #( �� m  #& � 
 C l o s e��  
 ����
�� 
disp m  +,����  ��   �� l 35 L  35 m  34����   $  Return the default value (0).    � <   R e t u r n   t h e   d e f a u l t   v a l u e   ( 0 ) .��  ��  � k  8L  I 8E����
�� .sysodlogaskr        TEXT c  8A b  8= m  8; � 8 A n   u n k n o w n   e r r o r   o c c u r r e d :     o  ;<���� 0 errornumber errorNumber m  =@��
�� 
ctxt��    !  l FF��"#��  " 9 3 An unknown error occurred. Resignal, so the caller   # �$$ f   A n   u n k n o w n   e r r o r   o c c u r r e d .   R e s i g n a l ,   s o   t h e   c a l l e r! %&% l FF��'(��  ' < 6 can handle it, or AppleScript can display the number.   ( �)) l   c a n   h a n d l e   i t ,   o r   A p p l e S c r i p t   c a n   d i s p l a y   t h e   n u m b e r .& *��* R  FL��+,
�� .ascrerr ****      � ****+ o  JK���� 0 errstr errStr, ��-��
�� 
errn- o  HI���� 0 errornumber errorNumber��  ��  �4  ��   	 m     ..�                                                                                  iPho  alis    N  Macintosh HD               �V��H+  ��{
iPhoto.app                                                      �a��U8        ����  	                Applications    �V��      ��9    ��{  %Macintosh HD:Applications: iPhoto.app    
 i P h o t o . a p p    M a c i n t o s h   H D  Applications/iPhoto.app   / ��  ��  ��    /0/ l     ��������  ��  ��  0 1��1 i     232 I      �������� 0 selected_images  ��  ��  3 O     .454 Q    -6786 k    #99 :;: l   ��<=��  <   get selection   = �>>    g e t   s e l e c t i o n; ?@? r    ABA l   
C����C 1    
��
�� 
selc��  ��  B o      ���� 0 these_items  @ DED l   ��FG��  F &   check for single album selected   G �HH @   c h e c k   f o r   s i n g l e   a l b u m   s e l e c t e dE IJI Z    KL����K =   MNM l   O����O n    PQP 1    ��
�� 
pclsQ n    RSR 4    ��T
�� 
cobjT m    ���� S o    ���� 0 these_items  ��  ��  N m    ��
�� 
ipalL R    ������
�� .ascrerr ****      � ****��  ��  ��  ��  J UVU l  ! !��WX��  W ) # return the list of selected photos   X �YY F   r e t u r n   t h e   l i s t   o f   s e l e c t e d   p h o t o sV Z��Z L   ! #[[ o   ! "���� 0 these_items  ��  7 R      ������
�� .ascrerr ****      � ****��  ��  8 L   + -\\ m   + ,��
�� boovfals5 m     ]]�                                                                                  iPho  alis    N  Macintosh HD               �V��H+  ��{
iPhoto.app                                                      �a��U8        ����  	                Applications    �V��      ��9    ��{  %Macintosh HD:Applications: iPhoto.app    
 i P h o t o . a p p    M a c i n t o s h   H D  Applications/iPhoto.app   / ��  ��       ��^_`ab��cdefg��������������  ^ ���������������������������������� 0 selected_images  
�� .aevtoappnull  �   � ****�� 0 clip_in  �� 0 
clip_items  �� 0 	num_items  �� 0 lat  �� 0 long  �� 0 dialogresult dialogResult�� 0 these_images  �� 0 
this_photo  ��  ��  ��  ��  ��  ��  _ ��3����hi���� 0 selected_images  ��  ��  h ���� 0 these_items  i ]������������
�� 
selc
�� 
cobj
�� 
pcls
�� 
ipal��  ��  �� /� + !*�,E�O��k/�,�  	)jhY hO�W 	X  fU` ��j����kl��
�� .aevtoappnull  �   � ****j k    Mmm  ����  ��  ��  k �������� 0 i  �� 0 errstr errStr�� 0 errornumber errorNumberl D.������ (���������������� N�� a s���������������� ������� � � ��� ���	������������n����~?�}�|�{q�zo���y�������x
�� .miscactvnull��� ��� null
�� .JonsgClp****    ��� null�� 0 clip_in  
�� 
ascr
�� 
txdl
�� 
citm�� 0 
clip_items  
�� .corecnte****       ****�� 0 	num_items  
�� 
errn��#,��#-
�� 
cobj
�� 
doub�� 0 lat  �� 0 long  ������ Z
�� 
bool��#(���L�� ���#)
�� 
appr
�� 
btns
�� 
dflt
�� 
disp�� 
�� .sysodlogaskr        TEXT�� 0 dialogresult dialogResult��  n �w�v�u
�w 
errn�v���u  �� 0 selected_images  � 0 these_images  �~#2�} 0 
this_photo  
�| 
lati
�{ 
lngt�z 0 errstr errStro �t�s�r
�t 
errn�s 0 errornumber errorNumber�r  �y 
�x 
ctxt��N�J*j O}*j E�O�kv��,FO��-E�O�j 	E�O�l )��l�OPY �l )��l�OPY hOa kv��,FO�a k/a &E` O�a l/a &E` O_ a 
 _ a a & )�a la OPY hO_ a 
 _ a a & )�a la OPY hO ;a _ %a %_ %a  a !a "a #a $lva %a &a 'ka ( )E` *OPW 	X + ,hO)j+ -EQ` .O_ .f 
 _ .j 	j a & )�a /la 0Y J =k_ .j 	kh  _ .a �/E` 1O_ 1 _ *a 2,FO_ *a 3,FOPU[OY��Oa 4j )OPW �X 5 6�a   a 7a "a 8kva 'ja 9 )OjY ��a   a :a "a ;kva 'ja 9 )OjY {��  a <a "a =kva 'ja 9 )OjY Z��  a >a "a ?kva 'ja 9 )OjY 9�a /  a @a "a Akva 'ja 9 )OjY a B�%a C&j )O)�l�Ua �pp " 4 7 . 5 3 4 0 2 , 7 . 7 2 0 7 7 8b �qq�q q  rs�p�o�n�m�l�k�j�i�h�g�f�e�d�cr �tt  4 7 . 5 3 4 0 2s �uu  7 . 7 2 0 7 7 8�p  �o  �n  �m  �l  �k  �j  �i  �h  �g  �f  �e  �d  �c  �� c @G�Z�q�xd @��ƴ�e �bv�a
�b 
bhitv �ww 
 P a s t e�a  f �`x�` x  yzgy {{ ]�_|�^
�_ 
ipmr| A� ��  
�^ kfrmID  z }} ]�]~�\
�] 
ipmr~ A� ��  
�\ kfrmID  g  ]�[��Z
�[ 
ipmr� A� ��  
�Z kfrmID  ��  ��  ��  ��  ��  ��  ascr  ��ޭ