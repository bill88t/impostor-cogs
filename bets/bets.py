import json
import random
import asyncio
import discord
from redbot.core import Config, checks, commands, bank


class bets(commands.Cog):

    __version__ = "1"

    def format_help_for_context(self, ctx):
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\nCog Version: {self.__version__}"

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def bets(self, ctx: commands.Context):
        """Bet if the banwheel will stop on black or red"""
    
    @bets.command()
    async def list(self, ctx):
        """Show all the bets."""
        with open('-----hardcoded path here-----') as fp:
            data = json.load(fp)
        keys = list(data.keys())
        msg = ''
        for x in keys:
            userd = int(x)
            usern = self.bot.get_user(userd).display_name
            b = data[x]
            a = str(b)
            if 'black' in a:
                color = 'black'
            elif 'red' in a:
                color = 'red'
            a = a.replace("[{'amount': ", "")
            a = a.replace("}, {'color': '", "")
            a = a.replace("'}]", "")
            a = a.replace("black", "")
            a = a.replace("red", "")
            money = int(a)
            msg += usern+' bet on '+color+' '+str(money)+' Μελεpoints'
        if len(msg)>0:
            await ctx.send(msg)
        else:
            await ctx.send("No bets.")

    @bets.command()
    async def confirm(self, ctx, color1, color2):
        """Ολοκλήρωσε τα στοιχήματα."""
        if (ctx.author.id==-----hardcoded admin1 here-----) or (ctx.author.id==-----hardcoded admin2 here-----):
            if (((color1 == "black") or (color1 == "red")) and ((color2 == "black") or (color2 == "red"))):
                with open('-----hardcoded path here-----') as fp:
                    data = json.load(fp)
                keys = list(data.keys())
                msg = ''
                for x in keys:
                    userd = int(x)
                    usern = self.bot.get_user(userd).display_name
                    b = data[x]
                    a = str(b)
                    if 'black' in a:
                        color = 'black'
                    elif 'red' in a:
                        color = 'red'
                    a = a.replace("[{'amount': ", "")
                    a = a.replace("}, {'color': '", "")
                    a = a.replace("'}]", "")
                    a = a.replace("black", "")
                    a = a.replace("red", "")
                    money = int(a)
                    msg += usern+' bet on '+color+' '+str(money)+' Μελεpoints, '
                    if ((color1 == color) and (color2 == color)):
                        msg += '5x win\n'
                        money = money * 5
                        await bank.deposit_credits(self.bot.get_user(userd), money)
                    elif ((color1 == color) or (color2 == color)):
                        msg += '2x win\n'
                        money = money * 2
                        await bank.deposit_credits(self.bot.get_user(userd), money)
                    else:
                        msg += 'lol loser!\n'
                if len(msg)>0:
                    await ctx.send(msg)
                else:
                    await ctx.send("No bets.")
            else:
                await ctx.send("Invalid colors! Options: black, red")
        else:
            await ctx.send("Only admin1 and admin2 can run this command!")

    @bets.command()
    async def clear(self, ctx, *, confirm):
        """Clear the bet database"""
        if (ctx.author.id==-----hardcoded admin1 here-----) or (ctx.author.id==-----hardcoded admin2 here-----):
            if (confirm == "yes"):
                with open('-----hardcoded path here-----') as fp:
                    data = json.load(fp)
                data.clear()
                with open("-----hardcoded path here-----", "w+") as fp:
                    json.dump(data, fp, sort_keys=True, indent=4)
                await ctx.send("Done")
            else:
                await ctx.send("Confirmation is required! Do: \\bets clear yes")
        else:
            await ctx.send("Only admin1 and admin2 can run this command!")

    @commands.command()
    async def bet(self, ctx, colors, *, bet: int):
        """Bet on a color"""
        if bet > 0:
            bal = await bank.get_balance(ctx.author)
            if (colors == "black") or (colors == "red"):
                if bal >= bet:
                    with open('-----hardcoded path here-----') as fp:
                        data = json.load(fp)
                    try:
                        b = data[f"{ctx.author.id}"]
                        a = str(b)
                        a = a.replace("[{'amount': ", "")
                        a = a.replace("}, {'color': '", "")
                        a = a.replace("'}]", "")
                        a = a.replace("black", "")
                        a = a.replace("red", "")
                        c = int(a)
                        if (c>bet):
                            await bank.deposit_credits(ctx.author, c-bet)
                        elif (c<bet):
                            await bank.withdraw_credits(ctx.author, bet-c)
                        data[f"{ctx.author.id}"] = {"amount": bet},{"color": colors}
                        await ctx.send("You had already put a bet this week. The old bet was cancelled and money were refunded.\nThe new bet was registered sucessfully.")
                    except KeyError:
                        data[f"{ctx.author.id}"] = {"amount": bet},{"color": colors}
                        await bank.withdraw_credits(ctx.author, bet)
                        await ctx.send("The bet was registered sucessfully.")
                    with open("-----hardcoded path here-----", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                else: 
                    await ctx.send("You do not have enough Μελεpoints. Perhaps you should study for him a bit.")
            else:
                await ctx.send("black or red. that's your options.")
        else:
            await ctx.send("bruh i'm not thaat stupid..")

    async def red_get_data_for_user(self, *, user_id: int):
        # This cog only stores the user id until the bets are cleared. One week.
        return {}

    async def red_delete_data_for_user(self, *, requester, user_id: int) -> None:
        # This cog only stores the user id until the bets are cleared. One week.
        pass
