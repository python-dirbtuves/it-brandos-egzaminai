from os.path import join

estimate_travel_time_in_minutes = lambda distance, speed: round(float(distance) / int(speed) * 60)
min_to_hmin = lambda minutes: (minutes // 60, minutes % 60)


def access_file(file_dir: str):
    with open(join(file_dir, "Duom2.txt"), 'r', encoding='utf-8') as f:
        yield from f


def main(data_file_dir: str):
    lines = access_file(data_file_dir)
    with open(join(data_file_dir, "Rez2.txt"), 'w', encoding='utf-8') as fout:
        average_speed, departure_hours, departure_minutes = next(lines).split()[1:]
        departure_time_in_minutes = int(departure_hours) * 60 + int(departure_minutes)
        for line in lines:
            city, distance = line.split()
            departure_time_in_minutes += estimate_travel_time_in_minutes(distance, average_speed)
            print("{:15}{} val. {} min.".format(city, *min_to_hmin(departure_time_in_minutes)), file=fout)
