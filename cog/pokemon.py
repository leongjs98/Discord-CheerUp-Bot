#PokéApi
import requests
import json
import random
from discord.ext import commands
from discord import Embed


class Pokemon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["poke"])
    async def pokemon(self, ctx, name=None, language="en"):
        """ Command: `.pokemon <name/Pokédex_number> <language>`\n
            Alt: `poke`\n
            If <name/Pokédex_number> is left out, a random pokemon is shown\n
            The default language is in English"""

        if name == None:
            # Search for a random Pokemon
            # only 898 Pokemon as of 10 Oct 2021
            random_pokemon = str(random.randint(1, 898))
            json_data = get_pokemon(random_pokemon)
        else:
            json_data = get_pokemon(name)

        name = json_data["name"].capitalize()
        if language != "en":
            language = get_language_iso(language.capitalize())
            language = language.lower()
            name_in_other_language = get_name_in_other_lan(str(json_data["id"]), language)
        else:
            name_in_other_language = ''

        image = json_data["sprites"]["front_default"]
        types = get_types(json_data)
        description = get_description(str(json_data["id"]), language)
        pokedex_num = format_pokedex_num(str(json_data["id"]))

        evolution_chain = get_evolution_chain(str(json_data["id"]))

        embed = Embed(title=name + name_in_other_language, description=description)

        embed.set_thumbnail(url=image)
        embed.add_field(name="Types", value=types)
        embed.add_field(name="Pokédex Number", value=pokedex_num)
        embed.add_field(name="Evolution Chain", value=evolution_chain, inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Pokemon(client))


def get_pokemon(query):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + query)
    json_data = json.loads(response.text)
    return json_data  # return the image link


def get_types(json_data):
    for i in range(len(json_data["types"])):
        if i == 0:
            types = json_data["types"][i]["type"]["name"].capitalize()
        else:
            types = types + ', ' + json_data["types"][i]["type"][
                "name"].capitalize()

    return types


def get_description(id, language):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/",id)
    json_data = json.loads(response.text)

    for i in json_data["flavor_text_entries"]:
        if language in i["language"]["name"]:
            return i["flavor_text"].replace("\n", ' ')


def format_pokedex_num(id):
    id_str = str(id)

    for i in range(3 - len(id_str)):
        id_str = '0' + id_str

    return '#' + id_str


def get_evolution_chain(id):
    # Get evolution chain url
    response_species = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/",id)
    json_species = json.loads(response_species.text)
    evolution_chain_url = json_species["evolution_chain"]["url"]
    
    response = requests.get(evolution_chain_url)
    json_data = json.loads(response.text)

    chain_ptr = json_data["chain"]
    chain = chain_ptr["species"]["name"].capitalize() # First 
    # If there is a next evolution
    while 1:
      if chain_ptr["evolves_to"]: # If there is a next evolution
        chain = chain + " -> "
        for i in range(len(chain_ptr["evolves_to"])):
          if i > 0:
            chain = chain + '/'
          chain = chain + chain_ptr["evolves_to"][i]["species"]["name"].capitalize()
        
        chain_ptr = chain_ptr["evolves_to"][i] # Points to the next in the chain
      else:
        break

    return chain


def get_name_in_other_lan(id, language):
    response_species = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/",id)

    json_names = json.loads(response_species.text)["names"]

    for i in json_names:
      if language in i["language"]["name"]:
        return ' (' + i["name"] + ')'


def get_language_iso(language):
  if language not in language_dict:
    return language
  else:
    return language_dict[language]


