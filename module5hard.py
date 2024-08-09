from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = int(age)

    def __hash__(self):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == hash(nickname):
                self.current_user = nickname
        else:
            print('Введен не верный логин или пароль.')
        return

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
        nickname = User(nickname, password, age)
        self.users.append(nickname)
        self.current_user = nickname
        return

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search):
        search = search.lower()
        search_ = []
        for i in self.videos:
            if search in i.title.lower():
                search_.append(i.title)
        return search_

    def watch_video(self, name_video):
        for i in self.videos:
            if i.title == name_video:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                    continue
                elif i.adult_mode is True:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        continue
                for j in range(i.time_now, i.duration):
                    print(j + 1, end=' ')
                    sleep(1)
                print("Конец видео")
                i.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
