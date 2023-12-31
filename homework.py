class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        print(f'Тип тренировки: {self.training_type};'
              'Длительность: {self.duration} ч.;'
              'Дистанция: {self.distance} км;Ср. скорость: {self.speed} км/ч;'
              'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
LEN_STEP = 0.65
M_IN_KM = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return super().get_distance()

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return super().get_mean_speed()   
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() + 
                  self.CALORIES_MEAN_SPEED_SHIFT) * 
                  self.weight / self.M_IN_KM * self.duration)

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    WEIGHT_COEF_1 = 0.035
    WEIGHT_COEF_2 = 0.029 
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return super().get_distance()

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return super().get_mean_speed()   
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.WEIGHT_COEF_1 * self.weight + 
                (self.get_mean_speed()**2 / self.height) * 
                self.WEIGHT_COEF_2 * self.weight) * self.duration)

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return super().show_training_info()
    


class Swimming(Training):
    """Тренировка: плавание."""
LEN_STEP = 1.38
COEFF_SPEED = 1.1
COEFF_SPEED_MULTIPLY = 2
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool : int,
                 count_pool : int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return super().get_distance()

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool / 
               self.M_IN_KM / self.duration)
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.COEFF_SPEED) * 
                self.COEFF_SPEED_MULTIPLY * self.weight * 
                self.duration)

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return super().show_training_info()


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