language_dict = {
  "Abkhazian": "ab",
  "Afar": "aa",
  "Afrikaans": "af",
  "Akan": "ak",
  "Albanian": "sq",
  "Amharic": "am",
  "Arabic": "ar",
  "Aragonese": "an",
  "Armenian": "hy",
  "Assamese": "as",
  "Avaric": "av",
  "Avestan": "ae",
  "Aymara": "ay",
  "Azerbaijani": "az",
  "Bambara": "bm",
  "Bashkir": "ba",
  "Basque": "eu",
  "Belarusian": "be",
  "Bengali (Bangla)": "bn",
  "Bihari": "bh",
  "Bislama": "bi",
  "Bosnian": "bs",
  "Breton": "br",
  "Bulgarian": "bg",
  "Burmese": "my",
  "Catalan": "ca",
  "Chamorro": "ch",
  "Chechen": "ce",
  "Chichewa": "ny",
  "Chinese": "zh",
  "Chinese (Simplified)": "zh-Hans",
  "Chinese (Traditional)": "zh-Hant",
  "Chuvash": "cv",
  "Cornish": "kw",
  "Corsican": "co",
  "Cree": "cr",
  "Croatian": "hr",
  "Czech": "cs",
  "Danish": "da",
  "Divehi": "dv",
  "Dutch": "nl",
  "Dzongkha": "dz",
  "English": "en",
  "Esperanto": "eo",
  "Estonian": "et",
  "Ewe": "ee",
  "Faroese": "fo",
  "Fijian": "fj",
  "Finnish": "fi",
  "French": "fr",
  "Fula": "ff",
  "Galician": "gl",
  "Gaelic (Scottish)": "gd",
  "Gaelic (Manx)": "gv",
  "Georgian": "ka",
  "German": "de",
  "Greek": "el",
  "Greenlandic": "kl",
  "Guarani": "gn",
  "Gujarati": "gu",
  "Haitian Creole": "ht",
  "Hausa": "ha",
  "Hebrew": "he",
  "Herero": "hz",
  "Hindi": "hi",
  "Hiri Motu": "ho",
  "Hungarian": "hu",
  "Icelandic": "is",
  "Ido": "io",
  "Igbo": "ig",
  "Indonesian": "id",
  "Interlingua": "ia",
  "Interlingue": "ie",
  "Inuktitut": "iu",
  "Inupiak": "ik",
  "Irish": "ga",
  "Italian": "it",
  "Japanese": "ja",
  "Javanese": "jv",
  "Kalaallisut": "kl",
  "Kannada": "kn",
  "Kanuri": "kr",
  "Kashmiri": "ks",
  "Kazakh": "kk",
  "Khmer": "km",
  "Kikuyu": "ki",
  "Kinyarwanda (Rwanda)": "rw",
  "Kirundi": "rn",
  "Kyrgyz": "ky",
  "Komi": "kv",
  "Kongo": "kg",
  "Korean": "ko",
  "Kurdish": "ku",
  "Kwanyama": "kj",
  "Lao": "lo",
  "Latin": "la",
  "Latvian (Lettish)": "lv",
  "Limburgish ( Limburger)": "li",
  "Lingala": "ln",
  "Lithuanian": "lt",
  "Luga-Katanga": "lu",
  "Luganda": "lg",
  "Luxembourgish": "lb",
  "Manx": "gv",
  "Macedonian": "mk",
  "Malagasy": "mg",
  "Malay": "ms",
  "Malayalam": "ml",
  "Maltese": "mt",
  "Maori": "mi",
  "Marathi": "mr",
  "Marshallese": "mh",
  "Moldavian": "mo",
  "Mongolian": "mn",
  "Nauru": "na",
  "Navajo": "nv",
  "Ndonga": "ng",
  "Northern Ndebele": "nd",
  "Nepali": "ne",
  "Norwegian": "no",
  "Norwegian bokmÃ¥l": "nb",
  "Norwegian nynorsk": "nn",
  "Nuosu": "ii",
  "Occitan": "oc",
  "Ojibwe": "oj",
  "Old Church Slavonic": "cu",
  "Oriya": "or",
  "Oromo (Afaan Oromo)": "om",
  "Ossetian": "os",
  "PÄli": "pi",
  "Pashto": "ps",
  "Persian (Farsi)": "fa",
  "Polish": "pl",
  "Portuguese": "pt",
  "Punjabi (Eastern)": "pa",
  "Quechua": "qu",
  "Romansh": "rm",
  "Romanian": "ro",
  "Russian": "ru",
  "Sami": "se",
  "Samoan": "sm",
  "Sango": "sg",
  "Sanskrit": "sa",
  "Serbian": "sr",
  "Serbo-Croatian": "sh",
  "Sesotho": "st",
  "Setswana": "tn",
  "Shona": "sn",
  "Sichuan Yi": "ii",
  "Sindhi": "sd",
  "Sinhalese": "si",
  "Siswati": "ss",
  "Slovak": "sk",
  "Slovenian": "sl",
  "Somali": "so",
  "Southern Ndebele": "nr",
  "Spanish": "es",
  "Sundanese": "su",
  "Swahili (Kiswahili)": "sw",
  "Swati": "ss",
  "Swedish": "sv",
  "Tagalog": "tl",
  "Tahitian": "ty",
  "Tajik": "tg",
  "Tamil": "ta",
  "Tatar": "tt",
  "Telugu": "te",
  "Thai": "th",
  "Tibetan": "bo",
  "Tigrinya": "ti",
  "Tonga": "to",
  "Tsonga": "ts",
  "Turkish": "tr",
  "Turkmen": "tk",
  "Twi": "tw",
  "Uyghur": "ug",
  "Ukrainian": "uk",
  "Urdu": "ur",
  "Uzbek": "uz",
  "Venda": "ve",
  "Vietnamese": "vi",
  "VolapÃ¼k": "vo",
  "Wallon": "wa",
  "Welsh": "cy",
  "Wolof": "wo",
  "Western Frisian": "fy",
  "Xhosa": "xh",
  "Yoruba": "yo",
  "Zhuang": "za",
  "Zulu": "zu"
}