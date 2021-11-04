#run.py
import asyncio, discord
from typing import ContextManager
from dice import *
from discord.ext import commands
import datetime



game = discord. Game("F 도움말 입력")
token = ("OTAxNDM4NzgwMTQ4NDE2NTUy.YXP4SQ.AO9_l_2mlflLsoi1dRrdsVittCA")


bot = commands.Bot(command_prefix="F " ,status = discord.Status.online, active = game)

@bot.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(bot.user.name)
    print(bot.user.id)
    print("==========")
    game = discord.Game("F 봇 작동")
    await bot.change_presence(status=discord.Status.online, activity=game)
        
                

@bot.command()
async def 에프봇(ctx):
    await ctx.send("F 봇 입니다. 모르는것이 있으면 F 도움말을 입력해 주세요 ")

@bot.command()
async def 따라말하기(ctx, *, txt):
    await ctx.send (txt)



@bot.command()
async def 따라해(ctx, *, txt):
    await ctx.send (txt)

@bot.command()
async def Efg(ctx, *, txt):
    await ctx.send (txt)

@bot.command()
async def 주연(ctx):
    await ctx.send("착한 비밀 쥬쥬")

@bot.command()
async def 보라(ctx):
    await ctx.send("보라돌이")

@bot.command()
async def 꾸엘(ctx):
    await ctx.send("못생겼어")

@bot.command()
async def 짱구(ctx):
    await ctx.send("존잘")

@bot.command()
async def 퍼플(ctx):
    await ctx.send("눈맨 나빠")

@bot.command()
async def 녹차(ctx):
    await ctx.send("눈맨 보다 잘났음 ㄲ")

@bot.command()
async def 계발자(ctx):
    await ctx.send(f'{ctx.message.author.mention}님 보다 잘생긴 존잘 짱구')

@bot.command()
async def 개발자(ctx):
    await ctx.send(f'{ctx.message.author.mention}님 보다 잘생긴 존잘 짱구')

@bot.command()
async def 민초(ctx):
    await ctx.send("맛있음")
    await ctx.send("https://img1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/6yAc/image/vzH4u71GGlPqEMmzeLxfnNWZPZc.png")

@bot.command()
async def 정보(ctx):
    date = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0x00ff00, title = "내 정보")
    embed.add_field(name="닉네임", value=ctx.author.name, inline=True)
    embed.add_field(name="서버 닉네임", value=ctx.author.display_name, inline=True)
    embed.add_field(name="아이디", value=ctx.author.id, inline=True)
    embed.add_field(name="디스코드 가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def 그냥나임(ctx):
    await ctx.send("그냥너임")

@bot.command()
async def 핑(ctx):
    embed = discord.Embed(color=0x00ff00, title = "F 봇 현재 핑")
    embed.add_field(name="F 봇의 현재 핑", value='현재의 핑 상테는 {0}초'.format(bot.latency), inline = True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/901438780148416552/c668ce80f840e02f0ca7caaf1d3a66a3.png")
    await ctx.send(embed=embed)
    

@bot.command()
async def 눈맨(ctx):
    await ctx.send("지옥에서 온 녹지 않는 눈사람")

@bot.command()
async def 도움말(ctx):
    await ctx.send("F 주사위는 주사위 게임을 할 수 있습니다, F 따라말하기 <원하는 말>, F 바보 F 봇을 놀리면.... 어마무시한 벌을 받습니다., F 정보 자신의 정보를 나타냅니다., F 핑 현재의 핑을 알 수 있습니다.")

@bot.command()
async def 바보(ctx):
    for j in range():
        await ctx.author.send(f'{ctx.message.author.mention}님도 바보')

@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "F 봇의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다.")

bot.run(token)
