# CheerUp! Discord Bot

#### Video Demo:  https://youtu.be/M5cFbcEPT2g

#### Description:
The projects mainly rely on the library discord.py (https://discordpy.readthedocs.io/en/stable/)

The main.py makes the bot runs and connect all the other commands together. It also allows load, unload and reload of all the commands except for ping and clear. These are for updating the command without restarting the bot entirely. Inside it, there are also a clear and ping command. Ping command (i.e. “.ping”) is for user to check how fast the bot response to the user. The clear command (i.e. “.clear”) lets the user delete an amount of messages within the channel they are in. The 

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
The 8ball.py makes a magic 8 ball command for the user. The user can use the command “.8ball” followed by a question. Then, a random question will be answered randomly (using the random library) with a pre-determined list of responses.

## cat.py
API: https://thecatapi.com/
The cat.py allow user to call a random image of cats through an API using the command “.cat”. Also, if the user use “.cat 1” or “.cat true”, this will make the random_breed parameter True. Then, information of a cat breed will be shown followed by a larger thumbnail image.

## dog.py
API: https://dog.ceo/dog-api/
The dog.py allow user to call a random image of dogs through an API using the command “.dog”.

## joke.py
API: https://jokeapi.dev/
The joke.py allow the user to call a random joke through The Joke API via the command “.joke”. The user can choose a particular category (.joke programming), a joke of the requested category will then be displayed. The categories are in the description and can be viewed with the function ".help joke".

## pokemon.py
API: https://pokeapi.co/
The pokemon.py allows the user to call information of a Pokémon. If only “.pokemon” is used, information of a random pokemon will be displayed. This is because the a Pokémon API can be search through the Pokédex number. After looking up online, there were 898 Pokémons, a random number generator is then used to generate a number between 1 to 898 and then used for the API call.

The API can also called via the name of the Pokémon. So, if the Pokédex number or the name of the Pokémon is included (e.g. “.pokemon Charizard” or “.pokemon 6”), the chosen Pokémon will have their information displayed. The information that is displayed will be the first one found with the language the user wanted.

The default language of the information is in English. The desciption and the Pokémon name will be displayed in different language using commands like “.pokemon 6 chinese”. Because the language name is in ISO code, the file contains a language dictionary to translate a language name into a language ISO code. The code then looks for the first description that has the requested language.

## urban_dictionary.py
API: https://rapidapi.com/community/api/urban-dictionary
This uses an official API of Urban Dictionary. The API finds multiple definition on the site. Then, the code find the most liked definition acquired from the API and embed it into a message.

## help.py
Inside the help.py. It subclasses the exisitng HelpCommand class to make custom help command for each of the command.

The whole project runs on the Replit platform. However, the bot will stop running after a certain amount of time. In order to let the bot stay online, UptimeRobot and keep_alive.py are used. UptimeRobot essentially keep pinging the discord bot and make it stay online.
