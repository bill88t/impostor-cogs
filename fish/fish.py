import json
import random
import asyncio
import discord
import time
from typing import Optional
from redbot.core import Config, checks, commands, bank
from collections import OrderedDict 
from operator import getitem

class fish(commands.Cog):

    __version__ = "1"

    def format_help_for_context(self, ctx):
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\nCog Version: {self.__version__}"

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    async def fish(self, ctx, comm: Optional[str] = None, opti: Optional[str] = None):
        """fissssshhhhhhhhhhh"""
        if permission_independant_rules_here:
            with open('hardcoed_db_path') as fp:
                data = json.load(fp)
            keys = list(data.keys())
            msg = ''
            if comm is None:
                try:
                    rod = data[f"{ctx.author.id}"]['rod']
                    lure = data[f"{ctx.author.id}"]['lure']
                    multi = data[f"{ctx.author.id}"]['multi']
                    level = data[f"{ctx.author.id}"]['level']
                    xp = data[f"{ctx.author.id}"]['xp']
                except KeyError:
                    rod = 1
                    lure = 1
                    multi = 1
                    level =1
                    xp = 0
                    data[f"{ctx.author.id}"] = {}
                    data[f"{ctx.author.id}"]['rod'] = 1
                    data[f"{ctx.author.id}"]['lure'] = 1
                    data[f"{ctx.author.id}"]['multi'] = 1
                    data[f"{ctx.author.id}"]['regular'] = 0
                    data[f"{ctx.author.id}"]['salmon'] = 0
                    data[f"{ctx.author.id}"]['gmele'] = 0
                    data[f"{ctx.author.id}"]['cod'] = 0
                    data[f"{ctx.author.id}"]['tropical'] = 0
                    data[f"{ctx.author.id}"]['level'] = 1
                    data[f"{ctx.author.id}"]['xp'] = 0
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                runs = random.randint(0, 3+(rod*2))
                if runs > 20:
                    runs -= random.randint(0, runs-20)
                if runs == 0:
                    msg += 'You didn\'t get any fish!'
                else:
                    reg = 0
                    sal = 0
                    cod = 0
                    trp = 0
                    for x in range(runs-1):
                        #time.sleep(2)
                        fisht = random.randint(0, 3)
                        if fisht == 0:
                            reg += random.randint(0, 3+lure)
                        elif fisht == 1:
                            sal += random.randint(0, 2+lure)
                        elif fisht == 2:
                            cod += random.randint(0, 1+lure)
                        else:
                            trp += random.randint(0, lure)
                    if reg > 100:
                        reg -= random.randint(0, reg-30)
                    if sal > 90:
                        sal -= random.randint(0, sal-30)
                    if cod > 80:
                        cod -= random.randint(0, cod-30)
                    if trp > 50:
                        trp -= random.randint(0, trp-30)
                    xp += reg
                    xp += sal * 2
                    xp += cod * 3
                    xp += trp * 5
                    gm = random.randint(0, 5)
                    if gm == 5:
                        gm = 1
                        xp += 50
                    else:
                        gm = 0
                    data[f"{ctx.author.id}"]['regular'] += reg
                    data[f"{ctx.author.id}"]['salmon'] += sal
                    data[f"{ctx.author.id}"]['gmele'] += gm
                    data[f"{ctx.author.id}"]['cod'] += cod
                    data[f"{ctx.author.id}"]['tropical'] += trp
                    if level < 20:
                        req = level * 1000
                    elif level < 50:
                        req = level * 3000
                    else:
                        req = level * 10000
                    msgl = ''
                    while req <= xp:
                        xp -= req
                        level += 1
                        msgl = 'Level up! You are now level **{}**'.format(level)
                    data[f"{ctx.author.id}"]['xp'] = xp
                    data[f"{ctx.author.id}"]['level'] = level
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                    if (reg + sal + gm + cod + trp) != 0:
                        msg += 'You got: '
                        if reg != 0:
                            msg += str(reg)
                            msg += ' <:fish:818454611491946517>'
                        if sal != 0:
                            if reg != 0:
                                msg += ', '
                            msg += str(sal)
                            msg += ' <:salmon:818454701124091957>'
                        if gm != 0:
                            if (sal != 0) or (reg != 0):
                                msg += ', '
                            msg += str(gm)
                            msg += ' <:melefish:818467766771384331>'
                        if cod != 0:
                            if (sal != 0) or (reg != 0) or (gm != 0):
                                msg += ', '
                            msg += str(cod)
                            msg += ' <:cod:818454738936659981>'
                        if trp != 0:
                            if (sal != 0) or (reg != 0) or (gm != 0) or (cod != 0):
                                msg += ', '
                            msg += str(trp)
                            msg += ' <:trp:818454760184217600>'
                        msg += '!\n'
                    else:
                        msg += 'You didn\'t get any fish!'
                    if len(msgl):
                        msg += '\n'
                        msg += msgl
            elif comm == 'sell':
                try:
                    multi = data[f"{ctx.author.id}"]['multi']
                except KeyError:
                    rod = 1
                    lure = 1
                    multi = 1
                    data[f"{ctx.author.id}"] = {}
                    data[f"{ctx.author.id}"]['rod'] = 1
                    data[f"{ctx.author.id}"]['lure'] = 1
                    data[f"{ctx.author.id}"]['multi'] = 1
                    data[f"{ctx.author.id}"]['regular'] = 0
                    data[f"{ctx.author.id}"]['salmon'] = 0
                    data[f"{ctx.author.id}"]['gmele'] = 0
                    data[f"{ctx.author.id}"]['cod'] = 0
                    data[f"{ctx.author.id}"]['tropical'] = 0
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                if opti is None:
                    msg += 'Do sell fish/salmon/gmele/cod/tropical and specify the quantity, or do sell all'
                elif opti == 'all':
                    am = int(data[f"{ctx.author.id}"]['regular']) + int(data[f"{ctx.author.id}"]['salmon'])*3 + int(data[f"{ctx.author.id}"]['gmele'])*10 + int(data[f"{ctx.author.id}"]['cod'])*2 + int(data[f"{ctx.author.id}"]['tropical'])*4
                    data[f"{ctx.author.id}"]['regular'] = 0
                    data[f"{ctx.author.id}"]['salmon'] = 0
                    data[f"{ctx.author.id}"]['cod'] = 0
                    data[f"{ctx.author.id}"]['tropical'] = 0
                    data[f"{ctx.author.id}"]['gmele'] = 0
                elif opti == 'fish':
                    am = int(data[f"{ctx.author.id}"]['regular'])*multi
                    data[f"{ctx.author.id}"]['regular'] = 0
                elif opti == 'salmon':
                    am = int(data[f"{ctx.author.id}"]['salmon'])*3*multi
                    data[f"{ctx.author.id}"]['salmon'] = 0
                elif opti == 'cod':
                    am = int(data[f"{ctx.author.id}"]['cod'])*2*multi
                    data[f"{ctx.author.id}"]['cod'] = 0
                elif opti == 'tropical':
                    am = int(data[f"{ctx.author.id}"]['tropical'])*4*multi
                    data[f"{ctx.author.id}"]['tropical'] = 0
                elif opti == 'gmele':
                    am = int(data[f"{ctx.author.id}"]['gmele'])*10*multi
                    data[f"{ctx.author.id}"]['gmele'] = 0
                try:
                    await bank.deposit_credits(self.bot.get_user(ctx.author.id), am)
                    msg += 'You got ' + str(am) + ' Μελεpoints!'
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                except:
                    msg += 'Invalid item!'
            elif comm == 'upgrade':
                bal = await bank.get_balance(ctx.author)
                try:
                    rod = data[f"{ctx.author.id}"]['rod']
                    lure = data[f"{ctx.author.id}"]['lure']
                    multi = data[f"{ctx.author.id}"]['multi']
                except KeyError:
                    rod = 1
                    lure = 1
                    multi = 1
                    data[f"{ctx.author.id}"] = {}
                    data[f"{ctx.author.id}"]['rod'] = 1
                    data[f"{ctx.author.id}"]['lure'] = 1
                    data[f"{ctx.author.id}"]['multi'] = 1
                    data[f"{ctx.author.id}"]['regular'] = 0
                    data[f"{ctx.author.id}"]['salmon'] = 0
                    data[f"{ctx.author.id}"]['gmele'] = 0
                    data[f"{ctx.author.id}"]['cod'] = 0
                    data[f"{ctx.author.id}"]['tropical'] = 0
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                if opti is None:
                    msg += 'Do upgrade rod/lure/multiplier amount. You can have up to 30 of each upgrade.\nRod upgrades cost 500 Μελεpoints each, lure upgrades cost 700 Μελεpoints each and multiplier upgrades cost 2000 each.\n Rod upgrades improve your chances to get fish.\nLure upgrades improve your rates of getting multiple of each.\nAnd multiplier upgrades make your fish sell for more Μελεpoints'
                elif opti == 'rod':
                    if (data[f"{ctx.author.id}"]['rod'] < 30) and (bal >= 500):
                        await bank.withdraw_credits(self.bot.get_user(ctx.author.id), 300)
                        data[f"{ctx.author.id}"]['rod'] += 1
                        with open("hardcoed_db_path", "w+") as fp:
                            json.dump(data, fp, sort_keys=True, indent=4)
                        msg += 'Upgrade done!'
                    else:
                        msg += 'Already maxed out! Or balance too low!'
                elif opti == 'lure':
                    if (data[f"{ctx.author.id}"]['lure'] < 30) and (bal >= 700):
                        await bank.withdraw_credits(self.bot.get_user(ctx.author.id), 500)
                        data[f"{ctx.author.id}"]['lure'] += 1
                        with open("hardcoed_db_path", "w+") as fp:
                            json.dump(data, fp, sort_keys=True, indent=4)
                        msg += 'Upgrade done!'
                    else:
                        msg += 'Already maxed out! Or balance too low!'
                elif opti == 'multiplier':
                    if (data[f"{ctx.author.id}"]['multi'] < 30) and (bal >= 2000):
                        await bank.withdraw_credits(self.bot.get_user(ctx.author.id), 1000)
                        data[f"{ctx.author.id}"]['multi'] += 1
                        with open("hardcoed_db_path", "w+") as fp:
                            json.dump(data, fp, sort_keys=True, indent=4)
                        msg += 'Upgrade done!'
                    else:
                        msg += 'Already maxed out! Or balance too low!'
                else:
                    msg += 'Invalid upgrade!'
            elif (comm == 'inventory') or (comm == 'inv'):
                try:
                    rod = data[f"{ctx.author.id}"]['rod']
                    lure = data[f"{ctx.author.id}"]['lure']
                    multi = data[f"{ctx.author.id}"]['multi']
                    level = data[f"{ctx.author.id}"]['level']
                    xp = data[f"{ctx.author.id}"]['xp']
                    reg = data[f"{ctx.author.id}"]['regular']
                    sal = data[f"{ctx.author.id}"]['salmon']
                    gm = data[f"{ctx.author.id}"]['gmele']
                    cod = data[f"{ctx.author.id}"]['cod']
                    trp = data[f"{ctx.author.id}"]['tropical']
                except KeyError:
                    data[f"{ctx.author.id}"] = {}
                    data[f"{ctx.author.id}"]['rod'] = 1
                    data[f"{ctx.author.id}"]['lure'] = 1
                    data[f"{ctx.author.id}"]['multi'] = 1
                    data[f"{ctx.author.id}"]['regular'] = 0
                    data[f"{ctx.author.id}"]['salmon'] = 0
                    data[f"{ctx.author.id}"]['gmele'] = 0
                    data[f"{ctx.author.id}"]['cod'] = 0
                    data[f"{ctx.author.id}"]['tropical'] = 0
                    data[f"{ctx.author.id}"]['level'] = 1
                    data[f"{ctx.author.id}"]['xp'] = 0
                    with open("hardcoed_db_path", "w+") as fp:
                        json.dump(data, fp, sort_keys=True, indent=4)
                if level < 20:
                    req = level * 1000
                elif level < 50:
                    req = level * 3000
                else:
                    req = level * 10000
                msg += '**'
                msg += ctx.author.display_name
                msg += '\'s inventory:**\n'
                msg += '{} <:fish:818454611491946517>,'.format(reg)
                msg += ' {} <:cod:818454738936659981>,'.format(cod)
                msg += ' {} <:salmon:818454701124091957>,'.format(sal)
                msg += ' {} <:trp:818454760184217600>,'.format(trp)
                msg += ' {} <:melefish:818467766771384331>\n'.format(gm)
                msg += '**\n'
                msg += ctx.author.display_name
                msg += '\'s fishing id:**\n'
                msg += 'Level {}\n'.format(level) 
                msg += '{}/'.format(xp)
                msg += '{} XP\n'.format(req)
                msg += '\n**Fishing rod status:**\n'
                msg += '{}'.format(rod)
                msg += '/30 rod upgrades\n'
                msg += '{}'.format(lure)
                msg += '/30 lure upgrades\n'
                msg += '{}'.format(multi)
                msg += '/30 multiplier upgrades'
            elif (comm == 'ld') or (comm == 'leaderboard'):
                count = 0
                #res = sorted(data.items(), key = lambda x: x[1]['level'], reverse=True)
                res = sorted(data, key=lambda x: (data[x]['level']), reverse=True)
                #self.bot.get_guild(ctx.guild.id).get_member(int(x)).display_name
                for x in range(10):
                    idn = int(res[x])
                    msg += str(x)
                    msg += '. '
                    msg += self.bot.get_guild(ctx.guild.id).get_member(idn).display_name
                    msg += ' level '
                    msg += str(data[str(idn)]['level'])
                    msg += '\n'
            else:
                msg = 'Invalid command specified!'
            await ctx.send(msg)
        else:
            await ctx.send("Fishing not allowed!")

    async def red_get_data_for_user(self, *, user_id: int):
        # This cog does not store any user data.
        return {}

    async def red_delete_data_for_user(self, *, requester, user_id: int) -> None:
        # This cog does not store any user data.
        pass
