

async def help(message):
    channel = message.channel

    await channel.send(""" 
    >>> 
    ** Comands **

    ```css
    #whatsup: Say whatsup in a random way
    .whatsup
    [whatsup]
    
    [meme] .<phrase>
    ```
    """)