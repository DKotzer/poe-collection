from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
import requests
# from currency import currencyDetails
# from book_list import book_list
book_list =[
  {
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "year": 1958,
  },
  {
    "author": "Hans Christian Andersen",
    "country": "Denmark",
    "imageLink": "images/fairy-tales.jpg",
    "language": "Danish",
    "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
    "pages": 784,
    "title": "Fairy tales",
    "year": 1836
  },
  {
    "author": "Dante Alighieri",
    "country": "Italy",
    "imageLink": "images/the-divine-comedy.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
    "pages": 928,
    "title": "The Divine Comedy",
    "year": 1315
  },
  {
    "author": "Unknown",
    "country": "Sumer and Akkadian Empire",
    "imageLink": "images/the-epic-of-gilgamesh.jpg",
    "language": "Akkadian",
    "link": "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh\n",
    "pages": 160,
    "title": "The Epic Of Gilgamesh",
    "year": -1700
  },
  {
    "author": "Unknown",
    "country": "Achaemenid Empire",
    "imageLink": "images/the-book-of-job.jpg",
    "language": "Hebrew",
    "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
    "pages": 176,
    "title": "The Book Of Job",
    "year": -600
  },
  {
    "author": "Unknown",
    "country": "India/Iran/Iraq/Egypt/Tajikistan",
    "imageLink": "images/one-thousand-and-one-nights.jpg",
    "language": "Arabic",
    "link": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights\n",
    "pages": 288,
    "title": "One Thousand and One Nights",
    "year": 1200
  },
  {
    "author": "Unknown",
    "country": "Iceland",
    "imageLink": "images/njals-saga.jpg",
    "language": "Old Norse",
    "link": "https://en.wikipedia.org/wiki/Nj%C3%A1ls_saga\n",
    "pages": 384,
    "title": "Nj\u00e1l's Saga",
    "year": 1350
  },
  {
    "author": "Jane Austen",
    "country": "United Kingdom",
    "imageLink": "images/pride-and-prejudice.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
    "pages": 226,
    "title": "Pride and Prejudice",
    "year": 1813
  },
  {
    "author": "Honor\u00e9 de Balzac",
    "country": "France",
    "imageLink": "images/le-pere-goriot.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Le_P%C3%A8re_Goriot\n",
    "pages": 443,
    "title": "Le P\u00e8re Goriot",
    "year": 1835
  },
  {
    "author": "Samuel Beckett",
    "country": "Republic of Ireland",
    "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
    "language": "French, English",
    "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
    "pages": 256,
    "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
    "year": 1952
  },
  {
    "author": "Giovanni Boccaccio",
    "country": "Italy",
    "imageLink": "images/the-decameron.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/The_Decameron\n",
    "pages": 1024,
    "title": "The Decameron",
    "year": 1351
  },
  {
    "author": "Jorge Luis Borges",
    "country": "Argentina",
    "imageLink": "images/ficciones.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/Ficciones\n",
    "pages": 224,
    "title": "Ficciones",
    "year": 1965
  },
  {
    "author": "Emily Bront\u00eb",
    "country": "United Kingdom",
    "imageLink": "images/wuthering-heights.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Wuthering_Heights\n",
    "pages": 342,
    "title": "Wuthering Heights",
    "year": 1847
  },
  {
    "author": "Albert Camus",
    "country": "Algeria, French Empire",
    "imageLink": "images/l-etranger.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/The_Stranger_(novel)\n",
    "pages": 185,
    "title": "The Stranger",
    "year": 1942
  },
  {
    "author": "Paul Celan",
    "country": "Romania, France",
    "imageLink": "images/poems-paul-celan.jpg",
    "language": "German",
    "link": "\n",
    "pages": 320,
    "title": "Poems",
    "year": 1952
  },
  {
    "author": "Louis-Ferdinand C\u00e9line",
    "country": "France",
    "imageLink": "images/voyage-au-bout-de-la-nuit.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Journey_to_the_End_of_the_Night\n",
    "pages": 505,
    "title": "Journey to the End of the Night",
    "year": 1932
  },
  {
    "author": "Miguel de Cervantes",
    "country": "Spain",
    "imageLink": "images/don-quijote-de-la-mancha.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/Don_Quixote\n",
    "pages": 1056,
    "title": "Don Quijote De La Mancha",
    "year": 1610
  },
  {
    "author": "Geoffrey Chaucer",
    "country": "England",
    "imageLink": "images/the-canterbury-tales.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/The_Canterbury_Tales\n",
    "pages": 544,
    "title": "The Canterbury Tales",
    "year": 1450
  },
  {
    "author": "Anton Chekhov",
    "country": "Russia",
    "imageLink": "images/stories-of-anton-chekhov.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/List_of_short_stories_by_Anton_Chekhov\n",
    "pages": 194,
    "title": "Stories",
    "year": 1886
  },
  {
    "author": "Joseph Conrad",
    "country": "United Kingdom",
    "imageLink": "images/nostromo.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Nostromo\n",
    "pages": 320,
    "title": "Nostromo",
    "year": 1904
  },
  {
    "author": "Charles Dickens",
    "country": "United Kingdom",
    "imageLink": "images/great-expectations.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Great_Expectations\n",
    "pages": 194,
    "title": "Great Expectations",
    "year": 1861
  },
  {
    "author": "Denis Diderot",
    "country": "France",
    "imageLink": "images/jacques-the-fatalist.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Jacques_the_Fatalist\n",
    "pages": 596,
    "title": "Jacques the Fatalist",
    "year": 1796
  },
  {
    "author": "Alfred D\u00f6blin",
    "country": "Germany",
    "imageLink": "images/berlin-alexanderplatz.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/Berlin_Alexanderplatz\n",
    "pages": 600,
    "title": "Berlin Alexanderplatz",
    "year": 1929
  },
  {
    "author": "Fyodor Dostoevsky",
    "country": "Russia",
    "imageLink": "images/crime-and-punishment.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/Crime_and_Punishment\n",
    "pages": 551,
    "title": "Crime and Punishment",
    "year": 1866
  },
  {
    "author": "Fyodor Dostoevsky",
    "country": "Russia",
    "imageLink": "images/the-idiot.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/The_Idiot\n",
    "pages": 656,
    "title": "The Idiot",
    "year": 1869
  },
  {
    "author": "Fyodor Dostoevsky",
    "country": "Russia",
    "imageLink": "images/the-possessed.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/Demons_(Dostoyevsky_novel)\n",
    "pages": 768,
    "title": "The Possessed",
    "year": 1872
  },
  {
    "author": "Fyodor Dostoevsky",
    "country": "Russia",
    "imageLink": "images/the-brothers-karamazov.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/The_Brothers_Karamazov\n",
    "pages": 824,
    "title": "The Brothers Karamazov",
    "year": 1880
  },
  {
    "author": "George Eliot",
    "country": "United Kingdom",
    "imageLink": "images/middlemarch.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Middlemarch\n",
    "pages": 800,
    "title": "Middlemarch",
    "year": 1871
  },
  {
    "author": "Ralph Ellison",
    "country": "United States",
    "imageLink": "images/invisible-man.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Invisible_Man\n",
    "pages": 581,
    "title": "Invisible Man",
    "year": 1952
  },
  {
    "author": "Euripides",
    "country": "Greece",
    "imageLink": "images/medea.jpg",
    "language": "Greek",
    "link": "https://en.wikipedia.org/wiki/Medea_(play)\n",
    "pages": 104,
    "title": "Medea",
    "year": -431
  },
  {
    "author": "William Faulkner",
    "country": "United States",
    "imageLink": "images/absalom-absalom.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Absalom,_Absalom!\n",
    "pages": 313,
    "title": "Absalom, Absalom!",
    "year": 1936
  },
  {
    "author": "William Faulkner",
    "country": "United States",
    "imageLink": "images/the-sound-and-the-fury.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/The_Sound_and_the_Fury\n",
    "pages": 326,
    "title": "The Sound and the Fury",
    "year": 1929
  },
  {
    "author": "Gustave Flaubert",
    "country": "France",
    "imageLink": "images/madame-bovary.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Madame_Bovary\n",
    "pages": 528,
    "title": "Madame Bovary",
    "year": 1857
  },
  {
    "author": "Gustave Flaubert",
    "country": "France",
    "imageLink": "images/l-education-sentimentale.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Sentimental_Education\n",
    "pages": 606,
    "title": "Sentimental Education",
    "year": 1869
  },
  {
    "author": "Federico Garc\u00eda Lorca",
    "country": "Spain",
    "imageLink": "images/gypsy-ballads.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/Gypsy_Ballads\n",
    "pages": 218,
    "title": "Gypsy Ballads",
    "year": 1928
  },
  {
    "author": "Gabriel Garc\u00eda M\u00e1rquez",
    "country": "Colombia",
    "imageLink": "images/one-hundred-years-of-solitude.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/One_Hundred_Years_of_Solitude\n",
    "pages": 417,
    "title": "One Hundred Years of Solitude",
    "year": 1967
  },
  {
    "author": "Gabriel Garc\u00eda M\u00e1rquez",
    "country": "Colombia",
    "imageLink": "images/love-in-the-time-of-cholera.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/Love_in_the_Time_of_Cholera\n",
    "pages": 368,
    "title": "Love in the Time of Cholera",
    "year": 1985
  },
  {
    "author": "Johann Wolfgang von Goethe",
    "country": "Saxe-Weimar",
    "imageLink": "images/faust.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/Goethe%27s_Faust\n",
    "pages": 158,
    "title": "Faust",
    "year": 1832
  },
  {
    "author": "Nikolai Gogol",
    "country": "Russia",
    "imageLink": "images/dead-souls.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/Dead_Souls\n",
    "pages": 432,
    "title": "Dead Souls",
    "year": 1842
  },
  {
    "author": "G\u00fcnter Grass",
    "country": "Germany",
    "imageLink": "images/the-tin-drum.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/The_Tin_Drum\n",
    "pages": 600,
    "title": "The Tin Drum",
    "year": 1959
  },
  {
    "author": "Jo\u00e3o Guimar\u00e3es Rosa",
    "country": "Brazil",
    "imageLink": "images/the-devil-to-pay-in-the-backlands.jpg",
    "language": "Portuguese",
    "link": "https://en.wikipedia.org/wiki/The_Devil_to_Pay_in_the_Backlands\n",
    "pages": 494,
    "title": "The Devil to Pay in the Backlands",
    "year": 1956
  },
  {
    "author": "Knut Hamsun",
    "country": "Norway",
    "imageLink": "images/hunger.jpg",
    "language": "Norwegian",
    "link": "https://en.wikipedia.org/wiki/Hunger_(Hamsun_novel)\n",
    "pages": 176,
    "title": "Hunger",
    "year": 1890
  },
  {
    "author": "Ernest Hemingway",
    "country": "United States",
    "imageLink": "images/the-old-man-and-the-sea.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/The_Old_Man_and_the_Sea\n",
    "pages": 128,
    "title": "The Old Man and the Sea",
    "year": 1952
  },
  {
    "author": "Homer",
    "country": "Greece",
    "imageLink": "images/the-iliad-of-homer.jpg",
    "language": "Greek",
    "link": "https://en.wikipedia.org/wiki/Iliad\n",
    "pages": 608,
    "title": "Iliad",
    "year": -735
  },
  {
    "author": "Homer",
    "country": "Greece",
    "imageLink": "images/the-odyssey-of-homer.jpg",
    "language": "Greek",
    "link": "https://en.wikipedia.org/wiki/Odyssey\n",
    "pages": 374,
    "title": "Odyssey",
    "year": -800
  },
  {
    "author": "Henrik Ibsen",
    "country": "Norway",
    "imageLink": "images/a-Dolls-house.jpg",
    "language": "Norwegian",
    "link": "https://en.wikipedia.org/wiki/A_Doll%27s_House\n",
    "pages": 68,
    "title": "A Doll's House",
    "year": 1879
  },
  {
    "author": "James Joyce",
    "country": "Irish Free State",
    "imageLink": "images/ulysses.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Ulysses_(novel)\n",
    "pages": 228,
    "title": "Ulysses",
    "year": 1922
  },
  {
    "author": "Franz Kafka",
    "country": "Czechoslovakia",
    "imageLink": "images/stories-of-franz-kafka.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/Franz_Kafka_bibliography#Short_stories\n",
    "pages": 488,
    "title": "Stories",
    "year": 1924
  },
  {
    "author": "Franz Kafka",
    "country": "Czechoslovakia",
    "imageLink": "images/the-trial.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/The_Trial\n",
    "pages": 160,
    "title": "The Trial",
    "year": 1925
  },
  {
    "author": "Franz Kafka",
    "country": "Czechoslovakia",
    "imageLink": "images/the-castle.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/The_Castle_(novel)\n",
    "pages": 352,
    "title": "The Castle",
    "year": 1926
  },
  {
    "author": "K\u0101lid\u0101sa",
    "country": "India",
    "imageLink": "images/the-recognition-of-shakuntala.jpg",
    "language": "Sanskrit",
    "link": "https://en.wikipedia.org/wiki/Abhij%C3%B1%C4%81na%C5%9B%C4%81kuntalam\n",
    "pages": 147,
    "title": "The recognition of Shakuntala",
    "year": 150
  },
  {
    "author": "Yasunari Kawabata",
    "country": "Japan",
    "imageLink": "images/the-sound-of-the-mountain.jpg",
    "language": "Japanese",
    "link": "https://en.wikipedia.org/wiki/The_Sound_of_the_Mountain\n",
    "pages": 288,
    "title": "The Sound of the Mountain",
    "year": 1954
  },
  {
    "author": "Nikos Kazantzakis",
    "country": "Greece",
    "imageLink": "images/zorba-the-greek.jpg",
    "language": "Greek",
    "link": "https://en.wikipedia.org/wiki/Zorba_the_Greek\n",
    "pages": 368,
    "title": "Zorba the Greek",
    "year": 1946
  },
  {
    "author": "D. H. Lawrence",
    "country": "United Kingdom",
    "imageLink": "images/sons-and-lovers.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Sons_and_Lovers\n",
    "pages": 432,
    "title": "Sons and Lovers",
    "year": 1913
  },
  {
    "author": "Halld\u00f3r Laxness",
    "country": "Iceland",
    "imageLink": "images/independent-people.jpg",
    "language": "Icelandic",
    "link": "https://en.wikipedia.org/wiki/Independent_People\n",
    "pages": 470,
    "title": "Independent People",
    "year": 1934
  },
  {
    "author": "Giacomo Leopardi",
    "country": "Italy",
    "imageLink": "images/poems-giacomo-leopardi.jpg",
    "language": "Italian",
    "link": "\n",
    "pages": 184,
    "title": "Poems",
    "year": 1818
  },
  {
    "author": "Doris Lessing",
    "country": "United Kingdom",
    "imageLink": "images/the-golden-notebook.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/The_Golden_Notebook\n",
    "pages": 688,
    "title": "The Golden Notebook",
    "year": 1962
  },
  {
    "author": "Astrid Lindgren",
    "country": "Sweden",
    "imageLink": "images/pippi-longstocking.jpg",
    "language": "Swedish",
    "link": "https://en.wikipedia.org/wiki/Pippi_Longstocking\n",
    "pages": 160,
    "title": "Pippi Longstocking",
    "year": 1945
  },
  {
    "author": "Lu Xun",
    "country": "China",
    "imageLink": "images/diary-of-a-madman.jpg",
    "language": "Chinese",
    "link": "https://en.wikipedia.org/wiki/A_Madman%27s_Diary\n",
    "pages": 389,
    "title": "Diary of a Madman",
    "year": 1918
  },
  {
    "author": "Naguib Mahfouz",
    "country": "Egypt",
    "imageLink": "images/children-of-gebelawi.jpg",
    "language": "Arabic",
    "link": "https://en.wikipedia.org/wiki/Children_of_Gebelawi\n",
    "pages": 355,
    "title": "Children of Gebelawi",
    "year": 1959
  },
  {
    "author": "Thomas Mann",
    "country": "Germany",
    "imageLink": "images/buddenbrooks.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/Buddenbrooks\n",
    "pages": 736,
    "title": "Buddenbrooks",
    "year": 1901
  },
  {
    "author": "Thomas Mann",
    "country": "Germany",
    "imageLink": "images/the-magic-mountain.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/The_Magic_Mountain\n",
    "pages": 720,
    "title": "The Magic Mountain",
    "year": 1924
  },
  {
    "author": "Herman Melville",
    "country": "United States",
    "imageLink": "images/moby-dick.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Moby-Dick\n",
    "pages": 378,
    "title": "Moby Dick",
    "year": 1851
  },
  {
    "author": "Michel de Montaigne",
    "country": "France",
    "imageLink": "images/essais.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Essays_(Montaigne)\n",
    "pages": 404,
    "title": "Essays",
    "year": 1595
  },
  {
    "author": "Elsa Morante",
    "country": "Italy",
    "imageLink": "images/history.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/History_(novel)\n",
    "pages": 600,
    "title": "History",
    "year": 1974
  },
  {
    "author": "Toni Morrison",
    "country": "United States",
    "imageLink": "images/beloved.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Beloved_(novel)\n",
    "pages": 321,
    "title": "Beloved",
    "year": 1987
  },
  {
    "author": "Murasaki Shikibu",
    "country": "Japan",
    "imageLink": "images/the-tale-of-genji.jpg",
    "language": "Japanese",
    "link": "https://en.wikipedia.org/wiki/The_Tale_of_Genji\n",
    "pages": 1360,
    "title": "The Tale of Genji",
    "year": 1006
  },
  {
    "author": "Robert Musil",
    "country": "Austria",
    "imageLink": "images/the-man-without-qualities.jpg",
    "language": "German",
    "link": "https://en.wikipedia.org/wiki/The_Man_Without_Qualities\n",
    "pages": 365,
    "title": "The Man Without Qualities",
    "year": 1931
  },
  {
    "author": "Vladimir Nabokov",
    "country": "Russia/United States",
    "imageLink": "images/lolita.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Lolita\n",
    "pages": 317,
    "title": "Lolita",
    "year": 1955
  },
  {
    "author": "George Orwell",
    "country": "United Kingdom",
    "imageLink": "images/nineteen-eighty-four.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Nineteen_Eighty-Four\n",
    "pages": 272,
    "title": "Nineteen Eighty-Four",
    "year": 1949
  },
  {
    "author": "Ovid",
    "country": "Roman Empire",
    "imageLink": "images/the-metamorphoses-of-ovid.jpg",
    "language": "Classical Latin",
    "link": "https://en.wikipedia.org/wiki/Metamorphoses\n",
    "pages": 576,
    "title": "Metamorphoses",
    "year": 100
  },
  {
    "author": "Fernando Pessoa",
    "country": "Portugal",
    "imageLink": "images/the-book-of-disquiet.jpg",
    "language": "Portuguese",
    "link": "https://en.wikipedia.org/wiki/The_Book_of_Disquiet\n",
    "pages": 272,
    "title": "The Book of Disquiet",
    "year": 1928
  },
  {
    "author": "Edgar Allan Poe",
    "country": "United States",
    "imageLink": "images/tales-and-poems-of-edgar-allan-poe.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Edgar_Allan_Poe_bibliography#Tales\n",
    "pages": 842,
    "title": "Tales",
    "year": 1950
  },
  {
    "author": "Marcel Proust",
    "country": "France",
    "imageLink": "images/a-la-recherche-du-temps-perdu.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/In_Search_of_Lost_Time\n",
    "pages": 2408,
    "title": "In Search of Lost Time",
    "year": 1920
  },
  {
    "author": "Fran\u00e7ois Rabelais",
    "country": "France",
    "imageLink": "images/gargantua-and-pantagruel.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Gargantua_and_Pantagruel\n",
    "pages": 623,
    "title": "Gargantua and Pantagruel",
    "year": 1533
  },
  {
    "author": "Juan Rulfo",
    "country": "Mexico",
    "imageLink": "images/pedro-paramo.jpg",
    "language": "Spanish",
    "link": "https://en.wikipedia.org/wiki/Pedro_P%C3%A1ramo\n",
    "pages": 124,
    "title": "Pedro P\u00e1ramo",
    "year": 1955
  },
  {
    "author": "Rumi",
    "country": "Sultanate of Rum",
    "imageLink": "images/the-masnavi.jpg",
    "language": "Persian",
    "link": "https://en.wikipedia.org/wiki/Masnavi\n",
    "pages": 438,
    "title": "The Masnavi",
    "year": 1236
  },
  {
    "author": "Salman Rushdie",
    "country": "United Kingdom, India",
    "imageLink": "images/midnights-children.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Midnight%27s_Children\n",
    "pages": 536,
    "title": "Midnight's Children",
    "year": 1981
  },
  {
    "author": "Saadi",
    "country": "Persia, Persian Empire",
    "imageLink": "images/bostan.jpg",
    "language": "Persian",
    "link": "https://en.wikipedia.org/wiki/Bustan_(book)\n",
    "pages": 298,
    "title": "Bostan",
    "year": 1257
  },
  {
    "author": "Tayeb Salih",
    "country": "Sudan",
    "imageLink": "images/season-of-migration-to-the-north.jpg",
    "language": "Arabic",
    "link": "https://en.wikipedia.org/wiki/Season_of_Migration_to_the_North\n",
    "pages": 139,
    "title": "Season of Migration to the North",
    "year": 1966
  },
  {
    "author": "Jos\u00e9 Saramago",
    "country": "Portugal",
    "imageLink": "images/blindness.jpg",
    "language": "Portuguese",
    "link": "https://en.wikipedia.org/wiki/Blindness_(novel)\n",
    "pages": 352,
    "title": "Blindness",
    "year": 1995
  },
  {
    "author": "William Shakespeare",
    "country": "England",
    "imageLink": "images/hamlet.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Hamlet\n",
    "pages": 432,
    "title": "Hamlet",
    "year": 1603
  },
  {
    "author": "William Shakespeare",
    "country": "England",
    "imageLink": "images/king-lear.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/King_Lear\n",
    "pages": 384,
    "title": "King Lear",
    "year": 1608
  },
  {
    "author": "William Shakespeare",
    "country": "England",
    "imageLink": "images/othello.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Othello\n",
    "pages": 314,
    "title": "Othello",
    "year": 1609
  },
  {
    "author": "Sophocles",
    "country": "Greece",
    "imageLink": "images/oedipus-the-king.jpg",
    "language": "Greek",
    "link": "https://en.wikipedia.org/wiki/Oedipus_the_King\n",
    "pages": 88,
    "title": "Oedipus the King",
    "year": -430
  },
  {
    "author": "Stendhal",
    "country": "France",
    "imageLink": "images/le-rouge-et-le-noir.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/The_Red_and_the_Black\n",
    "pages": 576,
    "title": "The Red and the Black",
    "year": 1830
  },
  {
    "author": "Laurence Sterne",
    "country": "England",
    "imageLink": "images/the-life-and-opinions-of-tristram-shandy.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/The_Life_and_Opinions_of_Tristram_Shandy,_Gentleman\n",
    "pages": 640,
    "title": "The Life And Opinions of Tristram Shandy",
    "year": 1760
  },
  {
    "author": "Italo Svevo",
    "country": "Italy",
    "imageLink": "images/confessions-of-zeno.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/Zeno%27s_Conscience\n",
    "pages": 412,
    "title": "Confessions of Zeno",
    "year": 1923
  },
  {
    "author": "Jonathan Swift",
    "country": "Ireland",
    "imageLink": "images/gullivers-travels.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Gulliver%27s_Travels\n",
    "pages": 178,
    "title": "Gulliver's Travels",
    "year": 1726
  },
  {
    "author": "Leo Tolstoy",
    "country": "Russia",
    "imageLink": "images/war-and-peace.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/War_and_Peace\n",
    "pages": 1296,
    "title": "War and Peace",
    "year": 1867
  },
  {
    "author": "Leo Tolstoy",
    "country": "Russia",
    "imageLink": "images/anna-karenina.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/Anna_Karenina\n",
    "pages": 864,
    "title": "Anna Karenina",
    "year": 1877
  },
  {
    "author": "Leo Tolstoy",
    "country": "Russia",
    "imageLink": "images/the-death-of-ivan-ilyich.jpg",
    "language": "Russian",
    "link": "https://en.wikipedia.org/wiki/The_Death_of_Ivan_Ilyich\n",
    "pages": 92,
    "title": "The Death of Ivan Ilyich",
    "year": 1886
  },
  {
    "author": "Mark Twain",
    "country": "United States",
    "imageLink": "images/the-adventures-of-huckleberry-finn.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Adventures_of_Huckleberry_Finn\n",
    "pages": 224,
    "title": "The Adventures of Huckleberry Finn",
    "year": 1884
  },
  {
    "author": "Valmiki",
    "country": "India",
    "imageLink": "images/ramayana.jpg",
    "language": "Sanskrit",
    "link": "https://en.wikipedia.org/wiki/Ramayana\n",
    "pages": 152,
    "title": "Ramayana",
    "year": -450
  },
  {
    "author": "Virgil",
    "country": "Roman Empire",
    "imageLink": "images/the-aeneid.jpg",
    "language": "Classical Latin",
    "link": "https://en.wikipedia.org/wiki/Aeneid\n",
    "pages": 442,
    "title": "The Aeneid",
    "year": -23
  },
  {
    "author": "Vyasa",
    "country": "India",
    "imageLink": "images/the-mahab-harata.jpg",
    "language": "Sanskrit",
    "link": "https://en.wikipedia.org/wiki/Mahabharata\n",
    "pages": 276,
    "title": "Mahabharata",
    "year": -700
  },
  {
    "author": "Walt Whitman",
    "country": "United States",
    "imageLink": "images/leaves-of-grass.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Leaves_of_Grass\n",
    "pages": 152,
    "title": "Leaves of Grass",
    "year": 1855
  },
  {
    "author": "Virginia Woolf",
    "country": "United Kingdom",
    "imageLink": "images/mrs-dalloway.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Mrs_Dalloway\n",
    "pages": 216,
    "title": "Mrs Dalloway",
    "year": 1925
  },
  {
    "author": "Virginia Woolf",
    "country": "United Kingdom",
    "imageLink": "images/to-the-lighthouse.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/To_the_Lighthouse\n",
    "pages": 209,
    "title": "To the Lighthouse",
    "year": 1927
  },
  {
    "author": "Marguerite Yourcenar",
    "country": "France/Belgium",
    "imageLink": "images/memoirs-of-hadrian.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Memoirs_of_Hadrian\n",
    "pages": 408,
    "title": "Memoirs of Hadrian",
    "year": 1951
  }
]



