
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h  


             
                                                                                                                                 
CreateGrid   PROC     near               ;defini une fonction nomme CreateGrid pour inserer des coordonnees
            
             
             PUSH AX                     ; empile ou sauvegarde le contenu du registre AX sur la pile
             
             PUSH BX            
             
             MOV AX,0                    ;defini la premiere variable nomme AX auquelle on insere la valeur 0
             
             MOV DS,AX                   ;le registre DS enregistre la donnee de ma variables AX
             
             MOV BX,0          
             
             MOV DS,BX
             

Debuttantque1:
            
            
            AH_inferieur_ou_egal_CH:      ;label de ma premiere boucle while
            
            CMP AH,CH                     ;compare deux registres
            
            JLE AH_inferieur_ou_egal_CH   ;instruction inferieur ou egal
            
            INC AH                        ;incremente de 1 AH
            
            JMP                           ;fait un saut apres l'incrementation

fintantque1:
                                
             
             
Debuttantque2:
            
            
            BH_inferieur_ou_egal_DH:      ;label de ma deuxieme boucle while
                                          
            CMP BH,DH                     ;compare deux registres
            
            JLE BH_inferieur_ou_egal_DH   ;instruction inferieur ou egal
            
            INC BH                        ;incremente BH de 1
            
            JMP                           ;fait un saut apres l'incrementation


fintantque2:
                             
            
            
            CALL CreateGrid               ;j'appelle ma fonction
             

            
            RET
             
                
                                 
CreateGrid  ENDP                          ;Fin des declarations de ma fonction






EmptyGrid   PROC        near              ;defini une fonction nomme EmptyGrid pour pour initialiser la grille
    
            MOV AX,0                      ;insere la valeur 0 dans le registre AX
            
            MOV BX,CX
                                          ;divise BX et CX
            DIV BX
           
           
Debuttanque1:
           
                                          ;label de ma boucle while
           AX_infirieur_ou_egal_DX:
                                          ;compare le registre AX et le reste de la division
           CMP AX,DX 
           
           JLE AX_infirieur_ou_egal_DX
           
           
fintanque1:


            MOV BL,0
            
            MOV AL,DL
            
            DIV AL
            

Debuttanque2:
           
           
           BL_infirieur_ou_egal_AH:
                                          ;compare le registre BL et le reste de la division
           CMP BL,AH
           
           JLE BL_infirieur_ou_egal_AH
           
           MOV BH,CH 
           
           MUL AX                         ;multiplie BH et CH dans AX
           
           MOV CX,DX
           
           MUL BX                         ;multiplie CX et DX dans BX
           
           
           INC AX                         ;incremente AX de 1
                                          
           INC BL                         ;incremente BL de 1
           

fintanque2: 
           
           CALL EmptyGrid   

           RET

                                           
EmptyGrid ENDP                            ;Fin des declarations de la fonction EmptyGrid




RandomGrid  PROC   near                   ;defini une fonction aleatoire
    

            MOV CX,0 
            
            MOV AX,BX
            
            DIV AX
           
           
Debuttanque:
           
          
           CX_infirieur_ou_egal_DX:       ;label de ma boucle while

           CMP CX,DX                      ;compare le registre CX et le reste de la division de AX et BX
           
           JLE CX_infirieur_ou_egal_DX    ;voit si CX est inferieur ou egal a DX
           
           
fintanque:


            MOV CL,0
            
            MOV AL,BL
            
            DIV AL
            

Debuttanque3:
           
           
           CL_infirieur_ou_egal_DL:       ;label de ma boucle while
           
           CMP CL,DL                      ;compare le registre CL et le reste de la division de AL et BL nomme DL
           
           JLE CL_infirieur_ou_egal_DL    ;voit si CL est inferieur ou egal a DL
           
           MOV AH,BH 
           
           MUL CX                         ;multiplie AH et BH dans CX
           
           MOV BX,CX
                                          
           MUL DX                         ;multiplie BX et CX dans DX
           
           
           INC CX
           
           INC CL
           

fintanque3: 

          
           CALL randomGrid                ;j'appelle la fonction ramdomGrid

           RET                            ;Derniere instruction de la fonction



RandomGrid ENDP                           ;Fin des declarations de la fonction

  


                                          ;Defini une fonction nomme DieOrlive pour les principes de vie ou de mort 
