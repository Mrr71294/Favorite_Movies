import media
import fresh_tomatoes

coraline = media.Movie('Coraline',
                        'While exploring her new home, a girl named Coraline (Dakota Fanning) discovers a secret door, behind which lies an alternate world that closely mirrors her own but, in many ways, is better. She rejoices in her discovery, until Other Mother (Teri Hatcher) and the rest of her parallel family try to keep her there forever. Coraline must use all her resources and bravery to make it back to her own family and life.',
                        'http://t0.gstatic.com/images?q=tbn:ANd9GcSppDqGFUI8XOVnfo4W4Y38FCh-yvueqCnUy03O3YxoPK7vgA1s',
                        'https://www.youtube.com/watch?v=8UrcuKK-xqg')

jurassic_park = media.Movie('Jurassic Park',
                            "In Steven Spielberg's massive blockbuster, paleontologists Alan Grant (Sam Neill) and Ellie Sattler (Laura Dern) and mathematician Ian Malcolm (Jeff Goldblum) are among a select group chosen to tour an island theme park populated by dinosaurs created from prehistoric DNA. While the park's mastermind, billionaire John Hammond (Richard Attenborough), assures everyone that the facility is safe, they find out otherwise when various ferocious predators break free and go on the hunt.",
                            'https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg',
                            'https://www.youtube.com/watch?v=mmn7ovP-i4k')

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life.',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                    'On the lush alien world of Pandora live the Na\'vi, beings who appear primitive but are highly evolved. Because the planet\'s environment is poisonous, human/Na\'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na\'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.',
                    'http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp',
                    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

ratatouille = media.Movie('Ratatouille',
                            'Remy dreams of becoming a great chef, despite being a rat in a definitely rodent-phobic profession. He moves to Paris to follow his dream, and with the help of hapless garbage boy Linguini he puts his culinary skills to the test in the kitchen but he has to stay in hiding at the same time, with hilarious consequences. Remy eventually gets the chance to prove his culinary abilities to a great food critic but is the food good? A Pixar animation.',
                            'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                            'https://www.youtube.com/watch?v=uVeNEbh3A4U')

nightmare_b4_christmas = media.Movie('Titanic',
                                    'James Cameron\'s "Titanic" is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the "ship of dreams" -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.',
                                    'https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg',
                                    'https://www.youtube.com/watch?v=2e-eXJ6HgkQ')


movies = [coraline,jurassic_park,toy_story,avatar,ratatouille,nightmare_b4_christmas]

fresh_tomatoes.open_movies_page(movies)
