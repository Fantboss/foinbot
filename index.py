import discord, asyncio, random
token = "ODM5NjQxMjQyNzAyOTcwODgw.YJMm2A.wf9Lg8zevY5LYIMygPy2V1F0Msg"
intents = discord.Intents.all()
Client = discord.Client(intents=intents)

@Client.event
async def on_ready():
    print("bot")
    print(Client.user)
    print("===============================")
    game = discord.Game("!명령어")
    await Client.change_presence(status=discord.Status.online, activity=game)

    
@Client.event
async def on_message(message):
    if message.content == "!명령어":
        await message.channel.send("**모든 명령어는 관리자만 사용할수 있습니다 1.!디코,2.!청소,3.!추방,4.!DM,5.!유튜브,6.!로블록스,**")

    if message.content == "!디코":
        await message.channel.send("https://discord.gg/VC7VmZxhfa")

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제 완료!")

    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content == "!유튜브":
        await message.channel.send("https://www.youtube.com/channel/UCeCtNS2g3WaRrp7_QS0SaOg")

    if message.content == "!로블록스":
        await message.channel.send("https://www.roblox.com/users/2320486601/profile")

Client.run(token)
    
