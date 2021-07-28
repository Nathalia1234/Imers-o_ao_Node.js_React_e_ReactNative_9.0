"""
Programa onde o usúario informa quanto ele tem em
dinheiro BR (Brasileiro) e mostra o valor convertido em dólar (USD).
Considerando US$ 1.00 =  R$ 5.16 no dia 28.07.2021

"""

# valor informada em moeda brasileira R$
real = float(input('Informe o valor R$: '))

# conversão do dia
Dolar = real / 5.16
Euro = real / 6.09
LibraEsterlina = real / 7.16
RupiaIndiana = real / 0.069
DolarAustraliano = real / 3.79
DolarCanadense = real / 4.11
DolarCingapura = real / 3.80
FrancoSuico = real / 5.65
DolarNeozelandes = real / 3.58
DolarHongKong = real / 0.66

# converter de BR para dólar
print(' Foi convertido R$ {:.2f} reais , para USD {:.2f} dólares ( USD - Dólar  dos EUA )'.format(real, Dolar))

# converter de BR para euro
print(' Foi convertido R$ {:.2f} reais , para EUR {:.2f} euros ( EUR )'.format(real, Euro))

# converter de BR para libra
print(' Foi convertido R$ {:.2f} reais , para GBP {:.2f} libras ( GBP - Libra esterlina  )'.format(real, LibraEsterlina))

# converter de BR para rupia indiana
print(' Foi convertido R$ {:.2f} reais , para INR {:.2f} rupia  ( INR - Rúpia indiana )'.format(real, RupiaIndiana))

# converter de BR para dolar australiano
print(' Foi convertido R$ {:.2f} reais , para AUD {:.2f} dólar australiano  ( AUD - Dólar australiano )'.format(real, DolarAustraliano))

# converter de BR para dolar canadense
print(' Foi convertido R$ {:.2f} reais , para CAD {:.2f} dólar canadense  ( CAD - Dólar canadense )'.format(real, DolarCanadense))

# converter de BR para dolar cingapura
print(' Foi convertido R$ {:.2f} reais , para SGD {:.2f} dólar  de cingapura  ( SGD - Dólar de cingapura )'.format(real, DolarCingapura))

# converter de BR para franco suiço
print(' Foi convertido R$ {:.2f} reais , para CHF {:.2f} dólar suiço  ( CHF - Franco suico )'.format(real, FrancoSuico))

# converter de BR para dolar neozelandes
print(' Foi convertido R$ {:.2f} reais , para NZD {:.2f} dólar neozelandês  ( NZD - Dólar neozelandês )'.format(real, DolarNeozelandes))

# converter de BR para dolar de hong kong
print(' Foi convertido R$ {:.2f} reais , para CAD {:.2f} dólar  de hong kong  ( CAD - Dólar de hong kong )'.format(real, DolarHongKong))
