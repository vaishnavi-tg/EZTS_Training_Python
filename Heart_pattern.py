for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    











'''At row 0 col 0,3,6 we dont want star so we took the condition col%3!=0
in row 1 we want stars at col 0 3 6 
col%3==0 is true ,when col value is 0 3 6  
 
  Logic3  
  row-col==2 
  2-0==2
  3-1==2
  4-2==2
  5-3==2              
     
        
           logic 4
              2+6==8
                 3+5==8
                    4+4==8   '''      