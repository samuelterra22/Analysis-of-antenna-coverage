import requests

url_base = "http://sistemas.anatel.gov.br"
request_url = url_base + "/se/public/view/b/export_licenciamento.php"

face_response = requests.post(
    request_url,
    data={
        # "skip": 500,
        "filter": 1,
        # "rpp": 250,
        "fc_7": "MG",
        # "fc_8": 3138203
    }
)

response_json = face_response.json()

if len(response_json) == 1:

    redirect_url = face_response.json()['redirectUrl']
    file_name = redirect_url.split('=')[1] + ".zip"

    try:
        print("Por favor aguarde, realizando download do arquivo '" + file_name + "'...")
        r = requests.get(url_base + redirect_url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)
        print("Download realizado com sucesso!")
    except:
        print("Ocorreu um erro ao realizar o download...")

else:
    print(response_json['title'])
    print(response_json['message'])
