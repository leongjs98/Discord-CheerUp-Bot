# CheerUp! Discord Bot

#### Video Demo:  https://youtu.be/M5cFbcEPT2g

#### Description:
The projects mainly rely on the library discord.py
In main.py. The bot 

According to the documentation of the library
> There comes a point in your bot’s development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that.
Cogs in discord bot python is a way to put a collection of commands into one class. This makes the organizing, changing and debugging the codes easier.

For better organization, seven cogs are used in this. There are:
1. 8ball.py
2. cat.py
3. dog.py
4. pokemon.py
5. joke.py
6. urban_dictionary.py
7. help.py

## 8ball.py
The 8ball.py makes a magic 8 ball command for the user. The user can use the command “.8ball” followed by a question. Then, a random question will be answered randomly with the responses list.

## cat.py
The cat.py allow user to call a random image of cats through an API using the command “.cat”. The API name is The Cat API. Also, if the user use “.cat 1” or “.cat true”, this will make the random_breed parameter True. Then, information of a cat breed will be shown followed by a larger thumbnail image. 

## dog.py
The dog.py allow user to call a random image of dogs through an API using the command “.dog”.

## joke.py
The joke.py allow the user to call a random joke through The Joke API via the command “.joke”. The user can choose a particular category. The category are described in the comments.

## pokemon.py
The pokemon.py allows the user to call information of a pokemon. The API chosen is the PokeAPI If only “.pokemon” is used, information of a random pokemon will be shown. If the Pokedex number or the name of the Pokemon is included (e.g. “.pokemon Charizard” or “.pokemon 6”), the chosen Pokemon will have their information displayed. The information displayed can be in different language using commands like “.pokemon 6 chinese”.

## help.py
Inside the help.py. It uses the exisitng helpcommand class to make custom help command for each of the command.

The whole project runs on the Replit platform. However, the bot will stop running after a certain amount of time. In order to let the bot stay online, UptimeRobot and keep_alive.py are used. UptimeRobot essentially keep pinging the discord bot and make it stay online.

The main.py makes the bot runs and has load, unload and reload cog extension in the cogs folders. Inside it, there are also a clear and ping command. Ping command (i.e. “.ping”) is for user to check how fast the bot response to the user. The clear command (i.e. “.clear”) lets the user delete an amount of messages within the channel they are in. The 
