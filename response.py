import time

async def reponseTime(message):
    mensagemTime = await message.channel.send("Isso pode ser um pouco difícil, calma...")
    time.sleep(5)  
    mensagemFinish = await message.channel.send("Pronto!!")
    await mensagemFinish.add_reaction("✅")
    time.sleep(2)

    await mensagemTime.delete()