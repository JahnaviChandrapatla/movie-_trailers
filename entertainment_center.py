import fresh_tomatoes
import media

rangam=media.Me("Rangam",
                "Ashwin, a famous photographer, works with Renuka, an investigative journalist. When one of their colleagues, Saro, gets killed during a political meet, Ashwin and Renuka decide to investigate.",
                "http://2.bp.blogspot.com/-DLbp3CrX9Dw/TeoAM8XKHwI/AAAAAAAAACU/fIciunQbPZo/s1600/RANGAM-TELUGU-MOVIE-2011-ACDE.jpg",
                "https://youtu.be/n2PTFPdrGGI")
#print(rangam.storyline)
sisindri=media.Me("Sisindri",
                  "Sisindri's kidnapping comes as a shocker to his parents and they try to search for him. But he manages to escape from the clutches of his kidnappers and safely returns home.",
                  "https://upload.wikimedia.org/wikipedia/en/5/57/Sisindri.jpg",
                  "https://youtu.be/g6y8vyVM6NQ")
#print(sisindri.storyline)
#sisindri.show_trailer()
seventh_sense=media.Me("Seventh sense",
                      "You have a world to win",
                      "https://movie.webindia123.com/movie/2011/Regional/October/7thSense/wallpaper/7thSense8.jpg",
                      "https://www.youtube.com/watch?v=Ajahp5n3544")

krrish=media.Me("krrish",
                "a young man who has inherited supernatural powers thanks to his father's encounter with an alien.",
                "https://smedia2.intoday.in/indiatoday/images/stories/2013aug/krrish3_poster-1_1_660_081613024004.jpg",
                "https://www.youtube.com/watch?v=3qa3L9rTEG0")

damarukam=media.Me("Damarukam",
                   "The film story is when an evil power threatens the world and his beloved, he decides to stand up against it and fight to save the world.",
                   "https://files.prokerala.com/movies/pics/1920/anushka-shetta-and-nagarjuna-stills-14416.jpg",
                   "https://www.youtube.com/watch?v=i8nWSMMIVhM")
life_is_beautiful=media.Me("Life is beautiful",
                          "A college student, moves to his uncle's house in Hyderabad and meets various people in the neighbourhood, rich and poor alike.",
                          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1TAQSfsf4_X3gKJS6KYQCbYK7hMeSXwQHZhf-A--p1JXUiT_O",
                          "https://youtu.be/RE4tqo2eYjw")

mes=[rangam,sisindri,seventh_sense,krrish,damarukam,life_is_beautiful]
fresh_tomatoes.open_movies_page(mes)
