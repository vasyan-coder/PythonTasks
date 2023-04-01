def generate_groups():
    groups = []
    prefixes = ['ИВБО', 'ИКБО', 'ИСБО', 'ИТБО']
    for pref in prefixes:
        for i in range(1, 9):
            groups.append(f'{pref}-{str(i).zfill(2)}-21')
    return groups


if __name__ == "__main__":
    print(generate_groups())
