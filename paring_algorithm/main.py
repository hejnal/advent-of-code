#!/usr/bin/env python
import random

CSE = 1
DS = 2

all_peeps = [("Renke Pan", DS), ("Donald Seaton", CSE), ("Larissa Barra", CSE), ("Mehdi Dahmani", CSE), ("Peter Pakkenberg", CSE), ("Simon Schellaert", CSE), ("Tom Symonds", CSE), 
    ("Wojtek Hejna", CSE), ("Ali Sarraf", CSE), ("Gigi Bozzo", CSE), ("Jota Urdaneta", CSE), ("Luca Stanziano", DS), ("Seif Ben Abda", CSE), ("Tad Baljevic", CSE), ("Tom Oczos", CSE), 
    ("Christiane Ahlheim", DS), ("Darragh Kelly", DS), ("Dirk Nachbar", DS), ("Semih Oguz", CSE), ("Sumedha Menon", DS), ("Alessandro Mariani", DS)]


def parse_week(week_num):
    """ Returns a collection of people from a given week """

    if week_num == 1:
        return {"Dirk Nachbar": ["Mehdi Dahmani"], "Mehdi Dahmani": ["Dirk Nachbar"], "Darragh Kelly": ["Tad Baljevic"], "Tad Baljevic":["Darragh Kelly"], 
            "Larissa Barra":["Wojtek Hejna"], "Wojtek Hejna": ["Larissa Barra"], "Paola Igarteburu": ["Paola Igarteburu"], "Paola Igarteburu": ["Donald Seaton"],
            "Alessandro Mariani": ["Peter Pakkenberg"], "Peter Pakkenberg":["Alessandro Mariani"], "Christiane Ahlheim": ["Ali Sarraf"], "Tom Symonds":["Gigi Bozzo"],
            "Gigi Bozzo":["Tom Symonds"]}
    elif week_num == 2:
        return {"Donald Seaton": ["Christiane Ahlheim"], "Christiane Ahlheim": ["Donald Seaton"], 
        "Larissa Barra": ["Darragh Kelly"], "Darragh Kelly":["Larissa Barra"], 
            "Mehdi Dahmani":["Peter Pakkenberg"], "Peter Pakkenberg": ["Mehdi Dahmani"], 
            "Tom Symonds": ["Dirk Nachbar"], "Dirk Nachbar": ["Tom Symonds"],
            "Tad Baljevic": ["Seif Ben Abda"], "Seif Ben Abda":["Tad Baljevic"]}
    elif week_num == 3:
        return {"Donald Seaton": ["Darragh Kelly"], "Darragh Kelly": ["Donald Seaton"], 
        "Larissa Barra": ["Christiane Ahlheim"], "Christiane Ahlheim":["Larissa Barra"], 
            "Mehdi Dahmani":["Sumedha Menon"], "Sumedha Menon": ["Mehdi Dahmani"], 
            "Peter Pakkenberg": ["Seif Ben Abda"], "Seif Ben Abda": ["Peter Pakkenberg"],
            "Tad Baljevic": ["Dirk Nachbar"], "Dirk Nachbar":["Tad Baljevic"]}
    
    else:
        return {}

def main(new_attendees):
    week1 = parse_week(1)
    week2 = parse_week(2)
    week3 = parse_week(3)

    available_cse = [value[0] for value in all_peeps if value[0] in new_attendees and value[1] == CSE]
    print("Available CSEs: {}".format(available_cse))

    available_ds = [value[0] for value in all_peeps if value[0] in new_attendees and value[1] == DS]
    print("Available DSs: {}".format(available_ds))

    output = {}

    for index, cse in enumerate(available_cse):
        for other in (available_ds + available_cse[index:]):
            # check all the previous weeks
            assigned = False

            if ((cse in week1 and other in week1[cse]) or (cse in week2 and other in week2[cse]) or (cse in week3 and other in week3[cse])) or cse == other: 
                continue
            else:
                output[cse] = [other]
                print("Assigning {} to {}".format(other, cse))
                assigned = True

            if assigned == False:
                random_group = list(output.keys())[random.randint(0, len(output) - 1)]
                print("Cannot find any one else, merging groups...")
                output[random_group].append(cse)

            if other in available_cse:
                available_cse.remove(other)
            if other in available_ds:
                available_ds.remove(other)
            
            break

    print("Remaining list: available CSEs: {}, DS: {}".format(available_cse, available_ds))
    return output

if __name__ == "__main__":
    new_attendees = ["Alessandro Mariani", "Christiane Ahlheim", "Darragh Kelly", "Dirk Nachbar", "Donald Seaton", "Larissa Barra", "Mehdi Dahmani", "Peter Pakkenberg", "Sumedha Menon", "Tad Baljevic"]
    output = main(new_attendees)
    print("Final list is: {}".format(output))