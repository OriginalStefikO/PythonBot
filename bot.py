import discord
import time
import math

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='seznam příkazů "help"'))
        print('Bot je ready')


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


        if message.content == "help":
            embed = discord.Embed(
                title = "Seznam příkazů:",
                color = discord.Color.green()
            )
            embed.set_footer(
            text="Made by Stefik_O"
            )
            embed.add_field(
            name="BinToDec", 
            value="DecToBin",
            inline= True
            )
            embed.add_field(
            name="BinToHex",
            value="HexToBin",
            inline= True
            )
            embed.add_field(
            name="BinToText",
            value="TextToBin",
            inline= True
            )
            embed.add_field(
            name="DecToHex",
            value="HexToDec",
            inline= True
            )
            embed.add_field(
            name="DecToText",
            value="TextToDec",
            inline= True
            )
            embed.add_field(
            name="HexToText",
            value="TextToHex",
            inline= True
            )
            embed.add_field(
            name="Encode",
            value='Pro zakódování musíš zadat dvojciferné číslo, které si musíš zapamatovat pro dekódování:\n Encode 23 Ahoj',
            inline= False
            )
            embed.add_field(
            name="Decode",
            value='Pro dekódování musíš použít stejné číslo jako jsi použil na zakódování:\n Decode 23 188729c7c',
            inline= False
            )

            await message.channel.send(embed=embed)

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

        if message.content.startswith("BinToText"):
            input1 = message.content[10:]
            def decode_binary_string(s):
                return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(decode_binary_string(input1))

        if message.content.startswith("TextToBin"):
            input1 = message.content[10:]
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            await message.channel.send(''.join('{:08b}'.format(d) for d in bytearray(input1, 'utf-8')))

        if message.content.startswith("TextToHex"):
            input1 = message.content[10:]
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            textbin = ''.join('{:08b}'.format(d) for d in bytearray(input1, 'utf-8'))
            def bindec(n): 
                return int(n, 2)
            bide = bindec(textbin)
            await message.channel.send(hex(bide).replace("0x",""))

        if message.content.startswith("HexToText"):
            input1 = message.content[10:]
            await message.channel.send("⇣⇣⇣⇣⇣⇣")
            vysledek = int(input1, 16)
            def decbin(n): 
                return bin(n).replace("0b","")
            bide = decbin(vysledek)
            def decode_binary_string(s):
                return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
            await message.channel.send(decode_binary_string("0" + bide))

client = MyClient()
client.run('Your token copy here')