new_book_list = sorted(book_list, key=lambda k: k['year'])



# Create your views here.

def home(request):
    return render(request,'items/index.html', {'books': new_book_list})

def about(request):
    return render(request,'about.html')

def items(request):
    return render(request,'items/index.html', {'books': new_book_list})





# -------------------------------------------- Weapons list Below
###
#
#
##
#
weapon_list = [
{
    "id": 52216,
    "name": "Demigod's Authority",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9PbmVIYW5kV2VhcG9ucy9PbmVIYW5kU3dvcmRzL0RlbWlnb2RzQXV0aG9yaXR5IiwidyI6MiwiaCI6Mywic2NhbGUiOjF9XQ/be10fa5951/DemigodsAuthority.png",
    "baseType": "Golden Blade",
    "itemClass": 3,
    "sparkline": {
    "data": [
        0,
        0.22,
        -2.06,
        None,
        None,
        None,
        None
    ],
    "totalChange": -2.06
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        0.22,
        -2.06,
        33.67,
        17.85,
        86.11,
        64.92
    ],
    "totalChange": 64.92
    },
    "implicitModifiers": [
    {
        "text": "+(16-24) to all Attributes",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "You and Nearby Allies have 30% increased Item Rarity",
        "optional": False
    },
    {
        "text": "5% increased Character Size",
        "optional": False
    }
    ],
    "flavourText": "Mayhem HC #4 Juggernaut",
    "itemType": "One Handed Sword",
    "chaosValue": 62415.96,
    "exaltedValue": 356.52,
    "count": 4,
    "detailsId": "demigods-authority-golden-blade",
    "listingCount": 21
},
{
    "id": 2244,
    "name": "The Enmity Divine",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvUmFnZSBTdGFmZiIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/7c95713fe7/Rage%20Staff.png",
    "levelRequired": 66,
    "baseType": "Imperial Staff",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [],
    "totalChange": 0
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        2.02,
        -11.68,
        -10.91,
        -10.35,
        -10.15,
        -10.14
    ],
    "totalChange": -10.14
    },
    "implicitModifiers": [
    {
        "text": "+18% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "Socketed Gems are supported by Level 1 Chance to Bleed",
        "optional": False
    },
    {
        "text": "Grants Summon Harbinger of Brutality Skill",
        "optional": False
    },
    {
        "text": "+5% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    },
    {
        "text": "+(30-40)% to Damage over Time Multiplier for Bleeding from Critical Strikes",
        "optional": False
    },
    {
        "text": "Adds (161-184) to (210-225) Physical Damage",
        "optional": False
    },
    {
        "text": "(32-40)% increased Critical Strike Chance",
        "optional": False
    }
    ],
    "flavourText": "Grants Summon Harbinger of Brutality Skill: Summons an immortal Harbinger minion. The minion will occasionally grant the player significantly increased damage, attack speed, movement speed, and reduced damage taken.",
    "itemType": "Staff",
    "chaosValue": 1050.42,
    "exaltedValue": 6,
    "count": 3,
    "detailsId": "the-enmity-divine-imperial-staff-6l",
    "listingCount": 4
},
{
    "id": 1899,
    "name": "Xirgil's Crank",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvU3RhZmY3dW5pcXVlIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/2437d7498a/Staff7unique.png",
    "levelRequired": 28,
    "baseType": "Coiled Staff",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [],
    "totalChange": 0
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        2.02,
        2.9,
        3.9,
        4.57,
        4.79,
        4.79
    ],
    "totalChange": 4.79
    },
    "implicitModifiers": [
    {
        "text": "+20% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "+15% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    },
    {
        "text": "(66-79)% increased Spell Damage",
        "optional": False
    },
    {
        "text": "+(77-91) to maximum Energy Shield",
        "optional": False
    },
    {
        "text": "+1 to Level of all Spell Skill Gems",
        "optional": False
    },
    {
        "text": "Reflects 1 to 150 Lightning Damage to Melee Attackers",
        "optional": False
    },
    {
        "text": "20% chance for Energy Shield Recharge to start when you Block",
        "optional": False
    }
    ],
    "flavourText": "\"Since one with knowledge of machines\nmight be able to bring the labyrinth to a standstill, \nIzaro had us place many boobytrapped decoys.\nBut I know which switch brings the monster down.\"\n- Xirgil, Trapbuilder's final words.",
    "itemType": "Staff",
    "chaosValue": 875.35,
    "exaltedValue": 5,
    "count": 2,
    "detailsId": "xirgils-crank-coiled-staff-6l",
    "listingCount": 3
},
{
    "id": 2028,
    "name": "Uul-Netol's Embrace",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kQXhlcy9VdWxOZXRvbHNLaXNzVXBncmFkZWQiLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MX1d/8c4738c8a9/UulNetolsKissUpgraded.png",
    "levelRequired": 64,
    "baseType": "Vaal Axe",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [],
    "totalChange": 0
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        1.9,
        2.79,
        3.81,
        -3.83,
        -3.69,
        -3.69
    ],
    "totalChange": -3.69
    },
    "implicitModifiers": [
    {
        "text": "25% chance to Maim on Hit",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "Trigger Level 20 Bone Nova when you Hit a Bleeding Enemy",
        "optional": False
    },
    {
        "text": "(282-314)% increased Physical Damage",
        "optional": False
    },
    {
        "text": "(25-28)% reduced Attack Speed",
        "optional": False
    },
    {
        "text": "Attacks have 25% chance to inflict Bleeding when Hitting Cursed Enemies",
        "optional": False
    }
    ],
    "flavourText": "At last she holds us,\nand so we turn to dust.",
    "itemType": "Two Handed Axe",
    "chaosValue": 805.23,
    "exaltedValue": 4.6,
    "count": 3,
    "detailsId": "uul-netols-embrace-vaal-axe-6l",
    "listingCount": 4
},
{
    "id": 1913,
    "name": "Kingmaker",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kQXhlcy9BbGV4YXhlYW5kaGVhcnRicmVha2VyIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/fb47351eee/Alexaxeandheartbreaker.png",
    "levelRequired": 66,
    "baseType": "Despot Axe",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [
        0,
        -19.78,
        -5.89,
        -5.45,
        -5.2,
        -17.77,
        -17.77
    ],
    "totalChange": -17.77
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        -19.78,
        -5.89,
        -5.45,
        -5.2,
        -17.77,
        -17.77
    ],
    "totalChange": -17.77
    },
    "implicitModifiers": [],
    "explicitModifiers": [
    {
        "text": "(191-240)% increased Physical Damage",
        "optional": False
    },
    {
        "text": "(7-12)% increased Attack Speed",
        "optional": False
    },
    {
        "text": "(30-40)% increased Critical Strike Chance",
        "optional": False
    },
    {
        "text": "Nearby Allies have 30% increased Item Rarity",
        "optional": False
    },
    {
        "text": "Nearby Allies have Culling Strike",
        "optional": False
    },
    {
        "text": "Insufficient Mana doesn't prevent your Melee Attacks",
        "optional": False
    },
    {
        "text": "Nearby Allies have +50% to Critical Strike Multiplier",
        "optional": False
    },
    {
        "text": "Nearby Allies have +10 Fortification",
        "optional": False
    }
    ],
    "flavourText": "A King and his people are linked together\nlike a soul and a beating heart.\nBoth can be severed by a same edge, \nthen forged anew.",
    "itemType": "Two Handed Axe",
    "chaosValue": 525.21,
    "exaltedValue": 3,
    "count": 26,
    "detailsId": "kingmaker-despot-axe-6l",
    "listingCount": 28
},
{
    "id": 45222,
    "name": "Replica Kongor's Undying Rage",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kTWFjZXMvS29uZ29yc1VuZHlpbmdSYWdlIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/5fa26110bc/KongorsUndyingRage.png",
    "levelRequired": 67,
    "baseType": "Terror Maul",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [],
    "totalChange": 0
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        2.03,
        2.93,
        3.94,
        4.6,
        3.87,
        -6.12
    ],
    "totalChange": -6.12
    },
    "implicitModifiers": [
    {
        "text": "25% chance to double Stun Duration",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "Adds (46-55) to (332-394) Physical Damage",
        "optional": False
    },
    {
        "text": "(30-40)% increased Critical Strike Chance",
        "optional": False
    },
    {
        "text": "+(15-20)% to all Elemental Resistances",
        "optional": False
    },
    {
        "text": "Hits can't be Evaded",
        "optional": False
    },
    {
        "text": "Your Critical Strikes do not deal extra Damage",
        "optional": False
    },
    {
        "text": "Regenerate 20% of Energy Shield per second if you've dealt a Critical Strike with this weapon Recently",
        "optional": False
    }
    ],
    "flavourText": "\"Prototype #599 offers an incredible defensive power, but at a cost.\nWhat underlying physics are at play here, I wonder?\"",
    "itemType": "Two Handed Mace",
    "chaosValue": 525.21,
    "exaltedValue": 3,
    "count": 3,
    "detailsId": "replica-kongors-undying-rage-terror-maul-6l",
    "listingCount": 5
},
{
    "id": 45700,
    "name": "The Fulcrum",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvRWxlbWVudGFsSGFybW9ueSIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/912f60acd7/ElementalHarmony.png",
    "levelRequired": 60,
    "baseType": "Ezomyte Staff",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [
        0,
        15.7,
        4.96,
        -10.91,
        -10.35,
        -10.29,
        -10.15
    ],
    "totalChange": -10.15
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        15.7,
        4.96,
        -10.91,
        -10.35,
        -10.29,
        -10.15
    ],
    "totalChange": -10.15
    },
    "implicitModifiers": [
    {
        "text": "+20% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "(140-180)% increased Physical Damage",
        "optional": False
    },
    {
        "text": "(2-50)% of Physical Damage Converted to Fire Damage",
        "optional": False
    },
    {
        "text": "(4-50)% of Physical Damage Converted to Cold Damage",
        "optional": False
    },
    {
        "text": "(1-50)% of Physical Damage Converted to Lightning Damage",
        "optional": True
    },
    {
        "text": "Elemental Ailments you inflict are Reflected to you",
        "optional": False
    },
    {
        "text": "Elemental Damage with Hits is Lucky while you are Shocked",
        "optional": False
    },
    {
        "text": "Damage Penetrates (8-10)% Elemental Resistances while you are Chilled",
        "optional": False
    },
    {
        "text": "Gain (30-40)% of Physical Damage as Extra Damage of a random Element while you are Ignited",
        "optional": False
    }
    ],
    "flavourText": "To stand at the confluence of the elements,\nthe master must achieve perfect balance.",
    "itemType": "Staff",
    "chaosValue": 525.21,
    "exaltedValue": 3,
    "count": 39,
    "detailsId": "the-fulcrum-ezomyte-staff-6l",
    "listingCount": 51
},
{
    "id": 93556,
    "name": "The Annihilating Light",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvSW50cmVwaWR1c0RvbG9yZW0iLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MX1d/8244c5f079/IntrepidusDolorem.png",
    "levelRequired": 68,
    "baseType": "Quarterstaff",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [
        0,
        -1.33,
        -7.23,
        -5.81,
        -5.3,
        0.67,
        5.51
    ],
    "totalChange": 5.51
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        -1.33,
        -7.23,
        -5.81,
        -5.3,
        0.67,
        5.51
    ],
    "totalChange": 5.51
    },
    "implicitModifiers": [
    {
        "text": "+18% Chance to Block Attack Damage while wielding a Staff",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "(60-70)% reduced Elemental Resistances",
        "optional": False
    },
    {
        "text": "Deal Triple Damage with Elemental Skills",
        "optional": False
    }
    ],
    "flavourText": "There is no force more destructive in the heavens\nthan the scintillating light of utter clarity.",
    "itemType": "Staff",
    "chaosValue": 525.21,
    "exaltedValue": 3,
    "count": 99,
    "detailsId": "the-annihilating-light-quarterstaff-6l",
    "listingCount": 453
},
{
    "id": 402,
    "name": "Death's Opus",
    "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Cb3dzL0RlYXRoc2hhcnAiLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MX1d/488e5f6267/Deathsharp.png",
    "levelRequired": 70,
    "baseType": "Death Bow",
    "links": 6,
    "itemClass": 3,
    "sparkline": {
    "data": [
        0,
        -11.82,
        -17.84,
        -3.5,
        16.93,
        10.55,
        22.51
    ],
    "totalChange": 22.51
    },
    "lowConfidenceSparkline": {
    "data": [
        0,
        -11.82,
        -17.84,
        -3.5,
        16.93,
        10.55,
        22.51
    ],
    "totalChange": 22.51
    },
    "implicitModifiers": [
    {
        "text": "(30-50)% increased Critical Strike Chance",
        "optional": False
    }
    ],
    "explicitModifiers": [
    {
        "text": "(90-105)% increased Physical Damage",
        "optional": False
    },
    {
        "text": "Adds (6-12) to (20-25) Physical Damage",
        "optional": False
    },
    {
        "text": "10% increased Attack Speed",
        "optional": False
    },
    {
        "text": "+50% to Global Critical Strike Multiplier",
        "optional": False
    },
    {
        "text": "Bow Attacks fire 2 additional Arrows",
        "optional": False
    }
    ],
    "flavourText": "The overture stretches thin,\nThe chorus gathers to begin.\nStacatto, drone, a rest drawn long,\nAnother hears Death's final song.",
    "itemType": "Bow",
    "chaosValue": 512.57,
    "exaltedValue": 2.93,
    "count": 34,
    "detailsId": "deaths-opus-death-bow-6l",
    "listingCount": 46
},
{
      "id": 4951,
      "name": "Voidforge",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kU3dvcmRzL1N0YXJmb3JnZSIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/86b81685e1/Starforge.png",
      "levelRequired": 67,
      "baseType": "Infernal Sword",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          -8.52,
          -7.8,
          0.33,
          11.63,
          12.3,
          8.95
        ],
        "totalChange": 8.95
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -8.52,
          -7.8,
          0.33,
          11.63,
          12.3,
          8.95
        ],
        "totalChange": 8.95
      },
      "implicitModifiers": [
        {
          "text": "30% increased Elemental Damage with Attack Skills",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "(30-60)% increased Physical Damage",
          "optional": False
        },
        {
          "text": "(5-8)% increased Attack Speed",
          "optional": False
        },
        {
          "text": "+(90-100) to maximum Life",
          "optional": False
        },
        {
          "text": "Your Elemental Damage can Shock",
          "optional": False
        },
        {
          "text": "Gain 300% of Weapon Physical Damage as Extra Damage of a random Element",
          "optional": False
        },
        {
          "text": "20% increased Area of Effect for Attacks",
          "optional": False
        },
        {
          "text": "Deal no Non-Elemental Damage",
          "optional": False
        }
      ],
      "flavourText": "A weapon born of nothingness,\ncan only create more nothingness.",
      "itemType": "Two Handed Sword",
      "chaosValue": 507.7,
      "exaltedValue": 2.9,
      "count": 99,
      "detailsId": "voidforge-infernal-sword-6l",
      "listingCount": 256
    },
    {
      "id": 46138,
      "name": "Replica Duskdawn",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvU29sYXJpc0x1bmFyaXNTdGFmZiIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/e5e9df18a4/SolarisLunarisStaff.png",
      "levelRequired": 64,
      "baseType": "Maelström Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          2,
          2.91,
          3.93,
          3.17,
          1.25,
          -0.37
        ],
        "totalChange": -0.37
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2,
          2.91,
          3.93,
          3.17,
          1.25,
          -0.37
        ],
        "totalChange": -0.37
      },
      "implicitModifiers": [
        {
          "text": "+25% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "+10% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        },
        {
          "text": "(40-50)% increased Critical Strike Chance",
          "optional": False
        },
        {
          "text": "Gain (10-20)% of Elemental Damage as Extra Chaos Damage",
          "optional": False
        },
        {
          "text": "+1% to Critical Strike Multiplier per 1% Chance to Block Attack Damage",
          "optional": False
        },
        {
          "text": "+60% to Critical Strike Multiplier if you've dealt a Non-Critical Strike Recently",
          "optional": False
        },
        {
          "text": "(120-150)% increased Elemental Damage if you've dealt a Critical Strike Recently",
          "optional": False
        }
      ],
      "flavourText": "\"Lab Two suffered significant structural damage in the process of creating\nPrototype #77. It is, however, the closest we've come to perfection.\"",
      "itemType": "Staff",
      "chaosValue": 499.19,
      "exaltedValue": 2.85,
      "count": 18,
      "detailsId": "replica-duskdawn-maelstrom-staff-6l",
      "listingCount": 34
    },
    {
      "id": 4955,
      "name": "Disintegrator",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvRWxkZXJTdGFmZiIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/4d2bfda95c/ElderStaff.png",
      "levelRequired": 64,
      "baseType": "Maelström Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          0.51,
          -0.67,
          1.89,
          -15.87,
          -11.33,
          7.83
        ],
        "totalChange": 7.83
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0.51,
          -0.67,
          1.89,
          -15.87,
          -11.33,
          7.83
        ],
        "totalChange": 7.83
      },
      "implicitModifiers": [
        {
          "text": "+25% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Adds (220-240) to (272-300) Physical Damage",
          "optional": False
        },
        {
          "text": "+1 to Maximum Siphoning Charges per Elder or Shaper Item Equipped",
          "optional": False
        },
        {
          "text": "25% chance to gain a Siphoning Charge when you use a Skill",
          "optional": False
        },
        {
          "text": "Adds (12-14) to (15-16) Physical Damage to Attacks and Spells per Siphoning Charge",
          "optional": False
        },
        {
          "text": "Gain 4% of Non-Chaos Damage as extra Chaos Damage per Siphoning Charge",
          "optional": False
        },
        {
          "text": "1% additional Physical Damage Reduction from Hits per Siphoning Charge",
          "optional": False
        },
        {
          "text": "0.2% of Damage Leeched as Life per Siphoning Charge",
          "optional": False
        },
        {
          "text": "Take 150 Physical Damage per Second per Siphoning Charge if you've used a Skill Recently",
          "optional": False
        },
        {
          "text": "Battlemage",
          "optional": False
        }
      ],
      "flavourText": "Blurred is the boundary\nbetween creator and destroyer.",
      "itemType": "Staff",
      "chaosValue": 447.86,
      "exaltedValue": 2.56,
      "count": 14,
      "detailsId": "disintegrator-maelstrom-staff-6l",
      "listingCount": 24
    },
    {
      "id": 1884,
      "name": "Windripper",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Cb3dzL0VhZ2xlIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/01fdf37ac0/Eagle.png",
      "levelRequired": 66,
      "baseType": "Imperial Bow",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          -0.76,
          4.52,
          6.37,
          3.33,
          7.19,
          7.55
        ],
        "totalChange": 7.55
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -0.76,
          4.52,
          6.37,
          3.33,
          7.19,
          7.55
        ],
        "totalChange": 7.55
      },
      "implicitModifiers": [
        {
          "text": "(20-24)% increased Elemental Damage with Attack Skills",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Adds (48-60) to (72-90) Cold Damage",
          "optional": False
        },
        {
          "text": "Adds 1 to (120-150) Lightning Damage",
          "optional": False
        },
        {
          "text": "(10-15)% increased Attack Speed",
          "optional": False
        },
        {
          "text": "(30-40)% increased Critical Strike Chance",
          "optional": False
        },
        {
          "text": "15% increased Quantity of Items Dropped by Slain Frozen Enemies",
          "optional": False
        },
        {
          "text": "30% increased Rarity of Items Dropped by Slain Shocked Enemies",
          "optional": False
        }
      ],
      "flavourText": "It hunts; as silent as falling snow, as deadly as the tempest.",
      "itemType": "Bow",
      "chaosValue": 437.68,
      "exaltedValue": 2.5,
      "count": 99,
      "detailsId": "windripper-imperial-bow-6l",
      "listingCount": 218
    },
    {
      "id": 2031,
      "name": "Duskdawn",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvU29sYXJpc0x1bmFyaXNTdGFmZiIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/e5e9df18a4/SolarisLunarisStaff.png",
      "levelRequired": 64,
      "baseType": "Maelström Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          -14.31,
          -3.53,
          3.61,
          4.83,
          -1.82,
          -12.1
        ],
        "totalChange": -12.1
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -14.31,
          -3.53,
          3.61,
          4.83,
          -1.82,
          -12.1
        ],
        "totalChange": -12.1
      },
      "implicitModifiers": [
        {
          "text": "+25% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "+10% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        },
        {
          "text": "(60-80)% increased Critical Strike Chance for Spells",
          "optional": False
        },
        {
          "text": "Gain (10-20)% of Elemental Damage as Extra Chaos Damage",
          "optional": False
        },
        {
          "text": "+1% to Critical Strike Multiplier per 1% Chance to Block Attack Damage",
          "optional": False
        },
        {
          "text": "+60% to Critical Strike Multiplier if you've dealt a Non-Critical Strike Recently",
          "optional": False
        },
        {
          "text": "(120-150)% increased Spell Damage if you've dealt a Critical Strike Recently",
          "optional": False
        }
      ],
      "flavourText": "\"The world is not simply black and white,\nit is not divided into good and evil.\nBut black and white, good and evil, do exist,\nand we must know how to recognize them.\"\n- Archbishop Geofri",
      "itemType": "Staff",
      "chaosValue": 437.68,
      "exaltedValue": 2.5,
      "count": 88,
      "detailsId": "duskdawn-maelstrom-staff-6l",
      "listingCount": 141
    },
    {
      "id": 2161,
      "name": "Martyr of Innocence",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvTWFydHlySW5ub2NlbmNlIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/6fd4eee9df/MartyrInnocence.png",
      "levelRequired": 52,
      "baseType": "Highborn Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          1.99,
          2.71,
          4.05,
          5.03,
          5.02,
          5.03
        ],
        "totalChange": 5.03
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          1.99,
          2.71,
          4.05,
          5.03,
          5.02,
          5.03
        ],
        "totalChange": 5.03
      },
      "implicitModifiers": [
        {
          "text": "+18% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Grants Level 15 Vengeance Skill",
          "optional": False
        },
        {
          "text": "+(12-16)% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        },
        {
          "text": "100% increased Fire Damage",
          "optional": False
        },
        {
          "text": "Adds (315-360) to (451-540) Fire Damage",
          "optional": False
        },
        {
          "text": "Damage Penetrates 15% of Fire Resistance if you have Blocked Recently",
          "optional": False
        },
        {
          "text": "Immune to Freeze and Chill while Ignited",
          "optional": False
        },
        {
          "text": "Battlemage",
          "optional": False
        }
      ],
      "flavourText": "You have been found guilty.\nLet the fires cleanse you of your sins.",
      "itemType": "Staff",
      "chaosValue": 437.68,
      "exaltedValue": 2.5,
      "count": 80,
      "detailsId": "martyr-of-innocence-highborn-staff-6l",
      "listingCount": 118
    },
    {
      "id": 42726,
      "name": "The Yielding Mortality",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvSGFyYmluZ2VyU3RhZmZVcGdyYWRlZCIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/76cf7c8cb7/HarbingerStaffUpgraded.png",
      "levelRequired": 66,
      "baseType": "Imperial Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          118.72,
          7.18,
          -14.87,
          -19.64,
          -21.23,
          -23.09
        ],
        "totalChange": -23.09
      },
      "implicitModifiers": [
        {
          "text": "+18% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Socketed Gems are supported by Level 1 Chance to Bleed",
          "optional": False
        },
        {
          "text": "Grants Summon Greater Harbinger of Brutality Skill",
          "optional": False
        },
        {
          "text": "+5% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        },
        {
          "text": "+(30-39)% to Damage over Time Multiplier for Bleeding from Critical Strikes",
          "optional": False
        },
        {
          "text": "Adds (161-181) to (202-220) Physical Damage",
          "optional": False
        },
        {
          "text": "(31-40)% increased Critical Strike Chance",
          "optional": False
        }
      ],
      "flavourText": "<<HBGAa>><<HBG01>><<HBGC04>><<HBG02>><<HBGC06>>\n<<HBGAa>><<HBG01>><<HBGAs>><<HBG02>><<HBGC06>>\n<<HBGC011>><<HBGAa>><<HBG04>><<HBGC08>><<HBGAa>>",
      "itemType": "Staff",
      "chaosValue": 419.5,
      "exaltedValue": 2.4,
      "count": 2,
      "detailsId": "the-yielding-mortality-imperial-staff-6l",
      "listingCount": 4
    },
    {
      "id": 1456,
      "name": "The Cauteriser",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kQXhlcy9Ud29IYW5kQXhlX3NwYXJlIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/6cc29798f1/TwoHandAxe_spare.png",
      "levelRequired": 40,
      "baseType": "Woodsplitter",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.31,
          -27.86,
          -42.7,
          4.61,
          -12.4,
          -18.21
        ],
        "totalChange": -18.21
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "+1 to Level of Socketed Strength Gems",
          "optional": False
        },
        {
          "text": "Trigger Level 5 Gore Shockwave on Melee Hit if you have at least 150 Strength",
          "optional": False
        },
        {
          "text": "+(15-30) to Strength",
          "optional": False
        },
        {
          "text": "(83-100)% increased Physical Damage",
          "optional": False
        },
        {
          "text": "Adds (35-45) to (80-90) Physical Damage",
          "optional": False
        },
        {
          "text": "Gain 70% of Physical Damage as Extra Fire Damage",
          "optional": False
        },
        {
          "text": "Culling Strike",
          "optional": False
        }
      ],
      "flavourText": "A burned branch leaks sap no more.",
      "itemType": "Two Handed Axe",
      "chaosValue": 409.7,
      "exaltedValue": 2.34,
      "count": 3,
      "detailsId": "the-cauteriser-woodsplitter-6l",
      "listingCount": 6
    },
    {
      "id": 2574,
      "name": "Arborix",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Cb3dzL1ZlcmRhbnRHdWFyZGlhbkJvdyIsInciOjIsImgiOjQsInNjYWxlIjoxfV0/9008310cc7/VerdantGuardianBow.png",
      "levelRequired": 70,
      "baseType": "Assassin Bow",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          1.48,
          7.24,
          2.61,
          2.42,
          2.45,
          2.45
        ],
        "totalChange": 2.45
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          1.48,
          7.24,
          2.61,
          2.42,
          2.45,
          2.45
        ],
        "totalChange": 2.45
      },
      "implicitModifiers": [
        {
          "text": "+(15-25)% to Global Critical Strike Multiplier",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Grants Level 30 Dash Skill",
          "optional": False
        },
        {
          "text": "Adds (80-100) to (200-225) Physical Damage",
          "optional": False
        },
        {
          "text": "Bow Attacks fire 2 additional Arrows if you haven't Cast Dash recently",
          "optional": False
        },
        {
          "text": "(20-30)% increased Attack Speed if you haven't Cast Dash recently",
          "optional": False
        },
        {
          "text": "(100-160)% increased Evasion Rating if you've Cast Dash recently",
          "optional": False
        },
        {
          "text": "(20-30)% increased Movement Speed if you've Cast Dash recently",
          "optional": False
        },
        {
          "text": "Travel Skills other than Dash are Disabled",
          "optional": False
        },
        {
          "text": "Iron Reflexes",
          "optional": False
        }
      ],
      "flavourText": "Through droughts, fires, floods and frost,\nthe ancient giants stand resolute,\nwhile deep in the rich, dark earth,\ntheir grasp stretches ever farther.",
      "itemType": "Bow",
      "chaosValue": 385.15,
      "exaltedValue": 2.2,
      "count": 21,
      "detailsId": "arborix-assassin-bow-6l",
      "listingCount": 37
    },
    {
      "id": 2012,
      "name": "Kitava's Feast",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kQXhlcy9LaXRhdmFzSHVuZ2VyIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/7e0b7ac41a/KitavasHunger.png",
      "levelRequired": 68,
      "baseType": "Void Axe",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          2.95,
          2.91,
          3.95,
          4.59,
          4.83,
          10.74
        ],
        "totalChange": 10.74
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.95,
          2.91,
          3.95,
          4.59,
          4.83,
          10.74
        ],
        "totalChange": 10.74
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Socketed Gems are supported by Level 25 Melee Splash",
          "optional": False
        },
        {
          "text": "(200-240)% increased Physical Damage",
          "optional": False
        },
        {
          "text": "1% of Physical Attack Damage Leeched as Life",
          "optional": False
        },
        {
          "text": "1% of Physical Attack Damage Leeched as Mana",
          "optional": False
        },
        {
          "text": "Recover 5% of Life on Kill",
          "optional": False
        },
        {
          "text": "Enemies Killed by your Hits are destroyed",
          "optional": False
        }
      ],
      "flavourText": "Hinekora bound Kitava to a rock \nthat Kitava could not lift with all his might.\nKitava vowed that when he broke free, \nhe would devour every soul in Hinekora's domain.",
      "itemType": "Two Handed Axe",
      "chaosValue": 369.88,
      "exaltedValue": 2.11,
      "count": 11,
      "detailsId": "kitavas-feast-void-axe-6l",
      "listingCount": 21
    },
    {
      "id": 42715,
      "name": "Witchhunter's Judgment",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvQnJhbmREZXRvbmF0ZVN0YWZmIiwidyI6MiwiaCI6NCwic2NhbGUiOjF9XQ/07d64ef02c/BrandDetonateStaff.png",
      "levelRequired": 68,
      "baseType": "Highborn Staff",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.41,
          8.17,
          9.24,
          9.93,
          6.45,
          5.28
        ],
        "totalChange": 5.28
      },
      "implicitModifiers": [
        {
          "text": "+18% Chance to Block Attack Damage while wielding a Staff",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Grants Level 20 Brandsurge Skill",
          "optional": False
        },
        {
          "text": "Brand Skills have (64-96)% increased Duration",
          "optional": False
        }
      ],
      "flavourText": "The pyre is never wasted on just one heretic.",
      "itemType": "Staff",
      "chaosValue": 369.22,
      "exaltedValue": 2.11,
      "count": 2,
      "detailsId": "witchhunters-judgment-highborn-staff-6l",
      "listingCount": 4
    },
    {
      "id": 45091,
      "name": "Replica Trypanon",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Ud29IYW5kTWFjZXMvVHJ5cGFub24iLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MX1d/3152ab4124/Trypanon.png",
      "levelRequired": 40,
      "baseType": "Great Mallet",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.03,
          2.93,
          3.94,
          4.6,
          4.66,
          4.83
        ],
        "totalChange": 4.83
      },
      "implicitModifiers": [
        {
          "text": "30% increased Stun Duration on Enemies",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "-5000 to Accuracy Rating",
          "optional": False
        },
        {
          "text": "This Weapon's Critical Strike Chance is 100%",
          "optional": False
        }
      ],
      "flavourText": "\"The best place for this prototype would be in the hands of our enemies.\"",
      "itemType": "Two Handed Mace",
      "chaosValue": 369.22,
      "exaltedValue": 2.11,
      "count": 2,
      "detailsId": "replica-trypanon-great-mallet-6l",
      "listingCount": 4
    },
    {
      "id": 436,
      "name": "Doomfletch's Prism",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9Cb3dzL0Rvb21GbGV0Y2giLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MX1d/a284f1cdab/DoomFletch.png",
      "levelRequired": 40,
      "baseType": "Royal Bow",
      "links": 6,
      "itemClass": 3,
      "sparkline": {
        "data": [
          0,
          1.51,
          2.41,
          3.43,
          4.09,
          4.32,
          4.32
        ],
        "totalChange": 4.32
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          1.51,
          2.41,
          3.43,
          4.09,
          4.32,
          4.32
        ],
        "totalChange": 4.32
      },
      "implicitModifiers": [
        {
          "text": "(20-24)% increased Elemental Damage with Attack Skills",
          "optional": False
        }
      ],
      "explicitModifiers": [
        {
          "text": "Adds (12-16) to (20-24) Physical Damage",
          "optional": False
        },
        {
          "text": "(10-14)% increased Attack Speed",
          "optional": False
        },
        {
          "text": "60% increased Mana Regeneration Rate",
          "optional": False
        },
        {
          "text": "Gain 100% of Weapon Physical Damage as Extra Damage of each Element",
          "optional": False
        }
      ],
      "flavourText": "\"The Vaal, a thousand years ago, \ncame up with more delightful methods of murder\nthan I could ever wish for.\" \n- Koralus Doomfletch",
      "itemType": "Bow",
      "chaosValue": 350.14,
      "exaltedValue": 2,
      "count": 19,
      "detailsId": "doomfletchs-prism-royal-bow-6l",
      "listingCount": 31
    },


]

def currency(request):
  response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Archnemesis&type=Currency')
  currencies_list = response.json()
  currencies_list2 = currencies_list['currencyDetails']
  return render (request,'items/currency.html', {'currency_list': currencies_list2} )
# def currency(request):
#     return render(request,'items/currency.html', {'currency_list': currencyDetails})
  
def scarabs(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=Scarab')
  scarabs_list = response.json()
  scarab_list = scarabs_list['lines']
  return render(request,'items/scarabs.html', {'scarab_list': scarab_list})
  
def weapons(request):
    return render(request,'items/weapons.html', {'weapon_list': weapon_list})