import wolframalpha

client = wolframalpha.Client('7QJ4YH-T5RP7VR292')

while True:
    query=str(input('Query: '))
    res= client.query(query)
    output=next(res.results).text
    print(output)
