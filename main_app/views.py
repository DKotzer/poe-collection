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




scarab_list = [
    {
      "id": 42606,
      "name": "Winged Divination Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkRpdmluYXRpb24iLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/e6539f578d/Tier4ScarabDivination.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          8.6,
          22.22,
          20.38,
          11.11,
          10.67,
          11.11
        ],
        "totalChange": 11.11
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          8.6,
          22.22,
          20.38,
          11.11,
          10.67,
          11.11
        ],
        "totalChange": 11.11
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "250% more Divination Cards found in Area",
          "optional": False
        }
      ],
      "flavourText": "Hinekora has sent the world another herald, but this hatungo walks another path.\nWe are left blinded, and subject to the vagaries of Fate.",
      "chaosValue": 50,
      "exaltedValue": 0.29,
      "count": 99,
      "detailsId": "winged-divination-scarab",
      "listingCount": 2145
    },
    {
      "id": 42748,
      "name": "Winged Reliquary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYlVuaXF1ZSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/e234573349/Tier4ScarabUnique.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          12.5,
          25,
          57.61,
          50,
          33.28,
          25
        ],
        "totalChange": 25
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          12.5,
          25,
          57.61,
          50,
          33.28,
          25
        ],
        "totalChange": 25
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "250% more Unique Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "The books were burned, and the scribes set themselves aflame.\nWhat secret so terrible could they have discovered?\nThough centuries have passed, we must investigate this for ourselves.",
      "chaosValue": 50,
      "exaltedValue": 0.29,
      "count": 99,
      "detailsId": "winged-reliquary-scarab",
      "listingCount": 1026
    },
    {
      "id": 60221,
      "name": "Winged Abyss Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkFieXNzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/c16297c4d3/Tier4ScarabAbyss.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -2.5,
          0,
          3.1,
          37.5,
          24.94,
          23.75
        ],
        "totalChange": 23.75
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -2.5,
          0,
          3.1,
          37.5,
          24.94,
          23.75
        ],
        "totalChange": 23.75
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 3 additional Abysses\nAbysses in Areas spawn 100% increased Monsters",
          "optional": False
        }
      ],
      "flavourText": "The Abyssals creep forth by night and by storm. Their eons underground were not\na respite, but an amassing, and now they number beyond comprehension.",
      "chaosValue": 49.5,
      "exaltedValue": 0.28,
      "count": 99,
      "detailsId": "winged-abyss-scarab",
      "listingCount": 508
    },
    {
      "id": 42683,
      "name": "Winged Harbinger Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkhhcmJpbmdlcnMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/81caefbf3f/Tier4ScarabHarbingers.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          2.56,
          5.45,
          28.21,
          24.37,
          9.67,
          2.56
        ],
        "totalChange": 2.56
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.56,
          5.45,
          28.21,
          24.37,
          9.67,
          2.56
        ],
        "totalChange": 2.56
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 7 additional Harbingers",
          "optional": False
        }
      ],
      "flavourText": "The thousand year truce has faltered, for the inscrutable ones have imprisoned their own God.\nShould they invade again, there will be no warning.",
      "chaosValue": 40,
      "exaltedValue": 0.23,
      "count": 99,
      "detailsId": "winged-harbinger-scarab",
      "listingCount": 1061
    },
    {
      "id": 42659,
      "name": "Winged Ambush Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYlN0cm9uZ2JveGVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/dd7b8bd53f/Tier4ScarabStrongboxes.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          6.06,
          21.21,
          21.21,
          26.94,
          24.27,
          18.18
        ],
        "totalChange": 18.18
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          6.06,
          21.21,
          21.21,
          26.94,
          24.27,
          18.18
        ],
        "totalChange": 18.18
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 9 additional Strongboxes",
          "optional": False
        }
      ],
      "flavourText": "In the absence of a strong martial presence, the renegades rise once more.\nTheir poisons threaten to cloud the land.",
      "chaosValue": 39,
      "exaltedValue": 0.22,
      "count": 99,
      "detailsId": "winged-ambush-scarab",
      "listingCount": 770
    },
    {
      "id": 42639,
      "name": "Winged Breach Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkJyZWFjaCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/0b375322d7/Tier4ScarabBreach.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          47.41,
          44.44,
          44.44,
          48.15,
          40.77,
          41.19
        ],
        "totalChange": 41.19
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          47.41,
          44.44,
          44.44,
          48.15,
          40.77,
          41.19
        ],
        "totalChange": 41.19
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 5 additional Breaches",
          "optional": False
        }
      ],
      "flavourText": "The Master Researcher's final commandment has failed.\nThe High Templar has seen the truth of our situation,\nand the world will be undone by his fear.",
      "chaosValue": 38.12,
      "exaltedValue": 0.22,
      "count": 99,
      "detailsId": "winged-breach-scarab",
      "listingCount": 565
    },
    {
      "id": 42605,
      "name": "Winged Legion Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkxlZ2lvbiIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/05b623a2a7/Tier4ScarabLegion.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          8,
          8,
          8,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          8,
          8,
          8,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 2 additional Legion Encounters\nEach Legion contains a War Hoard\nEach Legion is accompanied by a General",
          "optional": False
        }
      ],
      "flavourText": "As the passage between Wraeclast and the land beyond time's reach is torn open,\nwe stand on the precipice of eternal war.\nAnd no one remains to hold us back.",
      "chaosValue": 25,
      "exaltedValue": 0.14,
      "count": 99,
      "detailsId": "winged-legion-scarab",
      "listingCount": 591
    },
    {
      "id": 70514,
      "name": "Winged Expedition Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkV4cGVkaXRpb24iLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/b4dd63608b/Tier4ScarabExpedition.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -1.19,
          0,
          -3.33,
          -3.33,
          -11.53,
          -16.67
        ],
        "totalChange": -16.67
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -1.19,
          0,
          -3.33,
          -3.33,
          -11.53,
          -16.67
        ],
        "totalChange": -16.67
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Expedition Encounter\nArea contains 50% increased number of Runic Monster Markers\n20% increased number of Explosives\nRemnants in area have an additional Suffix",
          "optional": False
        }
      ],
      "flavourText": "Darkness surges in the shadows of the past. Ancient evils stir. The stars\nwatch, forever aloof, forever menacing. None remain who know the\nsecret, so we are defenseless in the face of the unknown.",
      "chaosValue": 25,
      "exaltedValue": 0.14,
      "count": 99,
      "detailsId": "winged-expedition-scarab",
      "listingCount": 1143
    },
    {
      "id": 42558,
      "name": "Craicic Lure",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQmVzdGlhcnkvQ3VycmVuY3lDcmFiQXNwZWN0IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/602d1dc44e/CurrencyCrabAspect.png",
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -5.56,
          -5.56,
          5.56,
          4.2,
          9.74,
          11.11
        ],
        "totalChange": 11.11
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -5.56,
          -5.56,
          5.56,
          4.2,
          9.74,
          11.11
        ],
        "totalChange": 11.11
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 4 additional Red Beasts from The Deep\nCannot be used alongside a Bestiary Scarab",
          "optional": False
        }
      ],
      "flavourText": "",
      "chaosValue": 20,
      "exaltedValue": 0.11,
      "count": 99,
      "detailsId": "craicic-lure",
      "listingCount": 607
    },
    {
      "id": 18991,
      "name": "Gilded Harbinger Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiSGFyYmluZ2VycyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/ce393cfd58/GreaterScarabHarbingers.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0.06,
          -5.83,
          -5.83,
          -5.83,
          -3.67,
          -0.47
        ],
        "totalChange": -0.47
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0.06,
          -5.83,
          -5.83,
          -5.83,
          -3.67,
          -0.47
        ],
        "totalChange": -0.47
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 4 additional Harbingers",
          "optional": False
        }
      ],
      "flavourText": "For your valour beyond the Gate, Sarina Titucius, we honour you with the first\nGilded Scarab awarded while its recipient still lives. Remain vigilant.",
      "chaosValue": 16.91,
      "exaltedValue": 0.1,
      "count": 99,
      "detailsId": "gilded-harbinger-scarab",
      "listingCount": 5684
    },
    {
      "id": 19007,
      "name": "Gilded Divination Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiRGl2aW5hdGlvbiIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/8101d1a6e1/GreaterScarabDivination.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -3.86,
          -4.06,
          -9.52,
          -1,
          7.74,
          -4.37
        ],
        "totalChange": -4.37
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -3.86,
          -4.06,
          -9.52,
          -1,
          7.74,
          -4.37
        ],
        "totalChange": -4.37
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "150% more Divination Cards found in Area",
          "optional": False
        }
      ],
      "flavourText": "Your centuries of service have been invaluable to us, Narumoa. Go now,\nreturn to Hinekora, and join your ancient kin in the halls of the dead.",
      "chaosValue": 16.91,
      "exaltedValue": 0.1,
      "count": 99,
      "detailsId": "gilded-divination-scarab",
      "listingCount": 6013
    },
    {
      "id": 42494,
      "name": "Fenumal Lure",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQmVzdGlhcnkvQ3VycmVuY3lTcGlkZXJBc3BlY3QiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/bf4835aab6/CurrencySpiderAspect.png",
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          13.33,
          26.67,
          33.33,
          20,
          1.46,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          13.33,
          26.67,
          33.33,
          20,
          1.46,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 4 additional Red Beasts from The Caverns\nCannot be used alongside a Bestiary Scarab",
          "optional": False
        }
      ],
      "flavourText": "",
      "chaosValue": 15,
      "exaltedValue": 0.09,
      "count": 99,
      "detailsId": "fenumal-lure",
      "listingCount": 900
    },
    {
      "id": 70512,
      "name": "Gilded Expedition Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiRXhwZWRpdGlvbiIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/19a2dff87d/GreaterScarabExpedition.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -1.68,
          -13.64,
          -8.96,
          4,
          4.98,
          7.95
        ],
        "totalChange": 7.95
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -1.68,
          -13.64,
          -8.96,
          4,
          4.98,
          7.95
        ],
        "totalChange": 7.95
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Expedition Encounter\nArea contains 50% increased number of Runic Monster Markers\n20% increased number of Explosives",
          "optional": False
        }
      ],
      "flavourText": "We lay you to rest in the forest deep, Runesmith Revna, so that you may be\nforever hidden from the stars which so terrified you in your final days.\nMay the secret you took to your grave be lifted from your burdens.",
      "chaosValue": 15,
      "exaltedValue": 0.09,
      "count": 99,
      "detailsId": "gilded-expedition-scarab",
      "listingCount": 6867
    },
    {
      "id": 42657,
      "name": "Winged Bestiary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkJlYXN0cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/7d79b58e5e/Tier4ScarabBeasts.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 5 additional Red Beasts",
          "optional": False
        }
      ],
      "flavourText": "Without an experienced Beastmaster to find them new realms,\nthe First Ones' ravaging hunt brings them ever closer to Wraeclast.",
      "chaosValue": 14,
      "exaltedValue": 0.08,
      "count": 99,
      "detailsId": "winged-bestiary-scarab",
      "listingCount": 346
    },
    {
      "id": 60220,
      "name": "Winged Blight Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkJsaWdodCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/6dde3a6e88/Tier4ScarabBlight.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0.42,
          -7.95,
          -7.95,
          -1.21,
          0.42,
          0.42
        ],
        "totalChange": 0.42
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0.42,
          -7.95,
          -7.95,
          -1.21,
          0.42,
          0.42
        ],
        "totalChange": 0.42
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains a Blight Encounter\nBlight Encounters contain an additional Blight Boss\n50% chance for Blight Chests to contain an additional Reward\nLanes of Blight Encounters in Areas have an additional Reward Chest",
          "optional": False
        }
      ],
      "flavourText": "The fungal plague returns, and its roots have adapted.\nThe undiscovered Blightheart that Dhunan theorised\nmust still exist somewhere, yet none remain\nwith the skill to see to its destruction.",
      "chaosValue": 12,
      "exaltedValue": 0.07,
      "count": 99,
      "detailsId": "winged-blight-scarab",
      "listingCount": 575
    },
    {
      "id": 19013,
      "name": "Gilded Ambush Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiU3Ryb25nYm94ZXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/8b46f6270a/GreaterScarabStrongboxes.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -4.54,
          -14.08,
          -14.08,
          -4.54,
          -0.01,
          0.62
        ],
        "totalChange": 0.62
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -4.54,
          -14.08,
          -14.08,
          -4.54,
          -0.01,
          0.62
        ],
        "totalChange": 0.62
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 5 additional Strongboxes",
          "optional": False
        }
      ],
      "flavourText": "Master Warrior Rindwik fell to one opponent alone: old age.\nOnly the greatest soldiers can say as much.",
      "chaosValue": 10.54,
      "exaltedValue": 0.06,
      "count": 99,
      "detailsId": "gilded-ambush-scarab",
      "listingCount": 7115
    },
    {
      "id": 42604,
      "name": "Winged Sulphite Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYlN1bHBoaXRlIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/91ecb97f73/Tier4ScarabSulphite.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Niko\nMap owner gains 100% more Sulphite",
          "optional": False
        }
      ],
      "flavourText": "Madness marches in machine form.\nHarnessed lightning, grim faces, and cold ambition abounds.\nCivilisation will be its own undoing.",
      "chaosValue": 10,
      "exaltedValue": 0.06,
      "count": 99,
      "detailsId": "winged-sulphite-scarab",
      "listingCount": 496
    },
    {
      "id": 42630,
      "name": "Winged Cartography Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYk1hcHMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/eec98e626c/Tier4ScarabMaps.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -0.01,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -0.01,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "85% more Maps found in Area",
          "optional": False
        }
      ],
      "flavourText": "The Sealing Blade has been removed, and the agent of Decay\nshall feed upon this world until nothing remains but dust.",
      "chaosValue": 10,
      "exaltedValue": 0.06,
      "count": 99,
      "detailsId": "winged-cartography-scarab",
      "listingCount": 545
    },
    {
      "id": 70511,
      "name": "Polished Expedition Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJFeHBlZGl0aW9uIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/a1f5997c7d/NormalScarabExpedition.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          2.34,
          2.68,
          2.68,
          2.68,
          4.79,
          5.08
        ],
        "totalChange": 5.08
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          2.34,
          2.68,
          2.68,
          2.68,
          4.79,
          5.08
        ],
        "totalChange": 5.08
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Expedition Encounter\nArea contains 25% increased number of Runic Monster Markers\n20% increased number of Explosives",
          "optional": False
        }
      ],
      "flavourText": "As you delve into the mysteries of this world, apprentice Revna,\nremember to learn from the past, not be consumed by it.",
      "chaosValue": 9.21,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "polished-expedition-scarab",
      "listingCount": 8904
    },
    {
      "id": 18989,
      "name": "Gilded Breach Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiQnJlYWNoIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/6c012fae5c/GreaterScarabBreach.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          4.05,
          -7.52,
          -7.52,
          4.05,
          5.41,
          4.74
        ],
        "totalChange": 4.74
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          4.05,
          -7.52,
          -7.52,
          4.05,
          5.41,
          4.74
        ],
        "totalChange": 4.74
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 3 additional Breaches",
          "optional": False
        }
      ],
      "flavourText": "Omid, Master Researcher, has left a final commandment upon his death:\nthe world must never know.",
      "chaosValue": 9.06,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "gilded-breach-scarab",
      "listingCount": 4354
    },
    {
      "id": 42633,
      "name": "Winged Metamorph Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYk1ldGFtb3JwaCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/08a2978215/Tier4ScarabMetamorph.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -10,
          -10
        ],
        "totalChange": -10
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -10,
          -10
        ],
        "totalChange": -10
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Metamorph Monsters\nMetamorph Bosses which drop an Itemised Sample drop two additional Itemised Samples\nAll Metamorph Monsters have Rewards",
          "optional": False
        }
      ],
      "flavourText": "Though the Necromancer of Weeping Black fell in the desert by the hand of Garukhan,\nhis mindless legions remain scattered throughout Wraeclast, with no master to curb their hunger.",
      "chaosValue": 9,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "winged-metamorph-scarab",
      "listingCount": 429
    },
    {
      "id": 18996,
      "name": "Polished Harbinger Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJIYXJiaW5nZXJzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/640ad00ede/NormalScarabHarbingers.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          1.88,
          -5.71,
          -8.62,
          1.49,
          2.4,
          -0.86
        ],
        "totalChange": -0.86
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          1.88,
          -5.71,
          -8.62,
          1.49,
          2.4,
          -0.86
        ],
        "totalChange": -0.86
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 3 additional Harbingers",
          "optional": False
        }
      ],
      "flavourText": "For deciphering the language of the inscrutable ones, honoured Sarina,\nwe charge you with investigating their intent in our land.",
      "chaosValue": 8.68,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "polished-harbinger-scarab",
      "listingCount": 5306
    },
    {
      "id": 42678,
      "name": "Winged Shaper Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYlNoYXBlciIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/1c759412df/Tier4ScarabShaper.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          -2.44,
          -11.11,
          -11.11,
          -11.11,
          -11.11
        ],
        "totalChange": -11.11
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          -2.44,
          -11.11,
          -11.11,
          -11.11,
          -11.11
        ],
        "totalChange": -11.11
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Shaper Influence outcome to Map Area\n150% more Rare Shaper Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "The Watchers have gone silent, yet they scream still.\nSomething lurks among the stars of our dreams, knocking at the door,\nwhispering with the voices of long lost friends...",
      "chaosValue": 8,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "winged-shaper-scarab",
      "listingCount": 434
    },
    {
      "id": 42692,
      "name": "Winged Elder Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYkVsZGVyIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/1d6efecde2/Tier4ScarabElder.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          -10,
          -10,
          -10.65,
          -20
        ],
        "totalChange": -20
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          -10,
          -10,
          -10.65,
          -20
        ],
        "totalChange": -20
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Elder Influence outcome to Map Area\n150% more Rare Elder Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "We are all equally fools for our childish notions.\nThat dread force Decay cannot be defeated by self-sacrifice.",
      "chaosValue": 8,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "winged-elder-scarab",
      "listingCount": 403
    },
    {
      "id": 42762,
      "name": "Winged Torment Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9UaWVyNFNjYXJhYlRvcm1lbnQiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/b809b07f2b/Tier4ScarabTorment.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          -10,
          -16.69,
          -20
        ],
        "totalChange": -20
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          -10,
          -16.69,
          -20
        ],
        "totalChange": -20
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 12 additional Tormented Spirits",
          "optional": False
        }
      ],
      "flavourText": "Without a speaker of the dead, the countless anguished spirits only grow in number.\nThey have no voice, and no hope. The sun darkens with each passing year.",
      "chaosValue": 8,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "winged-torment-scarab",
      "listingCount": 407
    },
    {
      "id": 22342,
      "name": "Gilded Legion Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiTGVnaW9uIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/a4fe4dfd58/GreaterScarabLegion.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -1.18,
          -1.76,
          -1.76,
          2.43,
          8.57,
          11.72
        ],
        "totalChange": 11.72
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -1.18,
          -1.76,
          -1.76,
          2.43,
          8.57,
          11.72
        ],
        "totalChange": 11.72
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Legion Encounter\nEach Legion contains a War Hoard\nEach Legion is accompanied by a General",
          "optional": False
        }
      ],
      "flavourText": "Given the fate of Deacon Eutychus and the men under Cardinal Sanctus Vox,\nlet none dare the Domain, lest they too feed that vile hunger eternal.",
      "chaosValue": 7.96,
      "exaltedValue": 0.05,
      "count": 99,
      "detailsId": "gilded-legion-scarab",
      "listingCount": 5275
    },
    {
      "id": 19010,
      "name": "Polished Divination Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJEaXZpbmF0aW9uIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/7fb7abf05a/NormalScarabDivination.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -10.15,
          -10.19,
          -10.19,
          -10.19,
          -2.62,
          -10.19
        ],
        "totalChange": -10.19
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -10.15,
          -10.19,
          -10.19,
          -10.19,
          -2.62,
          -10.19
        ],
        "totalChange": -10.19
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "100% more Divination Cards found in Area",
          "optional": False
        }
      ],
      "flavourText": "Though your peers fear you, Narumoa, the elders have decided that your\nsecond sight is ideal for handling all artefacts that seek to subvert Fate.",
      "chaosValue": 6,
      "exaltedValue": 0.03,
      "count": 99,
      "detailsId": "polished-divination-scarab",
      "listingCount": 5555
    },
    {
      "id": 19017,
      "name": "Polished Ambush Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJTdHJvbmdib3hlcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/46451362bc/NormalScarabStrongboxes.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          -5.33,
          -0.08,
          -0.11,
          -0.33
        ],
        "totalChange": -0.33
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          -5.33,
          -0.08,
          -0.11,
          -0.33
        ],
        "totalChange": -0.33
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 4 additional Strongboxes",
          "optional": False
        }
      ],
      "flavourText": "Your people were renegades, Rindwik, but you have proven your loyalty.\nYou will lead the martial defence of our expeditions.",
      "chaosValue": 5.98,
      "exaltedValue": 0.03,
      "count": 99,
      "detailsId": "polished-ambush-scarab",
      "listingCount": 6173
    },
    {
      "id": 42505,
      "name": "Farric Lure",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQmVzdGlhcnkvQ3VycmVuY3lDYXRBc3BlY3QiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/f8cbe8eacc/CurrencyCatAspect.png",
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          25,
          25,
          25,
          21.82,
          25
        ],
        "totalChange": 25
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          25,
          25,
          25,
          21.82,
          25
        ],
        "totalChange": 25
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 4 additional Red Beasts from The Wilds\nCannot be used alongside a Bestiary Scarab",
          "optional": False
        }
      ],
      "flavourText": "",
      "chaosValue": 5,
      "exaltedValue": 0.03,
      "count": 99,
      "detailsId": "farric-lure",
      "listingCount": 1447
    },
    {
      "id": 18999,
      "name": "Gilded Bestiary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiQmVhc3RzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/7225b9e62b/GreaterScarabBeasts.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -19.3,
          -24.81,
          -24.81,
          -12.15,
          -0.3,
          0.25
        ],
        "totalChange": 0.25
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -19.3,
          -24.81,
          -24.81,
          -12.15,
          -0.3,
          0.25
        ],
        "totalChange": 0.25
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 3 additional Red Beasts",
          "optional": False
        }
      ],
      "flavourText": "The Order was your clan in life, Agnar, Beastmaster, but the First Ones call\nback their favoured son. The gift of their Visions will pass to another.",
      "chaosValue": 4,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "gilded-bestiary-scarab",
      "listingCount": 4909
    },
    {
      "id": 19027,
      "name": "Gilded Reliquary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiVW5pcXVlIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/6ec6815d00/GreaterScarabUnique.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          -11.74,
          -14.49,
          6.57,
          18.1,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          -11.74,
          -14.49,
          6.57,
          18.1,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "150% more Unique Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Go to your rest now, Sumei, Master Lorekeeper. The Order shall keep\ncontained the terrible secret that burdened your final years.",
      "chaosValue": 4,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "gilded-reliquary-scarab",
      "listingCount": 4938
    },
    {
      "id": 42556,
      "name": "Saqawine Lure",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQmVzdGlhcnkvQ3VycmVuY3lTbmFrZUFzcGVjdCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/a8228222e2/CurrencySnakeAspect.png",
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          -20,
          -20,
          -20
        ],
        "totalChange": -20
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          -20,
          -20,
          -20
        ],
        "totalChange": -20
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 4 additional Red Beasts from The Sands\nCannot be used alongside a Bestiary Scarab",
          "optional": False
        }
      ],
      "flavourText": "",
      "chaosValue": 4,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "saqawine-lure",
      "listingCount": 897
    },
    {
      "id": 60162,
      "name": "Gilded Abyss Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiQWJ5c3MiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/e6bcf6b93d/GreaterScarabAbyss.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          7.2,
          14.12,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          7.2,
          14.12,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 2 additional Abysses\nAbysses in Areas spawn 50% increased Monsters",
          "optional": False
        }
      ],
      "flavourText": "The Winter of the World has ended at the hands of the Three Sisters. We lay this scarab\nupon your ancient grave in thanks for your efforts, Honoured Founder. As you hoped,\nthe fate of your people will never befall another.",
      "chaosValue": 4,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "gilded-abyss-scarab",
      "listingCount": 6351
    },
    {
      "id": 60178,
      "name": "Gilded Blight Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiQmxpZ2h0IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/cf36f28d45/GreaterScarabBlight.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          4.65,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          4.65,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains a Blight Encounter\nBlight Encounters contain an additional Blight Boss\n50% chance for Blight Chests to contain an additional Reward",
          "optional": False
        }
      ],
      "flavourText": "Be at rest, Blightmaster Dhunan, on the distant shores of\nyour home. A dangerous expedition, but one worthy for\nhe who gave his life to cleanse Wraeclast.",
      "chaosValue": 4,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "gilded-blight-scarab",
      "listingCount": 6029
    },
    {
      "id": 18976,
      "name": "Rusted Harbinger Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJIYXJiaW5nZXJzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/1940157b44/LesserScarabHarbingers.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -0.06,
          -0.25
        ],
        "totalChange": -0.25
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          -0.06,
          -0.25
        ],
        "totalChange": -0.25
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 2 additional Harbingers",
          "optional": False
        }
      ],
      "flavourText": "Your ancestry has been much maligned by history, young Sarina Titucius,\nbut to the Order of the Djinn, you are born anew.",
      "chaosValue": 3.99,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "rusted-harbinger-scarab",
      "listingCount": 5306
    },
    {
      "id": 18973,
      "name": "Rusted Ambush Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJTdHJvbmdib3hlcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/5600ee7971/LesserScarabStrongboxes.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -1.4,
          -1.69,
          -1.69,
          -1.69,
          -4.14,
          -15.17
        ],
        "totalChange": -15.17
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -1.4,
          -1.69,
          -1.69,
          -1.69,
          -4.14,
          -15.17
        ],
        "totalChange": -15.17
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 3 additional Strongboxes",
          "optional": False
        }
      ],
      "flavourText": "Your outlaw camp abandoned you when their surprise attack failed, young Rindwik.\nNow that you know we exist, we cannot let you go. You have two choices.",
      "chaosValue": 3.02,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "rusted-ambush-scarab",
      "listingCount": 5786
    },
    {
      "id": 40058,
      "name": "Gilded Metamorph Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiTWV0YW1vcnBoIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/7e8dd3bd31/GreaterScarabMetamorph.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -15.48,
          -20.53,
          -20.53,
          -20.53,
          -11.67,
          -20.53
        ],
        "totalChange": -20.53
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -15.48,
          -20.53,
          -20.53,
          -20.53,
          -11.67,
          -20.53
        ],
        "totalChange": -20.53
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Metamorph Monsters\nMetamorph Bosses which drop an Itemised Sample drop an additional Itemised Sample\nAll Metamorph Monsters have Rewards",
          "optional": False
        }
      ],
      "flavourText": "There was a man of bone, rotting flesh, and weeping black, but his name, his\nill-gotten knowledge, and his role in the Order shall be stricken from memory.",
      "chaosValue": 3,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "gilded-metamorph-scarab",
      "listingCount": 4816
    },
    {
      "id": 70501,
      "name": "Rusted Expedition Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJFeHBlZGl0aW9uIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/e9bb9fa480/LesserScarabExpedition.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          1.34,
          0,
          0,
          4.84,
          5.86,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          1.34,
          0,
          0,
          4.84,
          5.86,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Expedition Encounter",
          "optional": False
        }
      ],
      "flavourText": "Your people no longer walk this continent, young Revna,\nbut the Order of the Djinn will give you a new home.",
      "chaosValue": 3,
      "exaltedValue": 0.02,
      "count": 99,
      "detailsId": "rusted-expedition-scarab",
      "listingCount": 14449
    },
    {
      "id": 19019,
      "name": "Gilded Cartography Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiTWFwcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/2567494a92/GreaterScarabMaps.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          -16.67,
          -28.31,
          0,
          -3.96,
          -16.67
        ],
        "totalChange": -16.67
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          -16.67,
          -28.31,
          0,
          -3.96,
          -16.67
        ],
        "totalChange": -16.67
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "50% more Maps found in Area",
          "optional": False
        }
      ],
      "flavourText": "Betucia, Bearer of the Sealing Blade, the Order of the Djinn survives\nbecause of your sacrifice, but will be forever wounded by your loss.",
      "chaosValue": 2.5,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "gilded-cartography-scarab",
      "listingCount": 3862
    },
    {
      "id": 19000,
      "name": "Gilded Sulphite Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiU3VscGhpdGUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/2a3855535e/GreaterScarabSulphite.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Niko\nMap owner gains 60% more Sulphite",
          "optional": False
        }
      ],
      "flavourText": "Let him not be called Raethan the Betrayer. His discovery was too important\nto keep locked away. Now, for good or ill, it is in civilisation's hands.",
      "chaosValue": 2,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "gilded-sulphite-scarab",
      "listingCount": 6506
    },
    {
      "id": 22458,
      "name": "Polished Legion Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJMZWdpb24iLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/0edb9242f1/NormalScarabLegion.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -5.44,
          -5.44,
          -5.44,
          -3.06,
          3.65,
          -5.44
        ],
        "totalChange": -5.44
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -5.44,
          -5.44,
          -5.44,
          -3.06,
          3.65,
          -5.44
        ],
        "totalChange": -5.44
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Legion Encounter\nEach Legion contains a War Hoard",
          "optional": False
        }
      ],
      "flavourText": "As our hand in the Chamber, we grant you, Deacon Eutychus,\naccess to a domain we lack the resources to explore.",
      "chaosValue": 2,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-legion-scarab",
      "listingCount": 7374
    },
    {
      "id": 18987,
      "name": "Polished Breach Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJCcmVhY2giLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/20276236e9/NormalScarabBreach.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          4.23,
          4.93,
          5.63,
          5.63,
          5.72,
          5.63
        ],
        "totalChange": 5.63
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          4.23,
          4.93,
          5.63,
          5.63,
          5.72,
          5.63
        ],
        "totalChange": 5.63
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 2 additional Breaches",
          "optional": False
        }
      ],
      "flavourText": "We task you, honoured Omid, with the investigation of this mysterious\n'Xoph' and artefacts related to rifts in the boundaries of our world.",
      "chaosValue": 1.5,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-breach-scarab",
      "listingCount": 6215
    },
    {
      "id": 18967,
      "name": "Rusted Divination Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJEaXZpbmF0aW9uIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/ac84db8246/LesserScarabDivination.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          9.42,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          9.42,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "50% more Divination Cards found in Area",
          "optional": False
        }
      ],
      "flavourText": "You were a casualty of callous Karui warfare, ageless Narumoa, but the Order\nmended your wounds. You are bound to us now by your own code.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "rusted-divination-scarab",
      "listingCount": 5828
    },
    {
      "id": 18992,
      "name": "Gilded Torment Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiVG9ybWVudCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/0dcb6987a3/GreaterScarabTorment.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          100,
          50,
          0,
          0,
          0.54,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          100,
          50,
          0,
          0,
          0.54,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 7 additional Tormented Spirits",
          "optional": False
        }
      ],
      "flavourText": "Though you were swallowed by your own darkness, you saved countless others\nfrom eternal misery, young Tsarsk. You were not nothing, as you feared.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "gilded-torment-scarab",
      "listingCount": 3083
    },
    {
      "id": 18993,
      "name": "Gilded Shaper Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiU2hhcGVyIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/8c0ef8557c/GreaterScarabShaper.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Shaper Influence outcome to Map Area\n90% more Rare Shaper Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Qianga of the Stars, Deliverer of the Sealing Blade to the Watchers, go now, and\nlet your half-dreamt life be troubled by nightmares of achromic hunger no more.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "gilded-shaper-scarab",
      "listingCount": 2866
    },
    {
      "id": 18997,
      "name": "Polished Cartography Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJNYXBzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/0baaf413d0/NormalScarabMaps.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "35% more Maps found in Area",
          "optional": False
        }
      ],
      "flavourText": "For your loyalty and valour, honoured Betucia, we are proud to put\nthe requisition of dream-artefacts in your capable hands.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-cartography-scarab",
      "listingCount": 3615
    },
    {
      "id": 19005,
      "name": "Polished Bestiary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJCZWFzdHMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/0f4dc83dc5/NormalScarabBeasts.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          18.4,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          18.4,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains 2 additional Red Beasts",
          "optional": False
        }
      ],
      "flavourText": "None among us understand the beasts of this world better than you,\nhonoured Agnar. You will root out the mysteries of wild-artefacts.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-bestiary-scarab",
      "listingCount": 6168
    },
    {
      "id": 19009,
      "name": "Gilded Elder Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9HcmVhdGVyU2NhcmFiRWxkZXIiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/2bd3ed1eca/GreaterScarabElder.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          10.02,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          10.02,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Elder Influence outcome to Map Area\n90% more Rare Elder Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Egrin of the Dark Between Stars, Forger of the Sealing Blade,\nlet your name be redeemed by your unexpected sacrifice.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "gilded-elder-scarab",
      "listingCount": 2637
    },
    {
      "id": 40044,
      "name": "Polished Metamorph Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJNZXRhbW9ycGgiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/86ad4cae39/NormalScarabMetamorph.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Metamorph Monsters\nMetamorph Bosses which drop an Itemised Sample drop an additional Itemised Sample",
          "optional": False
        }
      ],
      "flavourText": "As you explore the vast well of human darkness, Saresh, our Surgeon of the Dead,\nremember that the price can sometimes exceed the value of knowledge.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-metamorph-scarab",
      "listingCount": 7790
    },
    {
      "id": 60022,
      "name": "Polished Abyss Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJBYnlzcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/c78d645398/NormalScarabAbyss.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Abyss\nAbysses in Areas spawn 50% increased Monsters",
          "optional": False
        }
      ],
      "flavourText": "Your golems and your leadership have slowed the tide of death, Clayshaper.\nThe relics of power you bid us find have kept the Vastiri Plains from the brink\nof oblivion. The defences of the Maraketh will hold.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-abyss-scarab",
      "listingCount": 8578
    },
    {
      "id": 60120,
      "name": "Polished Blight Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJCbGlnaHQiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/fda66abb96/NormalScarabBlight.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0.5,
          0.5,
          0.5,
          0.5,
          0.5,
          0.5
        ],
        "totalChange": 0.5
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0.5,
          0.5,
          0.5,
          0.5,
          0.5,
          0.5
        ],
        "totalChange": 0.5
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains a Blight Encounter\nBlight Encounters contain an additional Blight Boss",
          "optional": False
        }
      ],
      "flavourText": "For using the techniques of your homeland to contain\nthe fungal plague, honoured Dhunan, you shall lead the war\nto eliminate it and end the century-cycle of infestation.",
      "chaosValue": 1,
      "exaltedValue": 0.01,
      "count": 99,
      "detailsId": "polished-blight-scarab",
      "listingCount": 9863
    },
    {
      "id": 22453,
      "name": "Rusted Legion Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJMZWdpb24iLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/0006525c3c/LesserScarabLegion.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0.05,
          0,
          0,
          52,
          46.23,
          64
        ],
        "totalChange": 64
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0.05,
          0,
          0,
          52,
          46.23,
          64
        ],
        "totalChange": 64
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Legion Encounter",
          "optional": False
        }
      ],
      "flavourText": "Your faith and our Order are not in opposition, young Eutychus. \nLet this be the start of a new era of cooperation.",
      "chaosValue": 0.82,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-legion-scarab",
      "listingCount": 7489
    },
    {
      "id": 18966,
      "name": "Rusted Cartography Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJNYXBzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/c982c28d52/LesserScarabMaps.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "20% more Maps found in Area",
          "optional": False
        }
      ],
      "flavourText": "Consider yourself an orphaned Eternal no longer, young Betucia.\nThe Order of the Djinn is your family now.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-cartography-scarab",
      "listingCount": 4881
    },
    {
      "id": 18968,
      "name": "Rusted Reliquary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJVbmlxdWUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/72516960f1/LesserScarabUnique.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "50% more Unique Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "The Maraketh left you to die alone in the desert, young Sumei, but we\nsaw the potential in you. The Order of the Djinn is your akhara now.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-reliquary-scarab",
      "listingCount": 6959
    },
    {
      "id": 18969,
      "name": "Rusted Elder Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJFbGRlciIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/11cabe4d12/LesserScarabElder.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -1.99,
          0,
          0,
          0,
          -0.04,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -1.99,
          0,
          0,
          0,
          -0.04,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Elder Influence outcome to Map Area\n30% more Rare Elder Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Your visions led the Azmeri down into a world left abandoned by the Vaal.\nThey cast you out, young Egrin, but the Order of the Djinn accepts you.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-elder-scarab",
      "listingCount": 6521
    },
    {
      "id": 18970,
      "name": "Rusted Bestiary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJCZWFzdHMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/ea23afd0ff/LesserScarabBeasts.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Einhar\nArea contains an additional Red Beast",
          "optional": False
        }
      ],
      "flavourText": "Feuding Ezomytes slaughtered your kin, young Agnar, but we pulled you\nfrom the flames. The Order of the Djinn is your clan now.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-bestiary-scarab",
      "listingCount": 8588
    },
    {
      "id": 18971,
      "name": "Rusted Torment Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJUb3JtZW50IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/b4e843a49b/LesserScarabTorment.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 3 additional Tormented Spirits",
          "optional": False
        }
      ],
      "flavourText": "Young Tsarsk, you were a broken and forgotten child lying glassy-eyed\nin a flesh-pit in Trarthus, but the Order found and cleansed you.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-torment-scarab",
      "listingCount": 6322
    },
    {
      "id": 18972,
      "name": "Rusted Breach Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJCcmVhY2giLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/37bd40da6c/LesserScarabBreach.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Breach",
          "optional": False
        }
      ],
      "flavourText": "The Ember-dwellers sought to throw you to their volcanic god, young Omid,\nbut we caught you instead. The Order of the Djinn is your tribe now.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-breach-scarab",
      "listingCount": 8470
    },
    {
      "id": 18974,
      "name": "Rusted Shaper Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJTaGFwZXIiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/9e83e315c9/LesserScarabShaper.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Shaper Influence outcome to Map Area\n30% more Rare Shaper Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "The Peak-dwellers saw you as impure, young Qianga, but the Order of\nthe Djinn sees you as all the stronger for your uniqueness.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-shaper-scarab",
      "listingCount": 6724
    },
    {
      "id": 18977,
      "name": "Rusted Sulphite Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJTdWxwaGl0ZSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/1e18c30014/LesserScarabSulphite.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Niko\nMap owner gains 20% more Sulphite",
          "optional": False
        }
      ],
      "flavourText": "As the first Brinerot to join the Order, you have much to prove,\nyoung Raethan. We are confident you will succeed.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-sulphite-scarab",
      "listingCount": 8575
    },
    {
      "id": 18984,
      "name": "Polished Shaper Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJTaGFwZXIiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/f92a75e584/NormalScarabShaper.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Shaper Influence outcome to Map Area\n60% more Rare Shaper Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Bold dreamer, Qianga of the Stars, she of the Celestial Cold! These titles\nwe bestow upon the one among us whose soul speaks to the ineffable.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "polished-shaper-scarab",
      "listingCount": 5369
    },
    {
      "id": 18986,
      "name": "Polished Sulphite Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJTdWxwaGl0ZSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/3b6d388b91/NormalScarabSulphite.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Niko\nMap owner gains 40% more Sulphite",
          "optional": False
        }
      ],
      "flavourText": "For harnessing and controlling the power of lightning, you, Raethan,\nare now charged with researching this new energy.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "polished-sulphite-scarab",
      "listingCount": 7368
    },
    {
      "id": 18998,
      "name": "Polished Torment Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJUb3JtZW50IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/b93daed118/NormalScarabTorment.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains 5 additional Tormented Spirits",
          "optional": False
        }
      ],
      "flavourText": "Your tortured soul long kept you isolated from your peers, Tsarsk, but has attracted\nnew kindred in kind. You are tasked with appeasing these anguished spirits.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "polished-torment-scarab",
      "listingCount": 5076
    },
    {
      "id": 19002,
      "name": "Polished Elder Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJFbGRlciIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/c950788060/NormalScarabElder.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Adds Elder Influence outcome to Map Area\n60% more Rare Elder Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "Speaker of unclean truths, Egrin of the Dark Between Stars.\nWe curse you whose soul echoes the madness of the void!",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "polished-elder-scarab",
      "listingCount": 5102
    },
    {
      "id": 19012,
      "name": "Polished Reliquary Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9Ob3JtYWxTY2FyYWJVbmlxdWUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/774d92ac8e/NormalScarabUnique.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "100% more Unique Items found in Area",
          "optional": False
        }
      ],
      "flavourText": "As the best of our lorekeepers, honoured Sumei, it is now your task\nto investigate the mysterious duplication of artefacts of power.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "polished-reliquary-scarab",
      "listingCount": 6092
    },
    {
      "id": 40043,
      "name": "Rusted Metamorph Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJNZXRhbW9ycGgiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/2bff955eb6/LesserScarabMetamorph.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains Metamorph Monsters",
          "optional": False
        }
      ],
      "flavourText": "Rejected even by the Faridun outcasts, young Saresh, you were cursed to walk the\nwhite sands until we found you. The Order shall command your penance now.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-metamorph-scarab",
      "listingCount": 7150
    },
    {
      "id": 60074,
      "name": "Rusted Blight Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJCbGlnaHQiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/c35814598b/LesserScarabBlight.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "totalChange": 0
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains a Blight Encounter",
          "optional": False
        }
      ],
      "flavourText": "We pulled you from the raging ocean, young Dhunan,\nbut we cannot return you to your home. The Order of the Djinn\noffers you a place on Wraeclast.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-blight-scarab",
      "listingCount": 9315
    },
    {
      "id": 60098,
      "name": "Rusted Abyss Scarab",
      "icon": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvU2NhcmFicy9MZXNzZXJTY2FyYWJBYnlzcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/5afc346c84/LesserScarabAbyss.png",
      "stackSize": 10,
      "itemClass": 0,
      "sparkline": {
        "data": [
          0,
          -6.25,
          2.08,
          4.17,
          4.17,
          4.17,
          4.17
        ],
        "totalChange": 4.17
      },
      "lowConfidenceSparkline": {
        "data": [
          0,
          -6.25,
          2.08,
          4.17,
          4.17,
          4.17,
          4.17
        ],
        "totalChange": 4.17
      },
      "implicitModifiers": [],
      "explicitModifiers": [
        {
          "text": "Area contains an additional Abyss",
          "optional": False
        }
      ],
      "flavourText": "As the hordes of bone and blood and foul magic surge across the Vastiri Plains,\nthe scant survivors of our akhara agree to your alliance, ash-scarred Ahkeli.\nDisorder means death. Order may mean life.",
      "chaosValue": 0.5,
      "exaltedValue": 0,
      "count": 99,
      "detailsId": "rusted-abyss-scarab",
      "listingCount": 8031
    }
]
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
    return render(request,'items/scarabs.html', {'scarab_list': scarab_list})
  
def weapons(request):
    return render(request,'items/weapons.html', {'weapon_list': weapon_list})