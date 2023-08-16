url = "https://retosdeprogramacion.com?year=2023&challenge=0&category=1&level=2&language=1&author=1&order=1&sort=1&search="
parametros = url.split("&")
for parametro in parametros:
    try:
        print(parametro.split("=")[1])
    except:
        break