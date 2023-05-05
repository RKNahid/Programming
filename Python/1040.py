a,b,c,d = map(float,input().split())
av = ((a*2)+(b*3)+(c*4)+d)/10
print("Media: %.1f"%av)
if av<5.0:
    print("Aluno reprovado.")
elif av>=7.0:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %.1f"%e)
    avg = (av+e)/2
    if avg>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f"%avg)
