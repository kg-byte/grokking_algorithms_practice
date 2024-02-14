# Recap
# 1. Greedy algorithms optimize locally, hoping to end up with a global optimum.
# 2. NP-complete( Nondeterministic polynomial ) problems have no known fast solution.
#    If a problem is NP and all other NP problems are polynomial-time reducible to it, then the problem is NP-complete.
# 3. Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.

STATIONS = dict[str, set[str]]


def find_final_stations(stations: STATIONS, states_needed: set[str]):
    final_stations: set[str] = set()

    while states_needed:
        best_station: str | None = None
        states_covered: set[str] = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station
            if best_station:
                states_needed -= states_covered
                final_stations.add(best_station)
    return final_stations


def main():
    states_needed: set[str] = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations: STATIONS = {}
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = {"wa", "id", "mt"}
    stations["kthree"] = {"or", "nv", "ca"}
    stations["kfour"] = {"nv", "ut"}
    stations["kfive"] = {"ca", "az"}
    assert find_final_stations(stations, states_needed) == {
        "ktwo",
        "kthree",
        "kone",
        "kfive",
    }


if __name__ == "__main__":
    main()
