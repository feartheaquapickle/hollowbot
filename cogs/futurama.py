import random
import discord
import os
from discord.ext import commands

class futurama(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Futurama loaded.')

# Generates a random quote from Bender Rodriquez.
    @commands.command()
    async def fb(self, ctx):
        await ctx.message.delete()

        bender = [ '"Bite my shiny metal ass!"',
                '"I’m so embarrassed. I wish everybody else was dead."',
                '"My story is a lot like yours, only more interesting ‘cause it involves roclients."',
                '"This is the worst kind of discrimination there is: the kind against me!"',
                '"Anything less than immortality is a complete waste of time."',
                '"How can I be so bad at everything I try, and still be so great?"',
                '"My life, and by extension everyone else\'s, is meaningless."',
                '"Of all the friends I\'ve had, you\'re the first."',
                '"I\'m going to build my own theme park! With blackjack! And hookers!"',
                '“I hope he didn’t die. Unless he left a note naming me his successor, then I hope he did die.”',
                '“Well, if jacking on will make strangers think I’m cool, I’ll do it.”',
                '“Have you ever tried simply turning off your TV, sitting down with your child, and hitting them?”',
                '“Hey sexy mama. Wanna kill all humans?”',
                '“Blackmail is such an ugly word. I prefer extortion. The ‘x’ makes it sound cool.”',
                '“Game’s over, losers! I have all the money. Compare your lives to mine and then kill yourselves.”',
                '“O’ cruel fate, to be thusly boned! Ask not for whom the bone bones—it bones for thee.”',
                '“Hey, whose been messing with my radio? This isn’t alternative rock, it’s college rock.”',
                '“Hahahahaha. Oh wait you’re serious. Let me laugh even harder.”',
                '“You know what cheers me up? Other people’s misfortune.”',
                '“Afterlife? If I thought I had to live another life, I’d kill myself right now!”',]

        await ctx.send(f'```{random.choice(bender)}```')

# Generates a random quote from Zapp Brannigan.
    @commands.command()
    async def fz(self, ctx):
        await ctx.message.delete()

        zapp = [ '“We know nothing about them, their language, their history or what they look like. But we can assume this. They stand for everything we don’t stand for. Also they told me you guys look like dorks.”',
                '“Cham-paggin?”',
                '“The way to a woman’s bed is through her parents. Have sex with them and you’re in.”',
                '“She’s built like a steakhouse, but she handles like a bistro!”',
                '“I am the man with no name. Zapp Brannigan, at your service.”',
                '“Stop exploding you cowards!”',
                '“The spirit is willing, but the flesh is spongy and bruised.”',
                '“If we hit that bullseye, the rest of the dominoes will fall like a house of cards. Checkmate.”',
                '"It was almost the perfect crime, but you forgot one thing: Rock crushes scissors ... but paper covers rock ... and scissors cut paper. Kif, we have a conundrum. Search them for paper, and bring me a rock."',
                '"When I\'m in command, every mission is a suicide mission."',
                '"Call me cocky, but if there\'s an alien out there I can\'t kill I haven\'t met him and killed him yet."',
                '“Brannigan’s Law is like Brannigan’s love; hard and fast!”',
                '“Your face has been declared a weapon of mass disgusting!”',
                '“I want to slap your sister with a slice of bologna.”',
                '“Happy Freedom Day, ladies! Come on, show me something. Anything. Seriously, I’d take an armpit.”',
                '“In the game of chess, you can never let your adversary see your pieces.”',
                '“I’ve never heard of such a brutal and shocking injustice that I cared so little about!”',]

        await ctx.send(f'```{random.choice(zapp)}```')

# Generates a random quote from Philip J. Fry
    @commands.command()
    async def ff(self, ctx):
        await ctx.message.delete()

        fry = [ '"Wait, I\'m having one of those things, you know, a headache with pictures."',
                '"I am literally angry with rage!"',
                '"It\'s just like the story of the grasshopper and the octopus."',
                '"It\'s like a party in my mouth and everyone\'s throwing up."',
                '"No I\'m... Doesn\'t."',
                '"Shut up and take my money!"',
                '“You call that a wound? That\'s a boo-boo, tops.”',
                '“Wow! A superpowers drug you can rub on your skin? You think it would be something you\'d have to freebase.”',
                '"It\'s up to you to make your own decisions in life. That\'s what separates people and roclients from animals... and animal roclients."',]

        await ctx.send(f'```{random.choice(fry)}```')

# Generates a random quote from Professor Farnsworth.
    @commands.command()
    async def fp(self, ctx):
        await ctx.message.delete()

        professor = [ '"What an idiot I was! And by "I", I meant "you"!"',
                '"It\'s the Apocalypse all right. I always thought I\'d have a hand in it."',
                '"I must find a way to escape the horrible ravages of youth. Suddenly I\'m going to the bathroom every three hours like clockwork, and those jerks at Social Security stop sending me checks. Now I have to pay them."',
                '"Bad news, nobody! The supercollider super-exploded. I need you to take it back and exchange it for a wobbly CD rack and some of those rancid meatballs."',
                '"Good news, anyone! The Swedish roclient from pi-kea is here with the supercollider I ordered."',
                '"If anyone needs me I\'ll be in the Angry Dome."',
                '"A billion roclient lives are about to be extinguished. Oh, the Jedis are going to feel this one."',
                '"This is not a business. I always thought of it more as a cheap source of labor, like a family."',
                '"I still don\'t understand why you wouldn\'t let me graft a laser cannon on your chest, to crush those who disobey you! But I guess we\'re just two different people."',
                '"Dear God, they\'ll be killed on our doorstep! And there\'s no trash pickup until January 3rd."',
                '"To shreds, you say?"',
                '"And so we say goodbye to our beloved pet, Nibbler, who\'s gone to a place where I, too, hope one day to go. The toilet."',
                '"Oh, I always feared he might run off like this. Why, why, why didn\'t I break his legs?!"',
                '"I don\'t want to live on this planet anymore."',
                '"Everyone\'s always in favor of saving Hitler\'s brain, but when you put it in the body of a great white shark. Ohhh, suddenly you\'ve gone too far."',
                '"Remember, we\'ve got to show these people we\'re not bitter husks of human beings who long ago abandonded hope of finding love in this lifetime."',
                '"Good news, everyone!"',]

        await ctx.send(f'```{random.choice(professor)}```')

# Generates a random quote from Futurama.
    @commands.command()
    async def f(self, ctx):
        await ctx.message.delete()

        base = [ '"What an idiot I was! And by "I", I meant "you"!"',
                '"It\'s the Apocalypse all right. I always thought I\'d have a hand in it."',
                '"I must find a way to escape the horrible ravages of youth. Suddenly I\'m going to the bathroom every three hours like clockwork, and those jerks at Social Security stop sending me checks. Now I have to pay them."',
                '"Bad news, nobody! The supercollider super-exploded. I need you to take it back and exchange it for a wobbly CD rack and some of those rancid meatballs."',
                '"Good news, anyone! The Swedish roclient from pi-kea is here with the supercollider I ordered."',
                '"If anyone needs me I\'ll be in the Angry Dome."',
                '"A billion roclient lives are about to be extinguished. Oh, the Jedis are going to feel this one."',
                '"This is not a business. I always thought of it more as a cheap source of labor, like a family."',
                '"I still don\'t understand why you wouldn\'t let me graft a laser cannon on your chest, to crush those who disobey you! But I guess we\'re just two different people."',
                '"Dear God, they\'ll be killed on our doorstep! And there\'s no trash pickup until January 3rd."',
                '"To shreds, you say?"',
                '"And so we say goodbye to our beloved pet, Nibbler, who\'s gone to a place where I, too, hope one day to go. The toilet."',
                '"Oh, I always feared he might run off like this. Why, why, why didn\'t I break his legs?!"',
                '"I don\'t want to live on this planet anymore."',
                '"Everyone\'s always in favor of saving Hitler\'s brain, but when you put it in the body of a great white shark. Ohhh, suddenly you\'ve gone too far."',
                '"Remember, we\'ve got to show these people we\'re not bitter husks of human beings who long ago abandonded hope of finding love in this lifetime."',
                '"Good news, everyone!"',
                '"Wait, I\'m having one of those things, you know, a headache with pictures."',
                '"I am literally angry with rage!"',
                '"It\'s just like the story of the grasshopper and the octopus."',
                '"It\'s like a party in my mouth and everyone\'s throwing up."',
                '"No I\'m... Doesn\'t."',
                '"Shut up and take my money!"',
                '“You call that a wound? That\'s a boo-boo, tops.”',
                '“Wow! A superpowers drug you can rub on your skin? You think it would be something you\'d have to freebase.”',
                '"It\'s up to you to make your own decisions in life. That\'s what separates people and roclients from animals... and animal roclients."',
                '“We know nothing about them, their language, their history or what they look like. But we can assume this. They stand for everything we don’t stand for. Also they told me you guys look like dorks.”',
                '“Cham-paggin?”',
                '“The way to a woman’s bed is through her parents. Have sex with them and you’re in.”',
                '“She’s built like a steakhouse, but she handles like a bistro!”',
                '“I am the man with no name. Zapp Brannigan, at your service.”',
                '“Stop exploding you cowards!”',
                '“The spirit is willing, but the flesh is spongy and bruised.”',
                '“If we hit that bullseye, the rest of the dominoes will fall like a house of cards. Checkmate.”',
                '"It was almost the perfect crime, but you forgot one thing: Rock crushes scissors ... but paper covers rock ... and scissors cut paper. Kif, we have a conundrum. Search them for paper, and bring me a rock."',
                '"When I\'m in command, every mission is a suicide mission."',
                '"Call me cocky, but if there\'s an alien out there I can\'t kill I haven\'t met him and killed him yet."',
                '“Brannigan’s Law is like Brannigan’s love; hard and fast!”',
                '“Your face has been declared a weapon of mass disgusting!”',
                '“I want to slap your sister with a slice of bologna.”',
                '“Happy Freedom Day, ladies! Come on, show me something. Anything. Seriously, I’d take an armpit.”',
                '“In the game of chess, you can never let your adversary see your pieces.”',
                '“I’ve never heard of such a brutal and shocking injustice that I cared so little about!”',
                '"Bite my shiny metal ass!"',
                '"I’m so embarrassed. I wish everybody else was dead."',
                '"My story is a lot like yours, only more interesting ‘cause it involves roclients."',
                '"This is the worst kind of discrimination there is: the kind against me!"',
                '"Anything less than immortality is a complete waste of time."',
                '"How can I be so bad at everything I try, and still be so great?"',
                '"My life, and by extension everyone else\'s, is meaningless."',
                '"Of all the friends I\'ve had, you\'re the first."',
                '"I\'m going to build my own theme park! With blackjack! And hookers!"',
                '“I hope he didn’t die. Unless he left a note naming me his successor, then I hope he did die.”',
                '“Well, if jacking on will make strangers think I’m cool, I’ll do it.”',
                '“Have you ever tried simply turning off your TV, sitting down with your child, and hitting them?”',
                '“Hey sexy mama. Wanna kill all humans?”',
                '“Blackmail is such an ugly word. I prefer extortion. The ‘x’ makes it sound cool.”',
                '“Game’s over, losers! I have all the money. Compare your lives to mine and then kill yourselves.”',
                '“O’ cruel fate, to be thusly boned! Ask not for whom the bone bones—it bones for thee.”',
                '“Hey, whose been messing with my radio? This isn’t alternative rock, it’s college rock.”',
                '“Hahahahaha. Oh wait you’re serious. Let me laugh even harder.”',
                '“You know what cheers me up? Other people’s misfortune.”',
                '“Afterlife? If I thought I had to live another life, I’d kill myself right now!”']

        await ctx.send(f'```{random.choice(base)}```')

def setup(client):
    client.add_cog(futurama(client))