DieOrLive PROC  near 
          
          MOV AX, 0
          
          MOV BX, 1 
          
          MOV CX, 0
          

DebutPour:                                ;Debut de ma boucle for
          

PremierIF:

          
          AX_superieur_0 :
          
     
          CMP AX,0                        ;compare le registre AX et 0
          
          JA AX_superieur_0               ;Voit si AX est superieur a 0
          
    
          CMP BX,0                        
          
          BX_supereur_0:
          
          JA BX_superieur_0
          
          DX_egal_a_zero:
          
       
          CMP DX,1                        ;compare DX et 1
          
          JE DX_egal_a_zero               ;voit si DX est egal a 1
          
          INC CX                          ;incremente CX
          
          JMP                             ;fait un saut apres l'incrementation
          

FinPremierIF:          
          
          
DeuxiemeIF:          
          
          
          BX_superieur_0:
          
          CMP BX,0
          
          JA BX_superieur_0
          
          DX_egal_a_1:
          
          CMP DX,1  
          
          JE DX_egal_a_1
          
          INC CX  
          
          JMP
          

FinDeuxiemeIF:         
          
          
TroisiemeIF:          
          
          
          AX_inferieur_BX:
          
          CMP AX,BX
          
          JL AX_inferieur_BX 
          
          CMP BX,0
          
          CX_superieur_0:
          
          JA CX_superieur_0
          
          BX_egal_a_1:
         
          CMP BX,1 
          
          JE BX_egal_a_1
          
          INC CX  
          
          JMP
          

FinTroisiemeIF:          
          
         
QuatriemeIF:         
         
         
          AX_superieur_a_zero:
          
          CMP AX,0
          
          JA AX_superieur_a_zero
          
          D_egal_a_1:
          
          CMP DX,1
          
          JE DX_egal_a_1                  
                            
          INC CX 
          
          JMP
          

FinQuatriemeIF:          
          
          
          
CinquiemeIF:          
          
         
          BX_inferieur_a_AX: 
          
          CMP BX,AX
          
          JL BX_inferieur_a_AX
          
          AX_egal_a_1:
         
          CMP AX, 1
          
          JE AX_egal_a_1
          
          INC CX  
          
          JMP
          

FinCinquiemeIF:          
          
         
SixiemeIF:         
         
          AX_superieur_a_0:
          
          CMP AX,0
          
          JA AX_superieur_a_0
          
          BX_inferieur_CX:
          
          CMP BX,CX 
          
          JL BX_inferieur_CX
          
          CMP DX,1
          
          JE DX_egal_a_1
          
          INC CX   
          
          JMP
          

FinSixiemeIF:          
          
          
SeptimeIF:         
         
          AX_inferieur_a_CX:
          
          CMP AX,CX 
          
          JL AX_inferieur_a_CX 
          
          CMP DX,1
          
          JE DX_egal_a_1
          
          INC CX 
          
          JMP
          

FinSeptiemeIF:          
          
         
HuitiemeIF:         
         
          
          CX_inferieur_a_AX:
          
          CMP CX,AX  
          
          JL CX_inferieur_a_AX
          
          CX_inferieur_a_BX:
         
          CMP CX,BX 
          
          JL CX_inferieur_a_BX
          
          Egalite_DX_a_1:
          
          CMP DX, 1
          
          JE Egalite_DX_A_1
          
          INC CX  
          
          JMP


FinHuitiemeIF:          
          
          

NeuviemeIF:

          
          DX_egal_a_3:
           
          CMP DX,3
          
          JE DX_egal_a_3
          
          Dl_egal_a_1:
          
          XOR AX,1
          
          JE AX_egal_a_1 
          
          JMP
          

FinNeuviemeIF:


          
DixiemeIF:          
          
         
          DX_superieur_a_3:
          
          CMP DX,3 
          
          JA DX_superieur_a_3
          
          OR DX,2
          
          DX_inferieur_a_2 :
         
          JL DX_inferieur_a_2 
          
          DX_egal_a_0:
          
          XOR DX,0
          
          JE DX_egal_a_0 
          
          JMP
          

FinDixiemeIF:          
          
          

FinBouclePour :
                       
          
          CALL DieOrLive
          
          RET
          

DieOrLive ENDP    