
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h  

random_turn  PROC               ;declaration des nombres aleatoires

CreateGrid   PROC     near      ;defini une fonction nomme CreateGrid pour inserer des coordonnees
            
             
             PUSH AX            ; empile ou sauvegarde le contenu du registre AX sur la pile
             
             PUSH BX            
             
             MOV AX, 0          ;defini la premiere variable nomme AX auquelle j'insere la valeur 0
             
             MOV DS,AX          ;le registre DS enregistre la donnee de ma variables AX
             
             MOV BX, 0          
             
             MOV DS, BX
             

Debuttantque1:
            
            
            AH_inferieur_ou_egal_CH:      ;label de ma boucle while
            
            CMP AH,CH                     ;compare deux registres
            
            JLE AH_inferieur_ou_egal_CH   ;instruction inferieur ou egal
            
            INC AH                        ; incremente de 1 AH
            
            JMP                           ;fait un saut apres l'incrementation

fintantque1:
                                
             
             
Debuttantque2:
            
            
            BH_inferieur_ou_egal_DH:
            
            CMP BH,DH 
            
            JLE BH_inferieur_ou_egal_DH
            
            INC BH 
            
            JMP


fintantque2:
                             
            
            
            CALL CreateGrid  ;j'appelle ma fonction
             

            
            RET
             
                
                                 
CreateGrid  ENDP  ;Fin des declarations de ma fonction






EmptyGrid   PROC        near             
    
            MOV AX,0 
            
            MOV BX,CX
            
            DIV BX
           
           
Debuttanque1:
           
          
           AX_infirieur_ou_egal_DX:

           CMP AX,DX 
           
           JLE AX_infirieur_ou_egal_DX
           
           
fintanque1:


            MOV BL,0
            
            MOV AL,DL
            
            DIV AL
            

Debuttanque2:
           
           
           BL_infirieur_ou_egal_AH:
           
           CMP BL,AH
           
           JLE BL_infirieur_ou_egal_AH
           
           MOV BH, CH 
           
           MUL AX
           
           MOV CX, DX
           
           MUL BX 
           
           
           INC AX
           
           INC BL
           

fintanque2: 
           
           CALL EmptyGrid   

           RET


EmptyGrid ENDP    



RandomGrid   PROC   near            ;defini fonction aleatoire
    


           CALL randomGrid

           RET



RandomGrid ENDP

Random_turn ENDP