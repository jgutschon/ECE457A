#!/usr/bin/python3


class CityMap:
    def __init__(self):
        self.city_dict = {}

    def add_city(self, city: int, adj_city: int, dist: int) -> None:
        if city not in self.city_dict:
            self.city_dict[city] = [(adj_city, dist)]
        else:
            self.city_dict[city].append((adj_city, dist))

    def show_cities(self) -> None:
        print("City\t| Adj Cities: (Name, Dist)")
        print("----\t| ------------------------")
        for city in self.city_dict:
            print(f"{city}:\t", end="")
            for city_tup in self.city_dict[city]:
                print(f" ({city_tup[0]}, {city_tup[1]}),\t", sep="", end="")
            print("")

    def find_ucs_path(self, start: int, goal: int):
        fringe = []
        total_dist = 0
        curr = start

        fringe.append(curr)

        while curr is not goal:
            # Remove from fringe
            fringe.pop(0)

            # Sort adjacent cities in order of ascending distance
            adj_cities = self.city_dict[curr]
            adj_cities.sort(key=lambda tup: tup[1])

            for city_tup in adj_cities:
                fringe.append(adj_cities[0])

            curr = fringe(0)

        return


if __name__ == "__main__":

    # build question 1 city map
    city_map = CityMap()
    city_map.add_city(6, 5, 35)
    city_map.add_city(6, 10, 30)
    city_map.add_city(6, 9, 26)
    city_map.add_city(6, 2, 38)
    city_map.add_city(5, 1, 5)
    city_map.add_city(5, 6, 35)
    city_map.add_city(1, 8, 24)
    city_map.add_city(1, 5, 5)
    city_map.add_city(8, 1, 24)
    city_map.add_city(8, 10, 15)
    city_map.add_city(8, 3, 23)
    city_map.add_city(10, 6, 30)
    city_map.add_city(10, 8, 15)
    city_map.add_city(10, 3, 24)
    city_map.add_city(10, 9, 26)
    city_map.add_city(3, 8, 23)
    city_map.add_city(3, 10, 24)
    city_map.add_city(3, 4, 7)
    city_map.add_city(9, 6, 26)
    city_map.add_city(9, 10, 26)
    city_map.add_city(9, 4, 18)
    city_map.add_city(9, 2, 26)
    city_map.add_city(9, 7, 35)
    city_map.add_city(4, 3, 7)
    city_map.add_city(4, 9, 18)
    city_map.add_city(2, 6, 38)
    city_map.add_city(2, 9, 26)
    city_map.add_city(2, 7, 32)

    city_map.show_cities()


# {
#     a: [ (b, 10), (c, 32), (d, 21) ],
#     b:
# }
