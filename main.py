from dotenv import load_dotenv
import discord

import utils.enviroment as enviroment
import utils.client 

env =  enviroment.EnvVars()
print(env.APLICATION_ID)
#client = client.MyClient()
#client.run(env.TOKEN)
