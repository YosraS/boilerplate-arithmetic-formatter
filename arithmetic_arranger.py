import re
class ArthProblem:
    def __init__(self,d1,d2,op):
        self.d1=d1
        self.d2=d2
        self.op=op
    def ResProblem(self):
        
        if self.op=='-':
            return str(int(self.d1)-int(self.d2))
        elif self.op=='+':
            return str(int(self.d1)+int(self.d2))
    
    def StrProblemBis(self,res=False):
        if len(self.d1)> len(self.d2):
            ln='--'+('-'*len(self.d1))
                
            diff=' '+(' '*((len(self.d1)-len(self.d2))))
                
            d= (('  '+str(self.d1))+"\n"+(str(self.op)+diff+str(self.d2)))+"\n"+ln+"\n"
        elif len(self.d1)< len(self.d2):
            
            ln='--'+('-'*len(self.d2)) 
            diff='  '+(' '*((len(self.d2)-len(self.d1))))
                
            d= ((diff+str(self.d1))+"\n"+(str(self.op)+' '+str(self.d2)))+"\n"+ln+"\n"
        else:
            ln='--'+('-'*len(self.d1))
            d= (("  "+str(self.d1))+"\n"+(str(self.op)+' '+str(self.d2)))+"\n"+ln+"\n"
        
        if res==False:
            return d
        elif res== True:
            return d+' '*(len(ln)-len(self.ResProblem()))+str(self.ResProblem())+"\n"

def display_list(arranged_problems):
    spacing = ' ' * 4
    
    for pieces in zip(*(prb.splitlines() for prb in arranged_problems)):
     print(spacing.join(pieces))
def display_listFourth(arranged_problems):
    spacing= ' ' * 4  # Space between cards.
    res=[]
    for pieces in zip(*(prb.splitlines() for prb in arranged_problems)):
        res.append(str(spacing.join(pieces)))
    text=''
    for i in res:
      text=text+i+'\n'
    text2=text[0:len(text)-1]
    #text=res[0]+'\n'+res[1]+'\n'+res[2]
    return text2

def arithmetic_arranger(problems,sol=False):
  arranged_problems=[]
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
      
    regex=r'(?P<dig1>.+)\s(?P<op>.{1})\s(?P<dig2>.+)'
    matches=re.search(regex,problem)
    d1=matches.group('dig1')
    d2=matches.group('dig2')
    op=matches.group('op')
      
    if d1.isdigit()==False or d2.isdigit()==False:
      return "Error: Numbers must only contain digits."
    elif op != '-' and op!='+':
      return "Error: Operator must be '+' or '-'."
    elif len(d1)>4 or len(d2)>4:
      return "Error: Numbers cannot be more than four digits."
    else:
      arranged_problems.append(ArthProblem(d1,d2,op).StrProblemBis(sol))
      
  return display_listFourth(arranged_problems)

