# CheerUp! Discord Bot

#### Video Demo:  https://youtu.be/M5cFbcEPT2g

#### Description:
The projects mainly rely on the library discord.py

According to the documentation of the library
> There comes a point in your bot’s development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that.
Cogs in discord bot python is a way to put a collection of commands into one class. This makes the organizing, changing and debugging the codes easier. There are seven cogs used in this.
The 8ball.py makes a magic 8 ball command for the user. The user can use the command “.8ball” followed by a question. Then, a random question will be answered randomly with the responses list.

The cat.py allow user to call a random image of cats through an API using the command “.cat”. The API name is The Cat API. Also, if the user use “.cat 1” or “.cat true”, this will make the random_breed parameter True. Then, information of a cat breed will be shown followed by a larger thumbnail image. 
The dog.py allow user to call a random image of dogs through an API using the command “.dog”.
The joke.py allow the user to call a random joke through The Joke API via the command “.joke”. The user can choose a particular category. The category are described in the comments.
The pokemon.py allows the user to call information of a pokemon. The API chosen is the PokeAPI If only “.pokemon” is used, information of a random pokemon will be shown. If the Pokedex number or the name of the Pokemon is included (e.g. “.pokemon Charizard” or “.pokemon 6”), the chosen Pokemon will have their information displayed. The information displayed can be in different language using commands like “.pokemon 6 chinese”.
The keep_alive.py makes the bot stay online via constantly pinging the bot with UptimeRobot 
The main.py has makes the bot runs and has load, unload and reload cog extension in the cogs folders. Inside it, there are also a clear and ping command. Ping command (i.e. “.ping”) is for user to check how fast the bot response to the user. The clear command (i.e. “.clear”) lets the user delete an amount of messages within the channel they are in. The 
