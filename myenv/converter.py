import requests

img_url = 'https://scontent.cdninstagram.com/v/t51.29350-15/464712093_1125596162517389_3407031986031854389_n.heic?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi45NjB4MTIwMC5zZHIuZjI5MzUwLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=f8k46iw50ZgQ7kNvgH_bR-P&_nc_gid=3cb378b498a14ec1b8c2f7240dff48b8&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzQ4ODY1NTI4NDg4OTYwNTE1MQ%3D%3D.3-ccb7-5&oh=00_AYARSQTFmVY8LXoOsB_fECnvNRHom38Qi5COdNpOrmBgCA&oe=67288DCC&_nc_sid=10d13b'
video_url='https://youtu.be/e_kf-X8FFn8'

def get_img(url=''):
    try:
        response = requests.get(url=url)
        with open('img_downloud.jpg','wb') as file:
            file.write(response.content)
        return 'Изображение скачано'
    except Exception as _ex:
        return "Проверьте ссылку"

def get_video(url=''):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open('video_kdownloud.mp4', 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024*1024):
                    if chunk:
                        file.write(chunk)
        return 'Видео скачано'
    except Exception as _ex:
        return "Проверьте ссылку"



def main():
    print(get_video(url=video_url))
    print(get_img(url=img_url))


if __name__ == "__main__":
    main()