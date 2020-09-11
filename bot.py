import discord

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Random things"))
        print('Bot je ready')


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith("BinToDec"):
            input1 = message.content[8:]
            def bindec(n): 
                return int(n, 2)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(bindec(input1))

        if message.content.startswith("DecToBin"):
            input1 = message.content[8:]
            def decbin(n): 
                return bin(n).replace("0b","")
            input2 = int(input1)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(decbin(input2))

        if message.content.startswith("HexToDec"):
            input1 = message.content[8:]
            input2 = int(input1, 16)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(input2)
            
        if message.content.startswith("DecToHex"):
            input1 = message.content[8:]
            input2 = int(input1)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(hex(input2).replace("0x",""))

        if message.content.startswith("HexToBin"):
            input1 = message.content[8:]
            input2 = int(input1, 16)
            def decbin(n): 
                return bin(n).replace("0b","")
            vysledek = decbin(input2)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(vysledek)

        if message.content.startswith("BinToHex"):
            input1 = message.content[8:]
            def bindec(n): 
                return int(n, 2)
            bide = bindec(input1)
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(hex(bide).replace("0x",""))

client = MyClient()
client.run('Token-here')
