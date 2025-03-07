print("Insira Um número")
table = {}
n = io.read()
n = tonumber(n)
Pares = 0

print("Seus Numeros São:")
local i = 0
while i < n do
  
  local x = math.random(1,100)
  table[n] = x
  print(table[n])
  i = i + 1

  if table[n]%2 == 0 then
     pares = pares + 1
  end

end


print('Quantidade de Numeros Pares: ', pares)