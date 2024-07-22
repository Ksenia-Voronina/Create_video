import cv2
import numpy as np
import transliterate


def create_video(line: str):
    # Ширина и высота видео
    width = 1920
    height = 1080

    # Преобразуем строку: русские символы заменяем английскими
    line = transliterate.translit(line, 'ru', reversed=True)

    # Кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Начальные координаты для бегущей строки
    x = width
    y = height // 2

    # Параметры шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    if len(line) >= 20:
        font_scale = 1
        font_thickness = 1
    else:
        font_scale = 5
        font_thickness = 5
    font_color = (0, 255, 127)  # Зеленый цвет текста

    # Размеры текста в пикселях
    line_len = cv2.getTextSize(line, font, font_scale, font_thickness)

    # Видеопоток с частотой 24 кадра в секунду
    out = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 72, (width, height))

    while True:
        # Очистка кадра
        frame.fill(0)

        # Новые координаты для бегущей строки
        x -= 10  # Скорость бегущей строки

        # Добавляем текст
        cv2.putText(frame, line, (x, y), font, font_scale, font_color, font_thickness)

        # Записываем кадр
        out.write(frame)

        if x + line_len[0][0] < 0:
            break
    
    # Закрываем видеопоток
    out.release()
    return {'title': line, 'path': f"videos/{line}.mp4"}

# Создаём видео
def main():
    line = input('Введите текст бегущей строки: ')
    create_video(line)


if __name__ == '__main__':
    main()
