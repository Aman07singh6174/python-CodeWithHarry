str='''Dear <|name|>, 
 you are selected!
    <|date|>
'''
print(str.replace('<|name|>', 'John').replace('<|date|>', '2024-06-15'))