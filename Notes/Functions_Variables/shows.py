SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family"
]

def main():
    cleanes_shows = []
    for show in SHOWS:
        cleanes_shows.append(show.strip().title())
    
    print(", ".join(cleanes_shows)) #how to join elements

main()