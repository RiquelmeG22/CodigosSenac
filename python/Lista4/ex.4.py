populacaoA = 8000
populacaoB = 20000
conta = 0

while(populacaoA <= populacaoB):
    populacaoA = int(populacaoA *1.03)
    populacaoB = int(populacaoB*1.15)
    conta += 1
print(f'Anos necessesarios {conta}, população do pais A {populacaoA}, população do pais B {populacaoB} ')   